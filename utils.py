"""Utils for lists"""


import pickle
import readline
from contextlib import contextmanager

import lists


def load_from_storage(storage_file='.storage'):
    """Loads lists object from a file"""
    try:
        with open(storage_file, 'rb') as fp:
            return pickle.load(fp)
    except FileNotFoundError:
        return lists.List('root')


def save_to_storage(data, storage_file='.storage'):
    """Dumps lists object to a file"""
    with open(storage_file, 'rb') as fp:
        pickle.dump(data, fp)


@contextmanager
def preset_input(string):
    """Setting user input to string when `input` is called"""
    def _pre_input_hook():
        readline.insert_text(string)
        readline.redisplay()

    readline.set_pre_input_hook(_pre_input_hook)
    try:
        yield
    finally:
        readline.set_pre_input_hook()


def print_ordered_iterable(iterable):
    """Prints ordered list"""
    for i, item in enumerate(iterable):
        print('({i}) {item}'.format(i=i+1, item=item))
