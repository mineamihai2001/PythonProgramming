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
                    with open(os.path.abspath(_file)) as f:
                        if to_search in f.read():
                            result.append(_file)
                # else: print(_file, "doesn't exist")
            except Exception as e:
                callback(e)
        return result
    else:
        raise ValueError("ValueError exception thrown")

def callback(exception: Exception):
    print("EXCEPTION HERE: ", exception)


res = fun("../lab3", "print", callback)
print(res)