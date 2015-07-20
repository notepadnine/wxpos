# Introduction #

wxpos is designed to be database independent. Currently it is best working with MySQL. It can also be used with SQLite. Support for PostgreSQL will be available soon.
This is made possible with [SQLAlchemy](http://sqlalchemy.org). There will also be support for MS-SQL Server and other RDBMS that SQLAlchemy supports.
In the pos/database directory, there are currently two files:
  * init: defines the init function. Creates the engine, session and all that is used for SQLAlchemy ORM.
  * config.py: interface to use the configuration system for connection to database systems

# Configuring MySQL #

In addition to that there is a dialog for configuration in pos/modules/base/dialogs/dbconfig.py
This dialog is used when running 'wxpos -c' or '--config'. You can then choose the mysql host, username, password, port, db name or sqlite filename to use.

Run "wxPos.py -c" or "wxPos.py --config" to configure the database, with optional testing values.