[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/16.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow
the <a href="https://www.odoo.com/documentation/16.0/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>,
or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>,
the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start
with <a href="https://www.odoo.com/documentation/16.0/developer/howtos.html">the developer tutorials</a>

# Set-up

Project name is `courses management`

## Note

* If you are Odoo developer set up my mini-project will not be problem for you )))

* If you know Odoo developer then please ask him/her to set up my mini-project

* If you are NOT Odoo developer ((( there is a long and easy road ahead of us

`GOOD LUCK`

## Get project

clone project to local machine

```shell
$ git clone https://gitlab.com/abduraxmon1/odoo-course.git
$ cd odoo-course
$ python3 -m venv venv
```

## Development

Activate virtual environment in Linux machine

```shell
$ source .venv/bin/activate
```

Activate virtual environment in Windows machine

```shell
$ venv\Scripts\activate
```

Activate virtual environment in MacOS machine

```shell
$ source venv/bin/activate
```

Install dependencies

```shell
$ pip install -r requirements.txt
```

## Configurations of Python

DO NOT forgot create database in PostgreSQL using odoo interface with database name `odoo16_3`, username `odoo16` and
password `odoo`

also SET this command in python run
configuration `-c {PATH_TO}/debian/odoo.conf -d {database_name} -u {database_username}` and for
script `{PATH_TO}/odoo-bin`
