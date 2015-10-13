from PySide import QtGui


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)

        # Attributes
        self.parent = parent

        self.set_behaviours()
        self.parent.trayIcon = self

    def set_behaviours(self):
        self.menu()

    def menu(self):
        menu = QtGui.QMenu(self.parent)

        self.minimizeAction = menu.addAction("Minimize")
        self.restoreAction = menu.addAction("Restore")
        exitAction = menu.addAction("Exit")

        self.restoreAction.setEnabled(False)

        self.minimizeAction.triggered.connect(self.minimize)
        self.restoreAction.triggered.connect(self.restore)
        exitAction.triggered.connect(QtGui.qApp.quit)

        menu.aboutToShow.connect(self.checkStatus)
        self.setContextMenu(menu)
        self.activated.connect(self.systemIcon)

    def checkStatus(self):
        if self.parent.isVisible():
            self.minimizeAction.setEnabled(True)
            self.restoreAction.setEnabled(False)
        else:
            self.minimizeAction.setEnabled(False)
            self.restoreAction.setEnabled(True)

    def systemIcon(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
            # Action to be taken when left click on the tray icon
            self.parent.activateWindow()

        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            # Action to be taken when double click on the tray icon
            self.restore()

        if reason == QtGui.QSystemTrayIcon.MiddleClick:
            # Action to be taken when middle click on the tray icon
            pass

    def restore(self):
        self.parent.show()

    def minimize(self):
        self.parent.hide()
