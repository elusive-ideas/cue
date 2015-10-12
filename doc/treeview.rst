Displaying Hierarchy using QT
=============================

In order to display the model we created, we need to use a treeview. There are
a few things that we can define in the treeview:

- header
- Context Menu for when using right click
- Action to be taken when double click
- Catching key presses

Header visibility
-----------------

By default, the header of the treeview is visible. It is possible to disable
its visibility by using the following code in its initialisator:

.. code-block:: python

   self.header().hide()

Alternatively, you can also hide the header at runtime by calling the method
on the treeview object:

.. code-block:: python

   view.header().hide()

Adding a Context Menu
---------------------

If you want to add a context menu to the treeview, the first thing you'll need
to do is add the following in the initialisator or your treeview:

.. code-block:: python

   self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
   self.customContextMenuRequested.connect(self.context_menu)

Once done, you'll have to implement the name of the method that you are
connected the request to. Here is an example:

.. code-block:: python

   def context_menu(self, pos):
       item = self.item_under_cursor()

       if item:
           self.folderMenu = QtGui.QMenu(self)
           selInExpl_menu = QtGui.QMenu('Item: {0}'.format(item.name), self)
           selInExpl_menu.setEnabled(False)
           self.folderMenu.addMenu(selInExpl_menu)
           self.folderMenu.exec_(QtGui.QCursor.pos())

.. warning:: Notice that the example above uses the treeview's method
'item_under_cursor' in order to get the item currently under the cursor.

Adding double click functionality
---------------------------------

There is nothing special about the implementation of a check for double click
in a treeview. All what needs to be done is connect the event to a function:

.. code-block:: python

self.doubleClicked.connect(self.item_double_clicked)

And then define the function itself:

.. code-block:: python

   def item_double_clicked(self):

       item = self.item_under_cursor()
       if item:
          print item.name

.. warning:: Notice that the example above uses the treeview's method
'item_under_cursor' in order to get the item currently under the cursor.

Catching key presses
--------------------

information about how to catch key presses when using the treeview.
