========================
django-sps-project
========================

My first Django project using Django version 1.10.1

This project was created to manage my wife's pet sitting business.

Features
==================================

Once installed this app will allow you to do the following.

* Create Customers
* Create Pets and assign them to Customers
* Create your Service book     
* Create Orders

In addition, you will be able see active, upcoming and unpaid customers on the dashboard. 

Working Environment
===================

I recommend running this in a virtualenv on Linux

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv sps

Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django==1.10.1

Cloning your project
=====================

Once you virtualenv is created and django is installed you can clone the code
to you virtualenv::

    $ git clone https://github.com/dancaps/sps.git

Installation of Dependencies
=============================

Make sure you have your virtualenv activated::

    $ pip install -r sps/requirements.txt

Demo
================

http://www.sps.dancaps.xyz/

username: demo
password: p@ssw0rd123
