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

Advanced Sorting
----------------

Placeholder text

Filtering Items
---------------

placeholder
