from PySide import QtCore


class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, root, parent=None):
        super(TreeModel, self).__init__(parent)

        self._rootNode = root

    def index(self, row, column, parent):
        '''
        MUST BE IMPLEMENTED

        Returns the index of the item in the model specified by the given row,
        column and parent index.

        If parent is not valid, rootNode will be used. - 'parent' method
        returns an empty QModelIndex if the element is the root node.

        Then we get the child that has the specific index. If for some reason,
        the child is empty, we return an empty QModelIndex. Otherwise, we
        create an index and we return it.
        '''

        parentNode = self.getNode(parent)
        childItem = parentNode.child(row)

        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        '''
        MUST BE IMPLEMENTED

        Returns the parent of the model item with the given index . If the item
        has no parent, an invalid PySide.QtCore.QModelIndex is returned.

        Gets the reference to the 'Node' object for the current selection.
        Gets the parent of the Node and finally wraps it up into a QModelIndex
        which is returned. If it does not have a parent, an empty QModelIndex
        will be used.
        '''

        # Get a reference to the 'Node' object
        node = self.getNode(index)

        if node == self._rootNode:
            return QtCore.QModelIndex()

        # Gets its parent by using the 'parent' method
        parentNode = node.parent()

        # If the parent node is the root
        if parentNode == self._rootNode:
            return QtCore.QModelIndex()

        return self.createIndex(parentNode.row(), 0, parentNode)

    def rowCount(self, parent):
        '''
        MUST BE IMPLEMENTED

        Returns the amount of children that a given item (parent) has.
        '''

        parentNode = self.getNode(parent)
        return parentNode.childCount()

    def columnCount(self, parent):
        '''
        MUST BE IMPLEMENTED

        Returns the number of columns for the children of the given parent .
        In most subclasses, the number of columns is independent of the parent
        '''

        return 1

    def data(self, index, role):
        '''
        MUST BE IMPLEMENTED

        Returns the data stored under the given role for the item referred to
        by the index
        '''

        node = self.getNode(index)
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return node.name

        if role == QtCore.Qt.UserRole + 1:
            if index.column() == 0:
                return node

    def getNode(self, index):
        '''
        NOT REQUIRED

        Given a QModelIndex, returns internal pointer to the object if the
        index is valid or the root node if the index is not valid
        '''

        if index.isValid():
            node = index.internalPointer()
            if node:
                return node

        return self._rootNode

    def flags(self, index):
        ''' This procedure makes items enabled and selectable '''

        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled

        node = index.internalPointer()
        if node.childCount() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled
