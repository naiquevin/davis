import json

from flask import Flask, render_template, request
from githubuser import analyze_forks
from githubarchive import languages, available_archives


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return 'Davis: Amatuer Experiments in Data Analysis & VISualizations'


@app.route('/github/forks')
def github_forks():
    username = request.args.get('username')
    if username not in [None, '']:
        fork_commits = analyze_forks(username)
        return render_template('github_user_forks.html',
                               data=True,
                               username=username,
                               fork_commits=fork_commits,
                               json_fork_commits=json.dumps(fork_commits))
    else:
        return render_template('github_user_forks.html', data=False)


@app.route('/github/activity/languages')
def github_activity_languages():
    archives = available_archives()
    archive = request.args.get('archive')
    if archive not in [None, '']:
        archive_dataset = 'githubarchives/%s' % archive
        langs = languages(archive_dataset)
        return render_template('github_activity_languages.html',
                               data=True,
                               json_languages=json.dumps(langs),
                               total_languages=len(langs),
                               archive=archive,
                               archives=archives)
    else:
        return render_template('github_activity_languages.html',
                               archives=archives,
                               data=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
