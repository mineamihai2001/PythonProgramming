import os


def extensions(director: str):
    files = os.listdir(director)
    unique_ext = list()
    for f in files:
        filename, file_extension = os.path.splitext(f)
        if file_extension not in unique_ext:
            unique_ext.append(file_extension)
    return unique_ext


print(extensions("C:/Users/minea/Downloads"))
