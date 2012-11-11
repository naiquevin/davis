from flask import Flask, render_template, request, Response

from utils.caching import get_cached_data
from githubuser import user_forks
from githubarchive import languages, available_archives


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return 'Davis: Amatuer Experiments in Data Analysis & VISualizations'


@app.route('/cache/<filename>')
def cached_json(filename):
    """For serving the json file in ``cache`` directory
    """
    return Response(get_cached_data(filename), mimetype='application/json')


@app.route('/github/user/forks')
def github_forks():
    """Commits of users in repos forked by them
    """
    username = request.args.get('username')
    template = 'github_user_forks.html'
    if username not in [None, '']:
        jsonfile = user_forks(username)
        return render_template(template,
                               data=True,
                               username=username,
                               jsonfile=jsonfile)
    else:
        return render_template(template, data=False)


@app.route('/github/activity/languages')
def github_activity_languages():
    archives = available_archives()
    archive = request.args.get('archive')
    template = 'github_activity_languages.html'
    if archive not in [None, '']:
        archive_dataset = 'githubarchives/%s' % archive
        jsonfile = languages(archive_dataset)
        return render_template(template,
                               data=True,
                               archives=archives,
                               archive=archive,
                               jsonfile=jsonfile)
    else:
        return render_template(template,
                               archives=archives,
                               data=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
