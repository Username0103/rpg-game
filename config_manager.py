"""gets configuration values"""

# pylint: disable=C0116

import configparser
import os

config_parser = configparser.ConfigParser()


def _get_path(file: str = "config.ini") -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, file)
    return config_file_path


def _read_config() -> configparser.ConfigParser:
    config_file_path = _get_path()
    config_parser.read(config_file_path)
    return config_parser


def reset_config() -> None:
    defaults_path = _get_path("config_defaults.ini")
    working_path = _get_path()
    with open(defaults_path, encoding="utf_8") as defaults:
        with open(working_path, "w", encoding="utf_8") as config_file:
            config_file.write(defaults.read())


def _check_presence(to_check: tuple[str, dict]) -> bool:
    try:
        for string in to_check[1].keys():
            get_config((to_check[0], string))
    except configparser.NoOptionError:
        return False
    except configparser.NoSectionError as exc:
        raise KeyError(
            "received wrong section to write_config()," f"was {to_check[0]}"
        ) from exc
    return True


def write_config(to_write: tuple[str, dict]) -> None:
    if _check_presence(to_write) is False:
        raise KeyError("Tried to write config to non-existing configuration!")
    config_parser[to_write[0]].update(to_write[1])
    with open(_get_path(), "w", encoding="utf_8") as config_file:
        config_parser.write(config_file)


def get_dict_section(section) -> dict[str, str]:
    config = _read_config()
    return dict(config[section])


def get_config(to_get: tuple[str, str]) -> str:
    config = _read_config()
    result = config.get(to_get[0], to_get[1])
    return result


if __name__ == "__main__":
    print(_check_presence(("USER", {"temp5": 0})))
