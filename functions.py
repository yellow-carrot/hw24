def filter_query(value, data):
    return filter(lambda x: value in x, data)


def limit_query(value, data):
    limit = int(value)
    return list(data)[:limit]


def map_query(value, data):
    column = int(value)
    return map(lambda x: x.split(' ')[column], data)


def sort_query(value, data):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def unique_query(data, *args, **kwargs):
    return set(data)
