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

Installing the Server
=====================

To install all the necessary Ubuntu packages, run the following commands::

    $  sudo apt-get update
    $  sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx python3-dev

Create your Virtualenv
======================

Virtualenv was installed in the previous step. Now you can create your virtualenv::

    $ virtualenv sps
    $ source sps/bin/activate

Installation of Dependencies
=============================

Make sure you have your virtualenv activated, whch::

    $ pip install -r sps/requirements.txt

Cloning your project
=====================

Once you virtualenv is created and django is installed you can clone the code
to you virtualenv::

    $ git clone https://github.com/dancaps/sps.git

Demo
================

http://www.sps.dancaps.xyz/

username: demo
password: p@ssw0rd123
