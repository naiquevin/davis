import urllib2
from urllib import urlencode
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
        response = request(url)
        data = json.loads(response.read())
        return data
    return dec


@cache_dict('repos')
@octoget
def repos(user):
    return 'users/%s/repos' % user


@cache_dict('commits')
@octoget
def commits(repo, user, params=None):
    """Get user's commits in the repo"""
    params = {} if params is None else params
    return 'repos/%s/%s/commits?%s' % (user, repo, urlencode(params))
    


def get_forks(user):
    allrepos = repos(user)
    forks = [r for r in allrepos if r['fork'] == True]
    return forks


def get_self_commits(repo, user):
    return commits(repo, user, {'author': user})


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)

    allrepos = repos("naiquevin")
    forks = [r for r in allrepos if r['fork'] == True]

    pp.pprint(forks)
