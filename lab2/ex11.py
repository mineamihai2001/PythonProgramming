def order(tuple_list: list):
    return sorted(tuple_list, key=lambda _tuple: _tuple[1][2])

print(order([('abc', 'bcd'), ('abc', 'zza')]))
