.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/zaitra/geojson-length/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

geojson-length could always use more documentation, whether as part of the
official geojson-length docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/zaitra/geojson-length/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `geojson-length` for local development.

1. Fork the `geojson-length` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/geojson-length.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv geojson-length
    $ cd geojson-length/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 geojson-length tests
    $ python setup.py test or pytest
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.com/zaitra/geojson-length/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests.test_geojson_length


To make sure our code is [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant, we use:

- [black code formatter](https://github.com/psf/black)
- [Flake8 code linter](http://flake8.pycqa.org)

There's a [pre-commit](https://pre-commit.com) config file in [.pre-commit-config.yaml](.pre-commit-config.yaml).
To [utilize pre-commit](https://pre-commit.com/#usage), install pre-commit with `pip3 install pre-commit` and then either:

- `pre-commit install` - to install pre-commit into your [git hooks](https://githooks.com). pre-commit will from now on run all the checkers/linters/formatters on every commit. If you later want to commit without running it, just run `git commit` with `-n/--no-verify`.
- Or if you want to manually run all the checkers/linters/formatters, run `pre-commit run --all-files`.

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.
