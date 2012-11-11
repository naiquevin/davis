import os
import re
import json
from functools import wraps

CACHE_DIR = '/home/vineet/python/projects/davis/cache'


def arg_to_tokens(a):
    if isinstance(a, dict):
        return '-'.join(['%s_%s' % (x, y) for (x, y) in a.iteritems()])
    else:
        return slugify(a)


def slugify(name):
    return re.sub(r'\W+','-',name)


def cache_json_resp(prefix):
    """Decorator for caching the response of http request in json
    format
    """
    def _cache_resp(func):
        @wraps(func)
        def dec(*args, **kwargs):
            slug_tokens = [prefix]+map(arg_to_tokens, args)
            slug = '-'.join(slug_tokens)
            cache_file = os.path.join(CACHE_DIR, slug) + '.json'
            if os.path.exists(cache_file):
                with open(cache_file) as f:
                    return json.load(f)
            else:
                data = func(*args, **kwargs)
                with open(cache_file, 'w+') as f:
                    json.dump(data, f, indent=4)
                return data
        return dec
    return _cache_resp


def cache_json_data(func):
    """Decorator for caching processed data in json file
    """
    @wraps(func)
    def dec(*args, **kwargs):
        slug = '-'.join([func.__name__]+map(arg_to_tokens, args))
        filepath = os.path.join(CACHE_DIR, slug) + '.json'
        if not os.path.exists(filepath):
            data = func(*args, **kwargs)
            with open(filepath, 'w+') as f:
                json.dump(data, f, indent=4)
        return '/cache/%s.json' % slug
    return dec


def get_cached_data(filename):
    with open(os.path.join(CACHE_DIR, filename)) as f:
        return f.read()
                  

