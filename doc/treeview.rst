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

information about adding a context menu

Adding double click functionality
---------------------------------

information about how to trigger an action when the user double clicks on the
view.

Catching key presses
--------------------

information about how to catch key presses when using the treeview.
