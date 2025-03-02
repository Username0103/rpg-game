'''used to "wrap" a module to avoid circulat imports.'''

import importlib

def import_specific(module_name, function_name):
    '''from module import func'''
    module = importlib.import_module(module_name)
    return getattr(module, function_name)

def import_all(module_name):
    '''from module import *'''
    module_obj = importlib.import_module(module_name)
    globals_dict = globals()
    for name in dir(module_obj):
        if not name.startswith('_'):
            globals_dict[name] = lambda *args, _name=name, **kwargs: getattr(
                importlib.import_module(module_name), _name)(*args, **kwargs)

if __name__ == "__main__":
    cls = import_specific('misc_functions', 'cls')
    cls()
    import_all('misc_functions')
