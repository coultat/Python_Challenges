async def calc_binary(value):

    if value < 2:
        return str(value)

    acum = str(value % 2)
    value = int(value / 2)

    return await calc_binary(value) + acum
