Using the Tray Icon
===================

There are instances in which you want your applications to keep running even
when the user closes the window. Then use a Tray Icon in order to retrieve
the interface.

You can easily implement this kind of functionality by adding the following
lines to the initialisator of your main window:

.. code-block:: python

   icon = QtGui.QIcon(r"X:\path_to_an_icon\icon.png"
   self.trayIcon = cue.widget.systemtrayicon.SystemTrayIcon(icon), self)
   self.trayIcon.show()

.. note:: The example above assumes that you already imported the module
   `cue.widget.systemtrayicon`

This will provide you with a Tray Icon for the application. By default, there
are some options that will be available to you when using right click on the
icon. These options will allow you to minimize/restore the window as well as
closing the application.

To get the most out of this kind of functionality, it would be good if the
maximize and minimize buttons in the main interface are disabled. You can do
this by adding the following to the initialisator of the window:

.. code-block:: python

   self.setWindowFlags(QtCore.Qt.Dialog)

It's also a good idea to let your users know that the application is still
running in the background and explain how they can restore it. You can do that
by re-implementing the `closeEvent` function. Here is an example:

.. code-block:: python

   def closeEvent(self, event):
       self.hide()
       if self.trayIcon:
           self.trayIcon.showMessage('Application Name',
                                     ('The application will remain running '
                                      'in the background. Use this icon to '
                                      'restore it.'))
       event.ignore()
