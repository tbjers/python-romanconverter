romanconverter
==============

This project provides a converter for `Roman numerals <https://en.wikipedia.org/wiki/Roman_numerals>`_.

Setup
-----

This project requires ``pyenv-virtualenv``. In order to install, please
follow the `installation instructions <https://github.com/pyenv/pyenv-virtualenv#installation>`_.

Activate a virtual environment before all other steps.

Installation
------------

Install dependencies::

    $ make init

Run script
----------

Run the script inside ``virtualenv``::

    $ make virtualenv
    $ dec2roman 2018

Testing
-------

Run tests::

    $ make test

Get coverage::

    $ make coverage
