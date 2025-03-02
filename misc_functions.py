'''misc functions for rpg game'''

import os
import msvcrt
import config_manager

def get_debug():
    return bool(int(config_manager.get_config(('DEBUG', 'debug_mode'))))

def cls():
    '''clears screen'''
    if get_debug() is False:
        os_name = os.name
        if os_name == "nt":
            os.system("cls")
        elif os_name == "posix":
            os.system("clear")
        else:
            raise ValueError(f"Unsupported OS. Was {os_name}")

def getch():
    '''gets input without waiting for enter'''
    return msvcrt.getch().decode()

if __name__ == "__main__":
    pass
