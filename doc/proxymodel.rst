Filtering and Ordering
======================

In order to filter and order the view, we will need to use a proxy model.

Creating a Proxy Model
----------------------

In order to create a proxy model, we need to use the following syntax:

.. code-block:: python

   from PySide.QtGui import QSortFilterProxyModel

   class Proxy(QSortFilterProxyModel):
       def __init__(self, model):
           super(proxy, self).__init__()
           self.model = model

.. note:: Even though the example above uses PySide, you might want to replace
   it by PyQt4, PyQt5 or whichever library you are using.

Sorting Items
-------------

It is possible to enable sorting in a view by adding the following to its
initialization method. When doing this, you will be able to toggle the order
of the items by clicking on the header of a specific column:

.. code-block:: python

   self.setSortingEnabled(True)

Filtering Items
---------------

placeholder
