import os
import glob
import gzip
import json
import csv
from contextlib import contextmanager
from collections import Counter

import pandas as pd

from utils.caching import cache_json_data as cache

"""
Analyzing data obtained from Github archive <http://githubarchive.org>
"""

@contextmanager
def githubarchive(archive):

    def json_loads(line):
        try:
            return json.loads(line)
        except UnicodeDecodeError:
            line = line.decode('utf-8', errors='replace')
            return json.loads(line)

    f = gzip.open(archive)
    lines = f.readlines()
    lines = (line.rstrip('\n') for line in lines)
    data = (json_loads(line) for line in lines)
    yield data
    f.close()


@cache
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


def csvify_activities(files, output):
    """Convert the githubarchive activities data from json into
    csv. Will return the path to the csv file

    :param files: list of files to be converted to a single csv file

    :param output: path to the output file
    """
    def to_dict(filepath):
        with githubarchive(filepath) as data:
            return [select_fields(d) for d in data if d['actor'] is not None]

    def select_fields(data):
        return {'actor': data['actor'],
                'actor_location': data['actor_attributes'].get('location', '-').encode('utf-8', errors='ignore'),
                'activity_time': data['created_at'],
                'activity_type': data['type']}

    data = reduce(lambda x, y: x + y, [to_dict(f) for f in files])
    fieldnames = ('actor', 'actor_location', 'activity_time', 'activity_type')
    return write_csv(output, data, fieldnames)


def write_csv(outputfile, data, fieldnames):
    """Write data from a list of dicts to a csv file using
    csv.DictWriter. Returns the path to the output file
    """
    with open(outputfile, 'wb') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for d in data:
            writer.writerow(d)
    return outputfile


def count_per_group(data, groupby):
    """An abstraction to run groupby on a pandas DataFrame and return
    the size of each resulting group
    """
    return data.groupby(groupby).apply(lambda g: str(len(g)))


@cache
def activity_types(csvfile):
    activities = pd.read_csv(csvfile)
    series = count_per_group(activities, 'activity_type')
    return series.to_dict()


def available_activity_csv():
    return [os.path.basename(p) for p in glob.glob('githubarchives/activities-*.csv')]

