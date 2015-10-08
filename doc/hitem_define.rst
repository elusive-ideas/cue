Hierarchical Relationships
--------------------------

It is possible to establish hierarchical relationships by using `parent`
parameter upon creation or by calling the
:func:`setParent <cue.obj.hitem.HItem.setParent>` method once the object
already exists.

Here is an example in which the parent is set upon creation:

.. code-block:: python

   from cue.obj.hitem import HItem

   root = HItem(name='Project')
   section01 = HItem(name='Section01', parent=root)

Here is an example in which the parent is set once the object is already
created:

.. code-block:: python

   from cue.obj.hitem import HItem

   root = HItem(name='Project')
   section01 = HItem(name='Section01')
   section01.setParent(root)

.. note:: The objects of type :func:`HItem <cue.obj.hitem.HItem>` can have only
   one parent.

.. warning:: When using the :func:`setParent <cue.obj.hitem.HItem.setParent>`
   method on a :func:`HItem <cue.obj.hitem.HItem>` that already has a parent,
   it will remove itself from the old parent and add itself to the new one.
