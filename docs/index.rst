============
fastqtools
============


Introduction
============

fastq is used to clean raw fastq data...

Authors
=======

.. _authors:
    
    - kongdeju <kongdeju@genehe.com>

Status
======

.. note::

    **not reviewed yet.**


Installation
============

use git to clone code::

    git clone git@192.168.1.251:/home/git/fastqtools.git


..  attention::

    if you want to run ``fastqtools`` on local server without docker , try to add ``config.py``.


Usage
=====

    
just type command::

    /path/to/fastqClean.py -h
    /path/to/fastqStat.py -h
    /path/to/fastqSplit.py -h


developments followed by ``Dcer`` rules, script will need a yaml file,which shoud contain following key and values

must_args
---------

- args1
    desc of args2

- args2
    desc of args2
 
optinal args
------------

- args3
    desc of args3


here is a sample yaml file::

    args1: value of args1
    args2: value of args2


RUN
===

cli way
-------

copy and paste to your input yaml file and call script::

    /path/of/ctpips.py -c your.yml


serer way
---------

send request to jbios with ``/start/ctpips/``::

    req = requests.get("http://<server>:port/ctpips/",data=json.dumps(indict))

for jbios detail information check api documentation `here <http://192.168.1.251:4700/dev-docs/jbios/>`_


Code
====

.. toctree::
   :maxdepth: 1

    Guide <index>
    Code Docs <api/modules>
