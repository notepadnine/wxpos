# Introduction #

wxpos is a pos software that should support the use of:
  * Barcode readers
  * Receipt printers
  * Cash drawers
  * Stock maintenance
  * Daily/Monthly/Weekly reports of sold products
  * Customer listing
  * And many more functions that should be easily added based on the need

# Idea #

wxpos is made with Python, using wxPython (subset of wxWidgets).
  * [Python](http://python.org) is used because it is cross-platform mainly.
  * [wxPython](http://www.wxpython.org/) is used for the GUI (graphical user interface) because it is also cross-platform, and provides a native look on any platform.

wxpos is designed to be easily migrated to any database system, currently MySQL and SQLite, and PostgreSQL in the future.

# About the directory structure and files #

There are two files in the main directory:
  * wxPos.py is the main application file. With command-line arguments, you can choose to redirect output to a file and hide the console window(use the -o or --output switch). Use -c or --config to run the database configuration dialog. For more details, use 'python wxPos.py -h'

The pos directory is the main python module used for the wxPos software.
The files in pos directory describe themselves by their names.
The directories are as following:
  * pos/modules/ Discussed in [Modules](Modules.md)
  * pos/database/ Discussed in [Database](Database.md)
  * pos/menu/ Contains the base classes for the menu, menu root items, and sub items. The functionality is there. The menu items are created from within the init.py file of the module itself. See the pos/modules/base/init.py of "base" module and pos/modules/user/init.py of "user" module for usage examples.

The images directory: Contains two directories menu and commands: menu contains icons of the menu entries, and commands some icons for the common actions of the different modules. The images directory should be changed and especially the menu directory, because the images directory should not depend on any module. In the future, there would be a system for images and resources.

The reports directory: all the reports of the report module are created there. If the directory does not exist, I suppose it will be a problem because the directory is not created dynamically. That thing should be fixed. And that directory along with some others if needed should be in a directory called "data".