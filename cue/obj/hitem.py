class HItem(object):
    ''' Custom object to be used in hierarchical structures '''

    def __new__(self, *args, **kwargs):
        '''
        Constructor for the hitem object
        Make sure that a name is specified
        '''

        assert 'name' in kwargs, "A name must be specified"
        return super(HItem, self).__new__(self, args, kwargs)

    def __init__(self, *args, **kwargs):
        parent = kwargs.get('parent', None)
        self._name = kwargs['name']
        self._children = []
        self._parent = parent

        if parent:
            parent.addChild(self)

    # -------------------------------------------------------------------------
    # Hierarchical Methods
    # -------------------------------------------------------------------------

    def addChild(self, child):
        '''
        Adds a child node to the current one
        '''

        self._children.append(child)

    def deleteChild(self, child):
        '''
        Delete a child object from the current one
        '''

        self._children.remove(child)

    def child(self, row):
        '''
        Returns the child node of the current one that has a specific index
        '''

        return self._children[row]

    def childCount(self):
        '''
        Return the amount of children of the current node
        '''

        return len(self._children)

    def parent(self):
        '''
        Return the parent of the current node
        '''

        return self._parent

    def setParent(self, parent):
        '''
        Sets the parent for the current object
        '''

        if self._parent:
            self._parent.deleteChild(self)

        parent.addChild(self)
        self._parent = parent

    def row(self):
        '''
        Return the index of this node relative to its parent
        '''

        if self._parent is not None:
            return self._parent._children.index(self)

    # -------------------------------------------------------------------------
    # Object Representation Methods
    # -------------------------------------------------------------------------

    def log(self, tabLevel=-1):
        output = ''
        tabLevel += 1

        for i in range(tabLevel):
            output += '   '

        output += '|- ' + self._name + '\n'

        for child in self._children:
            output += child.log(tabLevel)

        tabLevel -= 1

        return output

    def __repr__(self):
        return self.log()

    # -------------------------------------------------------------------------
    # Properties
    # -------------------------------------------------------------------------

    @property
    def name(self):
        return self._name
