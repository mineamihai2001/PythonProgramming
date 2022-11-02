import os


def fun(my_path:str):
    type = "file" if os.path.isfile(my_path) else "dir"
    if type == "file":
        f = open(my_path, "r")
        return f.read()[-20:]
    else:
        files = os.listdir(my_path)
        result = {}
        for f in files:
            file_name, file_extension = os.path.splitext(f)
            result[file_extension] = result[file_extension] + 1 if file_extension in result else 1
        return [(key, value) for key, value in result.items()]  


# result = fun("./ex2.txt")
result = fun("C:/Users/minea/Downloads")
print(result)