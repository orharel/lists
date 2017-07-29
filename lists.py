"""Lists module"""


class List():
    """List"""

    def __init__(self, name, lists=None, items=None):
        self.name = name
        self._lists = lists or []
        self._items = items or []

    def is_list_exists(self, list_name):
        """Return if list exists or not"""
        return list_name in [l.name for l in self._lists]

    def get_list(self, list_name):
        """Return a list in this list"""
        if not self.is_list_exists(list_name):
            raise RuntimeError('List doesn\'t exists!')
        return next(l for l in self._lists if l.name == list_name)

    def get_lists(self):
        """Return the lists' names in this list"""
        return [l.name for l in self._lists]

    def add_list(self, list_name):
        """Add a list to this list"""
        if self.is_list_exists(list_name):
            raise RuntimeError('List with the same name already exists!')
        self._lists.append(List(list_name))

    def change_list_name(self, list_name, new_list_name):
        """Change a list in this list"""
        if not self.is_list_exists(list_name):
            raise RuntimeError('List doesn\'t exists!')
        if self.is_list_exists(new_list_name):
            raise RuntimeError('List with the same name already exists!')
        next(l for l in self._lists if l.name == list_name).name = new_list_name

    def remove_list(self, list_name):
        """Remove a list form this lise"""
        if not self.is_list_exists(list_name):
            raise RuntimeError('List doesn\'t exists!')
        self._lists = [l for l in self._lists if l.name != list_name]

    def get_items(self):
        """Return the items of this list"""
        return self._items

    def add_item(self, item):
        """Add an item to this list"""
        if item in self._items:
            raise RuntimeError('Item already exists!')
        self._items.append(item)

    def change_item(self, item, new_item):
        """Change an item name in this list"""
        if item not in self._items:
            raise RuntimeError('Item doesn\'t exists!')
        if new_item in self._items:
            raise RuntimeError('New item already exists!')
        self._items[self._items.index(item)] = new_item

    def remove_item(self, item):
        """Remove an item from this list"""
        if item not in self._items:
            raise RuntimeError('Item doesn\'t exists!')
        self._items.remove(item)
