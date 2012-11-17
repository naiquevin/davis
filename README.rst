Davis
=====

Amateur experiments in **D**ata **A**nalysis and **VIS**ualizations.

Actually an excuse to learn a thing or two about data analysis and to
play around with Pandas_ and d3js_.

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

To be able to run the examples, you will need to download and prepare
some data first. From now, just download a day's activity from
`githubarchive.org`_ as follows::

  $ cd githubarchives
  $ wget http://data.githubarchive.org/2012-11-05-{0..23}.json.gz

Next, convert the json files into a single csv files as follows::

  (davisenv)$ cd ../
  (davisenv)$ python
  >>> import glob
  >>> from githubarchive import csvify_activities
  >>> files = glob.glob('githubarchives/2012-11-05-*.json.gz')
  >>> csvify_activities(files, 'githubarchives/activities-2012-11-05.csv')


Running the examples in browser.
--------------------------------

All examples are packaged as a webapp using the Flask_ web framework
and therefore can be run the browser by running the development server
locally. Assuming that Flask would have already been installed from the 
requirements.txt file, you can start the dev server as follows::

  (davisenv)$ python app.py

Now open http://127.0.0.1:5000 in your browser.


.. _Pandas: http://pandas.pydata.org/
.. _d3js: http://d3js.org/
.. _`githubarchive.org`: http://www.githubarchive.org/
.. _Flask: http://flask.pocoo.org/

