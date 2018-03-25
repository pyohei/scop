SCOP(String Converter of Python)
================================

SCOP is the simple string convert tool written with Python. There are some features in this tool.

-  Simple protocol
-  Simple web interface
-  Enable to customize this code as you want!

Sample
------

.. image:: https://i.imgur.com/Yourjqg.png

Install
-------

You can install this script as follows.

.. code:: bash

    git clone https://github.com/pyohei/scop.git

And you need to install python libraries which this tool required.

.. code:: bash

    pip install -r requirements.txt

Usage
-----

After clone this repository, you can excecute by the below command.

.. code:: bash

    python web.py

Environment
-----------

- Python 2.7.10
- Python 3.6.1

Customize
---------

You can add your original module if you want.
The way to create is below.

#. Create module file under ``converter`` directory
#. Add ``convert`` module having first argument.(``converter/_sample.py`` is sample file.)

After you can add your module, you can see your original converter from browser choices.
If you want to add modules into my repository, please give me Pull Request :)

Licence
-------

-  MIT
