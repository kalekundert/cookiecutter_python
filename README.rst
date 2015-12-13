****************
cookiecutter-kxg
****************

A cookiecutter template for my python libraries.  See 
https://github.com/audreyr/cookiecutter.  This cookiecutter will::

1. Create a ``setup.py`` file that is immediately ready to use.

2. Create a ready-to-use Sphinx directory for documentation.

3. Create a test command that can be called from anywhere in the repository.

4. Create an ``__init__.py`` with ``__version__`` filled in.

5. Copy the MIT license text into the project.

6. Configure Travis CI to run pytest and to deploy new versions to PyPI.

7. Create a virtual environment with ``know_its_ok``, ``bumpversion``, 
   ``sphinx``, and your new library already installed.

8. Create a ``git`` repository and commit all the boilerplate files included in 
   the cookiecutter.

Making a new library
====================
Just give ``cookiecutter`` the path to this repository and answer all of its 
questions::

   cookiecutter https://github.com/kalekundert/cookiecutter_pylib.git

If you find yourself using this cookie cutter a lot, you can save yourself some 
typing by aliasing it in your ``~/.cookiecutterrc`` file::

   abbreviations:
       py: https://github.com/kalekundert/cookiecutter_pylib.git

Publishing to PyPI
==================
When you want to publish a version of your library to PyPI, the first step is 
to increment the version number stored in ``__init__.py`` and to commit that 
with a tag that matches the new version.  You can do using the ``bumpversion`` 
command (pre-installed in the virtual environment) to do this automatically::

   $ bumpversion major
   $ bumpversion minor
   $ bumpversion patch

Then, assuming you've enabled Travis CI for the repository, just push to 
``github``.  Travis CI will run your tests again to make sure the new version 
works as expected and will then automatically deploy to PyPI::

   $ git push

Not Exactly What You Want?
==========================
If you have differences in your preferred setup, I encourage you to fork this
to create your own version.  Or create your own; it doesn't strictly have to
be a fork.  It's up to you whether or not to rename your fork/own version. Do 
whatever you think sounds good.  I'll also accept pull requests if they're 
small, atomic, and if they make my own development experience better.

.. _Travis-CI: http://travis-ci.org/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
