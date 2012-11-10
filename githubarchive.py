import os
import glob
import gzip
import json
from contextlib import contextmanager
from collections import Counter

"""
Analyzing data obtained from Github archive <http://githubarchive.org>
"""

@contextmanager
def githubarchive(archive):
    f = gzip.open(archive)
    lines = f.readlines()
    lines = (line.rstrip('\n') for line in lines)
    data = (json.loads(line) for line in lines)
    yield data
    f.close()


def languages(archive):
    repos = []
    with githubarchive(archive) as data:
        langs = Counter()
        for action in data:
            try:
                r = action['repository']['name']
                if r in repos:
                    continue
                langs[action['repository']['language']] += 1
            except KeyError:
                pass
    return langs


def available_archives():
    """List all the archives downloaded and available locally for
    analysis

    """
    return [os.path.basename(p) for p in glob.glob('githubarchives/*.json.gz')]

