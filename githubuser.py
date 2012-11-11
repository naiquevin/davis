import sys
import pprint
from collections import Counter

from utils.github import get_forks, get_self_commits, repos as user_repos
from utils.caching import cache_json_data as cache


@cache
def user_forks(user):
    forks = get_forks(user)
    selfcommits = {}
    for fork in forks:
        repo = fork['name']
        selfcommits[repo] = len(get_self_commits(repo, user))
    return selfcommits


@cache
def primary_languages(user):
    repos = user_repos(user)
    langs = map(lambda x: x['language'], repos)
    groups = Counter()
    for lang in langs:
        groups[lang] += 1
    return dict(groups.items())


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    script, user = sys.argv
    pp.pprint(user_forks(user))
    
