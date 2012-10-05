import urllib2
import pprint
from functools import wraps
import json

from utils.caching import cache_dict


API_URL = 'https://api.github.com'


def octourl(urlpath):
    return '%s/%s' % (API_URL, urlpath)


def request(url):
    return urllib2.urlopen(url)


def octoget(func):
    @wraps(func)
    def dec(*args, **kwargs):
        url = octourl(func(*args, **kwargs))
        response = request(url).read()
        data = json.loads(response)
        return data
    return dec


@cache_dict('repos')
@octoget
def repos(user):
    return 'users/%s/repos' % user


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)

    allrepos = repos("naiquevin")
    forks = [r for r in allrepos if r['fork'] == True]

    pp.pprint(forks)
