import os
import sys


def list_extensions():
    director = sys.argv[1]
    files = os.listdir(director)
    ext = list()
    for f in files:
        file_name, file_ext = os.path.splitext(f)
        if file_ext not in ext and file_ext != '':
            ext.append(file_ext)
    return sorted(ext)


print(list_extensions())
