import os
import json
from functools import wraps

CACHE_DIR = '/home/vineet/python/projects/dave/cache'


def cache_dict(prefix):
    def _cache_dict(func):
        @wraps(func)
        def dec(*args, **kwargs):
            slug = '-'.join([prefix]+list(args))
            cache_file = os.path.join(CACHE_DIR, slug) + '.json'
            if os.path.exists(cache_file):
                print 'Loading data from cache..'
                with open(cache_file) as f:
                    return json.load(f)
            else:
                print 'No cached data found. Fetching via API..'
                data = func(*args, **kwargs)                
                with open(cache_file, 'w+') as f:
                    json.dump(data, f, indent=4)
                return data
        return dec
    return _cache_dict
