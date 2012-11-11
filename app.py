from flask import Flask, render_template, request, Response

from utils.caching import get_cached_data
from githubuser import user_forks
from githubarchive import languages, available_archives


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    """Index
    """
    def title(r):
        return r.endpoint.replace('_', ' ').title()

    def description(r):
        doc = globals().get(r.endpoint).__doc__
        return '' if doc is None else doc.rstrip()

    ignored = ['static', 'cached_json']

    views = [{'url': r.rule,
              'title': title(r),
              'description': description(r)}
             for r
             in app.url_map.iter_rules()
             if r.endpoint not in ignored]
    return render_template('index.html', views=views)


@app.route('/cache/<filename>')
def cached_json(filename):
    """For serving the json file in ``cache`` directory
    """
    return Response(get_cached_data(filename), mimetype='application/json')


@app.route('/github/user/forks')
def github_forks():
    """Commits of users in github repos forked by them
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
    """Github repository activities per language
    """
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
