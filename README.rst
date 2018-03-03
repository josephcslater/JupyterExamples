.. image:: https://mybinder.org/badge.svg :target: https://mybinder.org/v2/gh/josephcslater/iPythonExamples/master

Jupyter Examples
================

Illustrative examples iPython (Jupyter) notebooks for those trying to learn
Python. (Also, notes to myself)

To play with them *now* without any installations, you can try these all out on `mybinder.org <https://mybinder.org/v2/gh/josephcslater/iPythonExamples/master>`_.

.. _installing_python:

Installing Python
_________________

In order to be able to use the notebooks you need a working scientific python installation.

The easiest path to this is to install Python via `Anaconda`_. There are other distributions- I endorse this one based on it seeming to kept up to date the best. **You must install** Python 3.5 or later for these notebooks to work. **Do note install Python 2.7.**

This proceeds as a normal install on your platform (Mac, Windows, Linux...).

Subsequently you must update some components of Anaconda by using the *conda* command from the *Anaconda Command Prompt*. On Windows, this runs as an actual program.

To ensure the conda package list is as up to date as possible::

  conda update conda

Then update everything else with::

  conda update --all

To use `Jupyter`_ (the notebook), launch a terminal on Mac or Linux, or the Anaconda Terminal on Windows (or similar name) and type:

.. code-block:: bash

   jupyter notebook

It's all in the GUI from here. You just need to play around a bit.

.. _github: http://www.github.com
.. _Anaconda: http://continuum.io/downloads
.. _Jupyter: http://www.jupyter.org

Your feedback is appreciated. Please also look
at other demonstrations on `my blog <http:josephcslater.github.io>`_.
