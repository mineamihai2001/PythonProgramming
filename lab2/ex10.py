def func(*lists):
    result = list()
    max_len = -1
    for _list in lists:
        max_len = len(_list) if len(_list) > max_len else max_len
    for index in range(max_len):
        _tuple = list()
        for _list in lists:    
            try:
                _tuple.append(_list[index])
            except:
                _tuple.append(None)
        result.append(tuple(_tuple))
    return result

print(func([1,2,3], [5,6,7], ["a", "b", "c"]))
