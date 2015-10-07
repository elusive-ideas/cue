from PySide import QtCore
from PySide import QtGui


class TreeView(QtGui.QTreeView):
    def __init__(self):
        super(TreeView, self).__init__()
        self.set_behaviour()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

    def set_behaviour(self):
        self.doubleClicked.connect(self.item_double_clicked)
        self.customContextMenuRequested.connect(self.context_menu)

    def item_double_clicked(self):

        item = self.item_under_cursor()
        if item:
            # Do something
            print item.name

    def context_menu(self, pos):
        '''
        If RMB is used and the mouse is over a selectable item, a menu will be
        displayed for it.
        '''

        item = self.item_under_cursor()

        if item:
            self.folderMenu = QtGui.QMenu(self)
            selInExpl_menu = QtGui.QMenu('Item: {0}'.format(item.name), self)
            selInExpl_menu.setEnabled(False)
            self.folderMenu.addMenu(selInExpl_menu)
            self.folderMenu.exec_(QtGui.QCursor.pos())

    def item_under_cursor(self):
        '''
        Return the item under the cursor or none
        Relies on the item being selectable
        '''

        selected = self.selectedIndexes()
        if not selected:
            return None

        index = selected[0]
        model = self.model()

        node = model.data(index, QtCore.Qt.UserRole+1)
        return node
