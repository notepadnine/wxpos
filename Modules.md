# Modules #

A wxpos module is a part of the software which has a specific role in it: as "user" that gives the ability to login to the software or "stock" that allows the user to keep track of his stock, etc...

It is a directory in the pos/modules/ directory which can/must contain the following elements: (suppose the name of the module "mname")
  * pos/modules/mname/init.py that defines the init function that is called once before the application is run.
  * pos/modules/mname/config.py that defines:
    * the dependencies tuple (that contains a list of other modules on which it depends)
    * a ModuleMenu class (which defines the menu items this module should have in the menu)
    * the load\_database\_objects function that will load the main objects of the module that will allow SQLAlchemy to configure the db tables for that module
    * the test\_database\_values function that will insert test database values if the user chooses to.
  * pos/modules/mname/objects/ A python module, usually based on the "base" module objects and the SQLAlchemy Base declarative object, that define an interface to the database system. Anyway, see the pos/modules/base/objects/common.py and the pos/modules/user/objects/user.py for example to understand it.
  * pos/modules/mname/panels/ Contains the panels used in the main toolbook of the app frame. That means every menu item should have a panel defined in that python module associated with it, as the the app frame contains essentially only a wx.Toolbook whose pages are the menu items and the panels to which each one is associated...
  * pos/modules/mname/dialogs/ Contains the dialogs that could be used for the functionality of the module to be complete.
  * pos/modules/mname/windows/ Contains the common windows/widgets (ex. listbox, notebook, controls, ...) that are used in many panels/dialogs...

That structure is recommended but not required. One thing is absolutely required: the dependencies tuple, even if it is empty...

That is a list of all modules done and to be done:

## BASE ##

### Content ###
Base module that provides the most basic functionality of the pos system. It is a base that should be extended by other modules.
  * idManager: object: Keeps track of given ids to windows in a dict. If a key is missing, it assigns a wx.NewId() to that key. This is no longer essential as ids are used rarely. It has been removed.
  * common: object: Base module for easy connection between database and object. Provides a set of similar functions for deleting, updating, adding and finding items. The find function was removed because useless now that SQLAlchemy is used, others may be removed also. Using queries instead.
  * manage: panel: Base panel for CRUD operation (new item, delete item, update item, list items)

### TODO ###
  * Add a common interface for module configurations.

## CURRENCY ##

### Content ###
Curency module that manages multiple currencies, with their symbols, default currency and conversion between one and another
  * currency: object: Allows conversion between units, retreiving the default one and all the other functionality of the currency module (name, symbol, value for conversion). ex: 1500 LL = 1$ => LL value=1; $ value=1500x1 = 1500
  * currencies: panel: UI based on managePanel that allows editing of value and name and symbol of the currencies. Be careful when deleting currencies as it might cascade delete all the products and customers associated to it.

### TODO ###
  * add the ability to change the default currency


## CUSTOMER ##

### Content ###
A customer might be a person or a company that frequently purchases from the company. Discounts may be associated to it, debts, and periodic bill payments.
  * customer: object: Stores and retrieves customer info, contact details and address details. Based on the common object
  * customergroup: object: Stores and retrieves the name of the group of customers and a comment about it. Based on the common object
  * customers: panel: Manage Panel to the customers (list, add, delete, edit)
  * customergroups: panel: Manage Panel to the groups.

### TODO ###
  * Contact and Address to be added
  * customerdiscount: discount(0%-100%), product, customer


## USER ##

### Content ###
A user is a person who can login and use the application. Every one of them has a password, a role, and specific permissions that limit its use of it. These are usually the employees, manager and owners of the shop.
  * user: object: Username, password
  * role: object: Name, list of permissions
  * permission: object: Name, description of what is allowed to do with that one.
  * users,roles,permissions: panel: Based on ManagePanel. Allow management of users, their roles, their permissions.
  * user: panel: Allows limited editing of the currently logged in user by himself.
  * superuser: object Acts almost as a user that has all the permissions. Should not always be used, as not tested with every module.

### TODO ###
  * the permissions should be assigned to a MenuRestriction objects that would allow or disallow the use of a certain panel in the toolbook

## STOCK ##

### Content ###
Provides functionality for adding and removing products that can be sold in the shop. These can be grouped in nested(or not) categories.
  * category: Name, parent category.
  * product: object: Name, description, price, currency, barcode, reference, quantity, category.
  * categories,products: panel: Based on ManagePanel. Allow management of categories and products.

### TODO ###
  * add ability to set buy price, sell price, taxes (like in [POSper](http://posper.org))


## SALES ##

### Content ###
Provides the ability to create tickets and sell items to customers and customers with browsable categories and products and customers.
  * ticket: object: list of lines of sold items (which can be based on products or not) (may be assigned to a customer)
  * ticketline: object: line which contains a description of what is sold, price and amount.
  * main: panel: Main panel in which is available a catalog (products/customers), a ticketline list and ticket manipulation actions.

### TODO ###
  * Print functionality
  * Cash drawer functionality
  * Cash register functionality (close cash): cash difference, date open date close, user, etc...


## PAYMENT ##

### Content ###
Provides the ability to add shop payments made for maintenance, salaries, stock buying or other expenses or incomes to keep track of cash flow.

### TODO ###
Not done yet.


## REPORT ##

### Content ###
Provides the abilty to generate reports of stock, payments, etc. on specific time period.
Generates reports in the PDF format,( maybe excel also(later)) using reportlab.

There are reports for these options currently: stock, sales, user's sales, customer's bought items, stock diary (ins and outs). All these should have filter options to choose currencies, products, and other restrictions on data displayed.

### TODO ###
  * Arrange the filter process to make the reports as customizable as possible.
  * Add the ability to choose the design of the report pages, plus the header and footer and stuff.


## TAXES ##

### Content ###
Seen in [POSper](http://posper.org). Not planned for, yet.

### TODO ###
Not done yet.