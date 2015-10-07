hitem
=====

`hitem` is a custom kind of object that allows the user to create hierarchical
structures easily.

Creating a hitem
-----------------

asd

Defining hierarchy
------------------

asd

Hierarchy representation
------------------------

It is possible to get a representation of the hierarchy of any `hitem` object
and his children by simply printing the object:

>>> from cue.obj.hitem import HItem
>>>
>>> root = HItem(name='Project')
>>> section01 = HItem(name='Section01', parent=root)
>>> HItem(name='sec01_element_01', parent=section01)
>>> HItem(name='sec01_element_02', parent=section01)
>>> section02 = HItem(name='Section02', parent=root)
>>> HItem(name='sec02_element_01', parent=section02)
>>> HItem(name='sec02_element_02', parent=section02)
>>>
>>> print root
|- Project
   |- Section01
      |- sec01_element_01
      |- sec01_element_02
   |- Section02
      |- sec02_element_01
      |- sec02_element_02
