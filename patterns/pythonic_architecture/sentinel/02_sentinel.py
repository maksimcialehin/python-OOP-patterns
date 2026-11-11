_SENTINEL = object()
NOT_FOUND = object()


database = {
    101: 'Нейрочип 3.0',
    102: None,
}


def get_cyberchip(user_id, default=_SENTINEL):
    chip = database.get(user_id)
    if chip is None:
        if default is _SENTINEL:
            return NOT_FOUND
        return default
    return chip


print(get_cyberchip(101))
print(NOT_FOUND)
