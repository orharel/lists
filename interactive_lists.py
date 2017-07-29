"""Interactive Lists"""


import argparse

import utils


class InteractiveLists():
    """InteractiveLists"""

    def __init__(self, storage_file='.storage'):
        self.root_list = utils.load_from_storage(storage_file)
        self.current_list = self.root_list
        self.lists = []

    def add_list(self):
        """Adding a list"""
        list_name = input('New list: ')
        self.current_list.add_list(list_name)

    def edit_list_name(self):
        """Changing a list name"""
        list_name = input('Change list: ')
        with utils.preset_input(list_name):
            new_list_name = input('New list name: ')
        self.current_list.change_list_name(list_name, new_list_name)

    def remove_list(self):
        """Removing a list"""
        list_name = input('Remove list: ')
        self.current_list.remove_list(list_name)

    def enter_list(self):
        """Enter into another list"""
        list_name = input('Enter list: ')
        if not self.current_list.is_list_exists(list_name):
            raise RuntimeError('List doesn\'t exists!')
        self.lists.append(self.current_list)
        self.current_list = self.current_list.get_list(list_name)

    def exit_list(self):
        """Exit list to parent list"""
        if self.current_list == self.root_list:
            raise RuntimeError('You\'re alredy in the last list')
        self.current_list = self.lists.pop()

    def add_item(self):
        """Adds an item"""
        item = input('New item: ')
        self.current_list.add_item(item)

    def edit_item(self):
        """Edit an item"""
        item = input('Edit item number: ')
        with utils.preset_input(item):
            new_item = input('New item: ')
        self.current_list.change_item(item, new_item)

    def remove_item(self):
        """Remove an item"""
        item = input('Remove item: ')
        self.current_list.remove_item(item)

    def do_action(self, user_input):
        """Perform an action according to the user's input"""
        if user_input in ['1', 'add', 'add list']:
            self.add_list()
        elif user_input in ['2', 'edit', 'edit list', 'edit list name']:
            self.edit_list_name()
        elif user_input in ['3', 'remove', 'remove list']:
            self.remove_list()
        elif user_input in ['4', 'enter', 'enter list']:
            self.enter_list()
        elif user_input in ['5', 'exit', 'exit list']:
            self.exit_list()
        elif user_input in ['6', 'add', 'add item']:
            self.add_item()
        elif user_input in ['7', 'edit', 'edit item']:
            self.edit_item()
        elif user_input in ['8', 'remove', 'remove item']:
            self.remove_item()
        else:
            print('Bad option...')

    def display_current_list(self):
        """Print the current list to the screen"""
        lists_names = self.current_list.get_lists()
        items = self.current_list.get_items()
        print('~~~~~')
        print('\nLists:')
        utils.print_ordered_iterable(lists_names)
        print('\nItems:')
        utils.print_ordered_iterable(items)
        print('~~~~~')

    def interact(self):
        """Interact with the user"""
        self.display_current_list()
        print('\n'.join(['(1) Add list',
                         '(2) Edit list name',
                         '(3) Remove list',
                         '(4) Enter list',
                         '(5) Exit list',
                         '(6) Add item',
                         '(7) Edit item',
                         '(8) Remove item']))
        user_input = input('Action: ')
        try:
            self.do_action(user_input)
        except RuntimeError as ex:
            print(ex)

    def run(self):
        """Run InteractiveLists interaction"""
        while True:
            self.interact()


def main():
    parser = argparse.ArgumentParser(description='Interactive lists from the cli')
    parser.add_argument('--storage-file', default='.storage', type=str)
    args = parser.parse_args()

    interactive_lists = InteractiveLists(**vars(args))
    interactive_lists.run()

if __name__ == '__main__':
    main()
