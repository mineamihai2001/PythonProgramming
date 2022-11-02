import os
from pprint import pprint
from stat import *


def file_details(file_name: str):
    details = os.stat(file_name)
    file_name, file_extension = os.path.splitext(file_name)
    abs_path = os.path.abspath(file_name)
    mode = details.st_mode

    return {
        "full_path": abs_path,
        "file_extension": file_extension,
        "file_size": details.st_size,
        "file_permissions": filemode(mode)
    }

details = file_details("./ex3.py")
pprint(details)