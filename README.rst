******************
cookiecutter_pyapp
******************

A cookiecutter template for my python applications.  See 
https://github.com/audreyr/cookiecutter.  This cookiecutter will::

1. Configure a ``pyproject.toml`` file to be used with ``flit`` to package and 
   distribute the project.

2. Configure a ``docs`` directory for use with Sphinx and Read The Docs.

3. Configure a ``tests`` directory for use with ``pytest``.

4. Configure Travis CI to run ``pytest`` and copy coverage results to 
   Coveralls.

5. Create an ``__init__.py`` with ``__version__`` filled in, and configure 
   ``bumpversion`` to manage that version number.

6. Create a ``README.rst`` file with badges indicating the health of the 
   project.

7. Copy either the MIT of GPLv3 license into the project.

8. Create a ``git`` repository and commit all the boilerplate files included in 
   the cookiecutter.

Making a new application
========================
Just give ``cookiecutter`` the path to this repository and answer all of its 
questions::

   cookiecutter https://github.com/kalekundert/cookiecutter_pyapp.git

If you find yourself using this cookiecutter a lot, you can save yourself some 
typing by aliasing it in your ``~/.cookiecutterrc`` file::

   abbreviations:
       py: https://github.com/kalekundert/cookiecutter_python.git

Publishing to PyPI
==================
When you want to publish a version of your library to PyPI, the first step is 
to make sure all of the tests pass on the continuous integration server.  
Enable Travis CI for the repository (if you haven't already) and push to 
GitHub::

   $ git push

Once the tests pass, use ``bumpversion`` to increment the version number as 
appropriate::

   $ bumpversion major
   $ bumpversion minor
   $ bumpversion patch

Then, use ``flit`` to publish the new release to PyPI::

   $ flit publish

Not Exactly What You Want?
==========================
If you have differences in your preferred setup, I encourage you to fork this 
to create your own version.  Or just create your own; it doesn't strictly have 
to be a fork.  It's up to you whether or not to rename your fork/own version. 
Do whatever you think sounds good.  I'll also accept pull requests if they're 
small, atomic, and if they make my own development experience better.

.. _Travis-CI: http://travis-ci.org/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
