import sys

from utils.github import repos


def analyze_forks(forks):
    # send request to get this user's commits in each fork
    for fork in forks:
        print fork['name']


def get_forks(user):
    allrepos = repos(user)
    forks = [r for r in allrepos if r['fork'] == True]
    return forks


if __name__ == '__main__':
    script, user = sys.argv
    analyze_forks(user)

