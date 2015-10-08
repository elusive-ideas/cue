Hierarchy representation
------------------------

It is possible to get a text representation of the hierarchy of a given
:func:`HItem <cue.obj.hitem.HItem>` object and its children.

Let's assume that we created a hierarchy using something like:

.. code-block:: python

   from cue.obj.hitem import HItem

   root = HItem(name='Project')

   section01 = HItem(name='Section01', parent=root)
   HItem(name='sec01_element_01', parent=section01)
   HItem(name='sec01_element_02', parent=section01)

   section02 = HItem(name='Section02', parent=root)
   HItem(name='sec02_element_01', parent=section02)
   HItem(name='sec02_element_02', parent=section02)

In order to get the text representation all we need to do is print the
:func:`HItem <cue.obj.hitem.HItem>` object:

.. code-block:: python

   print root

Which would output:

.. code-block:: text

   |- Project
      |- Section01
         |- sec01_element_01
         |- sec01_element_02
      |- Section02
         |- sec02_element_01
         |- sec02_element_02
