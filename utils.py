from functions import *

CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
}


def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd, value, file_name, data):
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))
