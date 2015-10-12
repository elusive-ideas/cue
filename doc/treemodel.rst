Preparing hierarchy for QT
==========================

We need to add our data to a tree model. We can do that using the following
syntax:

.. code-block:: python

   from cue.model.treemodel import TreeModel
   model = TreeModel(tree)

The model specifies the following things:

- Amount of rows/columns
- Data that needs to be displayed on each row and column
- Properties/flags of the items displayed (Selectable, Enabled, etc)

Specifying amount of rows
-------------------------

When working with hierarchical structures created with Hitems, there is no need
to specify the amount of rows as the amount of items in the hierarchy will be
used.

Specifying amount of columns
----------------------------

By default, the treemodel provided by `cue` has only one column. If you want to
change the amount of columns, it is possible to specify a new number by using
the following syntax:

.. code-block:: python

   def columnCount(self, parent):
       ''' Return the amount of columns for the model '''

       return 1

Specifying the data to be displayed
-----------------------------------

The `data` method is used to define the data that needs to be displayed in the
treeview. By default,

.. code-block:: python

   def data(self, index, role):
       node = self.getNode(index)
       if role == QtCore.Qt.DisplayRole:
           if index.column() == 0:
               return node.name

       if role == QtCore.Qt.UserRole + 1:
           if index.column() == 0:
               return node

Specifying Item properties
--------------------------

The item properties are defined using the `flags` method of the `TreeModel`
class.

.. code-block:: python

   def flags(self, index):
       ''' This procedure makes items enabled and selectable '''

       if not index.isValid():
          return QtCore.Qt.ItemIsEnabled

       node = index.internalPointer()
       if node.childCount() == 0:
          return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
       else:
          return QtCore.Qt.ItemIsEnabled
