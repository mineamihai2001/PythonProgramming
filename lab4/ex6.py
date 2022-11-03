import os


def fun(target:str, to_search:str, callback):
    if os.path.isfile(target):
        with open(target) as f:
            if to_search in f.read():
                return f
    elif os.path.isdir(target):
        files = os.listdir(target)
        result = list()
        for _file in files:
            try:
                # if os.path.exists(_file):
                    cale = os.path.join(target, _file)
                    with open(cale) as f:
                        if to_search in f.read():
                            result.append(_file)
                # else: print(_file, "doesn't exist")
            except Exception as e:
                callback(e)
        return result
    else:
        callback(ValueError)

def callback(exception: Exception):
    print("EXCEPTION HERE: ", exception)


res = fun("../lab2", "print", callback)
print(res)