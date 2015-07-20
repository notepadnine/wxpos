Cross platform pos software with support for barcode readers, receipt printer(not yet) and cash drawer control(not yet also).
Designed for retail shops, but could be extended for restaurants in the future.

Use MySQL or SQLite as database system. Support for PostgreSQL is under work. See [Database](Database.md) for more details.

Stand-alone application dependencies:
  * MySQL (for MySQL support)

Source dependencies:
  * Python (tested on Python 2.7)
  * wxPython (tested on wx-2.8-msw-unicode and "unstable" wx-2.9.2-msw)
  * MySQLdb module (for MySQL support)
  * MySQL (tested on 5.1) (for MySQL support)
  * reportlab for pdf reports

The project is still "new born". But you can see it running.
Support for customers, products (grouped in categories), users (whose roles are defined and have certain permissions), and a main page to sell products and browse them.
Support for reports of sales, stock and cash difference(generated in pdf format or excel maybe) is under way, but can be tried.
Much more to go including receipt printer/cash drawer functionality, discounts...

Functionality and UI are based on the open-source Java "POSper" and "Openbravo" softwares.

Help would be much appreciated, whether it is for testing or for programming or just feedback (user experience, features, issues).

# Announcement #

In the past few months, you might have noticed development was slow on wxpos. This project is not dead, it is being reborn :)

Seeing the growing interest in this project that started as a way to fulfill personal requirements, I and some friends came up with a new, better, nicer, bigger project: Coinbox POS. These people are those that brought you Lemon POS, also an open-source POS project you certainly have heard of if you have ever searched for such a thing. They are: Miguel Chavez Bamboa (main developer of Lemon POS) and Benjamin Burt (contributor to Lemon POS)

Coinbox POS will be a nicer and more mature wxPos (taking advantage of Lemon's experience) and a more customizable Lemon POS (inspired by wxPos's modules system and Python choice of doing things).

Stay tuned for more information soon to be announced. In the meantime, you can always check out the mess (until now ;) ) on [Github](https://github.com/coinbox/coin.box)