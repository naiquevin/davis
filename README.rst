Davis
=====

Amateur experiments in Data analysis and Visualizations.

Actually an excuse to learn a thing or two about data analysis and to
play around with Pandas and d3js.

Setup
-----

You will need Python and few other dependencies for running the
examples. The best way is to create a new virtualenv and install all
python based dependencies ::

  $ virtualenv davisenv --no-site-packages
  $ source davisenv/bin/activate
  (davisenv)$ cd /path/to/davis/repo
  (davisenv)$ pip install -r requirements.txt


Downloading some data
---------------------

Before running to examples, you will need to download and prepare some
data. From now, just download a day's activity from githubarchive.org::

  $ cd githubarchives
  $ wget http://data.githubarchive.org/2012-11-05-{0..23}.json.gz

Then convert the json files into a single csv files as follows::

  $ cd ../
  $ python
  >>> import glob
  >>> from githubarchive import csvify_activities
  >>> files = glob.glob('githubarchives/2012-11-05-*.json.gz')
  >>> csvify_activities(files, 'githubarchives/activities-2012-11-05.csv')


Running the examples in browser.
--------------------------------

This is a webapp and can be run in browser. It uses the Flask framework
(previous commands must have taken care of installing it)::

  (davisenv)$ python app.py

Now open http://0.0.0.0:5000 in your browser.

