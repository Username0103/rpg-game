'''misc functions for rpg game'''

#pylint: disable = E0401, E0606

import os
import config_manager

if os.name == 'posix':
    import sys
    import tty
    import termios
elif os.name == 'nt':
    import msvcrt
else:
    raise NotImplementedError


def get_debug() -> bool:
    '''uses config.ini to determine if debug mode is on.'''
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

def getch() -> str:
    '''gets input without waiting for enter'''
    if os.name == 'posix':
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return msvcrt.getch().decode()

if __name__ == "__main__":
    char = getch()
    print(f'getch was {char}')
