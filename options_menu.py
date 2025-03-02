"""manages changing options in a user-friendly manner"""

from time import sleep
import config_manager
import rpg_game_startup as leave
from misc_functions import cls

# pylint: disable=C0116


def begin() -> None:
    while True:
        available_options = config_manager.get_dict_section("USER")
        formatted_options = format_options(available_options)
        ui_result = user_interface(formatted_options, available_options)
        if isinstance(ui_result, str):
            if ui_result == "EXIT":
                cls()
                return leave.main_menu()
            if ui_result == "RESET":
                reset_options()
                continue
        elif ui_result is not None:
            user_input, value = ui_result
            write(user_input, value)
        else:
            raise TypeError(f'ui_result was None in {__name__}')


def format_options(options: dict) -> str:
    norange_keys_list = get_norange_options(options)
    norange_options = dict(zip(norange_keys_list, options.values()))
    formatted_options = [
        f"{num} - {key}. {value}"
        for num, (key, value) in enumerate(norange_options.items(), 1)
    ]
    return "\n".join(formatted_options)


def get_norange_options(options: dict) -> list:
    return [value.split(".")[0] for value in options]


def range_checker_handler(user_input: str, value: str, available_options: dict) -> bool:
    if value.isdigit():
        int_value = int(value)
    else:
        return False
    return bool(range_check((user_input, int_value), available_options))


def user_interface(user_options: str, raw_options: dict) -> tuple[str, str] | str:
    while True:
        cls()
        print(f"Available options to change: \n{user_options}")
        print("Select options via their name or number.")
        print('Input "exit" to go back to the main menu.')
        print('Input "reset" to reset options.')

        user_input = input()

        if user_input.lower() == "exit":
            return "EXIT"
        if user_input.lower() == "reset":
            return "RESET"
        if handled_input := handle_input(user_input, raw_options):
            return handled_input
        cls()
        print("Selected option not available or not in range.")
        print("Please retry.")
        sleep(1)


def handle_input(user_input, options) -> None | tuple[str, str]:
    checked_input = check_input(options, user_input)
    if checked_input and checked_input not in (None, False):
        cls()
        print("What value do you wish to change it to?")
        print(get_range_repr(checked_input, options))
        value = input()
        if not range_checker_handler(checked_input, value, options):
            return None
        return checked_input, value


def get_range_repr(range_of, options):
    ranges = option_range(options)
    if range_of in ranges.keys():
        range_tuple = ranges[range_of]
        return (f'Available values are between '
               f'{range_tuple[0]} and {range_tuple[1]}.')
    raise KeyError(f'Invalid key in {get_range_repr.__name__}. '
                   f'Tried to get key {range_of} in dict {ranges}')


def check_input(options: dict, inp: str) -> None | str:
    list_options = list(options.keys())
    norange_options = get_norange_options(options)

    if len(list_options) != len(norange_options):
        raise IndexError(f'Invalid length in {get_range_repr.__name__}. '
                         f'Tried to zip {list_options} and {norange_options}')

    option_map = dict(zip(norange_options, list_options))
    for key, value in option_map.items():
        if key.lower() == inp.lower():
            return value
    return check_int_input(list_options, inp)


def check_int_input(options: list, inp: str) -> None | str:
    if inp.isdigit():
        index = int(inp)
        if 1 <= index <= len(options):
            return options[index - 1]
    return None


def reset_options():
    while True:
        cls()
        print("Are you sure you wish to reset the in-game options?")
        print("Y/N")
        user_input = input().lower()
        if user_input == "y":
            return config_manager.reset_config()
        if user_input == "n":
            return None
        print('Input was not "Y" or "N".')
        sleep(1)


def write(inp, value) -> None:
    config_manager.write_config(("USER", {inp: value}))
    cls()
    print(f"Successfully changed option {''.join(get_norange_options({inp: '_'}))}.")
    sleep(1)


def range_check(to_check: tuple[str, int], options: dict) -> bool:
    range_dict = option_range(options)
    # to_check[0] is the key to search
    # to_check[1] is the value to see if it's in between
    # range_dict[to_check[0]] gets the tuple of ranges
    # the [0] after that gets the first value in the range.

    return range_dict[to_check[0]][0] <= to_check[1] <= range_dict[to_check[0]][1]


def option_range(options: dict) -> dict[str, tuple[int, int]]:
    option_ranges = [
        (int(value.split(".")[1]), int(value.split(".")[2])) for value in options
    ]
    option_names = options.keys()
    return dict(zip(option_names, option_ranges))

if __name__ == "__main__":
    begin()
