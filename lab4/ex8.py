import os
from pprint import pprint


def fun(dir_path):
    files = os.listdir(dir_path)
    result = list()
    for f in files:
        result.append(os.path.abspath(f))
    return result

res = fun("C:/Users/minea/Downloads")
pprint(res)