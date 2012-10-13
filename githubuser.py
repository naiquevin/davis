import sys
import pprint

from utils.github import get_forks, get_self_commits


def analyze_forks(user):
    forks = get_forks(user)
    selfcommits = {}
    for fork in forks:
        repo = fork['name']
        selfcommits[repo] = len(get_self_commits(repo, user))
    return selfcommits


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    script, user = sys.argv
    pp.pprint(analyze_forks(user))
    
