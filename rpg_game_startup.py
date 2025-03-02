
# pylint: disable=C0116
# pylint: disable=C0114

import sys
import misc_functions as mf
import options_menu as options

def menu_backend(selection: str):
    if selection == '1':
        raise NotImplementedError
    if selection == '2':
        options.begin()
    if selection in ('3', 'exit'):
        mf.cls()
        sys.exit()
    else:
        raise ValueError('did not get 1, 2, 3 or "exit" from main_menu() in menu_backend(). '
                         f'Invalid input was {selection}')

def main_menu():
    selected_action = None
    while selected_action not in ['1', '2', '3', 'exit']:
        print('Press 1 to play')
        print('Press 2 for options ')
        print('Press 3 to exit')
        selected_action = input().strip().lower()
    menu_backend(selected_action)


if __name__ == "__main__":
    main_menu()
