Creating Hierarchical Items
---------------------------

We can create hierarchical items using the :func:`HItem <cue.obj.hitem.HItem>`
object. All you need to do is create an instance of the class and provide a
name:

.. code-block:: python

   from cue.obj.hitem import HItem

   root = HItem(name='Project')

.. warning:: Upon creation, it is mandatory to specify a name. This is done
   using the `name` keyword parameter. Failing to provide one will raise an
   *assertion exception*.
