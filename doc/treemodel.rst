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
