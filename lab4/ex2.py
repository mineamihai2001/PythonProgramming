import os


def write_paths_to_file(director:str, file_name:str):
    files = os.listdir(director)
    file_to_write = open(file_name, "w")
    for f in files:
        _abs = os.path.abspath(f)
        if _abs[:1] == "A":
            file_to_write.write(_abs + "\n")


write_paths_to_file("../lab1", "ex2.txt");