import os


def fun(target:str, to_search:str):
    if os.path.isfile(target):
        with open(target) as f:
            if to_search in f.read():
                return target
    elif os.path.isdir(target):
        files = os.listdir(target)
        result = list()
        for _file in files:
            if os.path.exists(_file):
                with open(os.path.abspath(_file)) as f:
                    if to_search in f.read():
                        result.append(_file)
            else: print(_file, "doesn't exist")
        return result
    else:
        raise ValueError("ValueError exception thrown")


res = fun("../lab3/test", "print")
print(res)