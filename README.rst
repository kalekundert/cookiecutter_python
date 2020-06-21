*******************
cookiecutter_python
*******************

A cookiecutter template for my python applications.  See 
https://github.com/audreyr/cookiecutter.  This cookiecutter will::

1. Create a ``git`` repository and commit all the boilerplate files included in 
   the cookiecutter.

2. Configure ``commitlint`` to require `conventional commits`__.

   __ https://www.conventionalcommits.org/en/v1.0.0-beta.2/

1. Configure a ``pyproject.toml`` file to be used with ``flit`` to package and 
   distribute the project.

2. Configure a ``docs`` directory for use with Sphinx_ and `Read The Docs`_.

3. Configure a ``tests`` directory for use with ``pytest``.

4. Configure GitHub Actions to run ``pytest``, copy coverage results to 
   Coveralls_, and deploy to PyPI using ``python-sematic-release``.
   
6. Create a ``README.rst`` file with badges indicating the health of the 
   project.

7. Copy either the MIT or GPLv3 license into the project.

Using the cookiecutter
======================
Just give ``cookiecutter`` the path to this repository and answer all of its 
questions::

   cookiecutter https://github.com/kalekundert/cookiecutter_python.git

If you find yourself using this cookiecutter a lot, you can save yourself some 
typing by aliasing it in your ``~/.cookiecutterrc`` file::

   abbreviations:
       py: https://github.com/kalekundert/cookiecutter_python.git

Not Exactly What You Want?
==========================
If you have differences in your preferred setup, I encourage you to fork this 
to create your own version.  Or just create your own; it doesn't strictly have 
to be a fork.  It's up to you whether or not to rename your fork/own version. 
Do whatever you think sounds good.  I'll also accept pull requests if they're 
small, atomic, and if they make my own development experience better.

.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _Coveralls: https://coveralls.io/
