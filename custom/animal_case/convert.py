# https://github.com/rafa-acioly/animal_case
import re


def _unpack(data):
    if isinstance(data, dict):
        return data.items()
    return data


def to_snake_case(value):
    """
    Convert camel case string to snake case
    :param value: string
    :return: string
    """
    first_underscore = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', first_underscore).lower()


def keys_to_snake_case(content):
    """
    Convert all keys for given dict to snake case
    :param content: dict
    :return: dict
    """
    return {to_snake_case(key): value for key, value in _unpack(dict(content))}


def to_camel_case(value):
    """
    Convert the given string to camel case
    :param value: string
    :return: string
    """
    content = value.split('_')
    return content[0] + ''.join(word.title() for word in content[1:] if not word.isspace())


def keys_to_camel_case(content):
    """
    Convert all keys for given dict to camel case
    :param content: dict
    :return: dict
    """
    print(content)
    return {
        to_camel_case(key): value for key, value in _unpack(dict(content))
    }


def parse_keys(data=None, types='snake'):
    """
    Convert all keys for given dict/list to snake case recursively
    the main type are 'snake' and 'camel'
    :param data: dict
    :return: dict

    """
    if types not in ('snake', 'camel'):
        raise ValueError("Invalid parse type, use snake or camel")

    if type(data) == list:
        formatted = []
    elif type(data) == dict:
        formatted = {}
    else:
        raise ValueError("Invalid data type, use list or dict")

    formatter = keys_to_snake_case if types == 'snake' else keys_to_camel_case

    if type(data) == dict:
        for key, value in _unpack(formatter(data)):
            if isinstance(value, dict):
                formatted[key] = parse_keys(value, types)
            elif isinstance(value, list) and len(value) > 0:
                formatted[key] = []
                for _, val in enumerate(value):
                    formatted[key].append(parse_keys(val, types))
            else:
                formatted[key] = value
        return formatted

    else:
        for key, value in enumerate(formatter(data)):
            if isinstance(value, dict):
                formatted[key] = parse_keys(value, types)
            elif isinstance(value, list) and len(value) > 0:
                formatted[key] = []
                for _, val in enumerate(value):
                    formatted[key].append(parse_keys(val, types))
            else:
                formatted.append(value)
        return formatted
