from flask import Flask, render_template, request
import json
from githubuser import analyze_forks

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return 'Davis: Experiments in Data Analysis & VISualizations'


@app.route('/github/forks')
def github_forks():
    username = request.args.get('username')
    if username not in [None, '']:
        fork_commits = analyze_forks(username)
        return render_template('github.html',
                               data=True,
                               username=username,
                               fork_commits=fork_commits,
                               json_fork_commits=json.dumps(fork_commits))
    else:
        return render_template('github.html', data=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
