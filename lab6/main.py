import os
import re


def function_1(text):
    return re.findall("[a-z0-9]+", text, flags=re.IGNORECASE)


def function_2(r, text, x):
    return list(filter(lambda el: len(el) == x, re.findall(r, text)))


def function_3(text_chars, list_of_re):
    return [el for el in text_chars if any([re.search(r, el) for r in list_of_re])]


def function_6(s):
    low_s = s.lower()
    if not (low_s[0] in "aeiou" and low_s[-1] in "aeiou"):
        return s
    return "".join([ch if idx % 2 == 0 else '*' for idx, ch in enumerate(s)])

def function_7(string):
    return re.match(r"[1256]\d\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{6}$", string) != None


def function_8(directory, reg):
    result = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            file_name = os.path.join(root, f)
            r = re.search(reg, f)
            if r:
                result += [f]
            try:
                with open(file_name, "r") as f_d:
                    string = f_d.read()
                    if (re.search(reg, string)):
                        if r:
                            result[-1] = ">>" + result[-1]
                        else:
                            result += [f]
            except:
                pass
    return result


if __name__ == "__main__":
    print("FUNCTION 1 => ", function_1("wordhere"), function_1("####%#$%"), "\n")
    print("FUNCTION 2 => ", function_2(r"ab", "abcababxaxb", 2), "\n")
    print("FUNCTION 3 => ", function_3(["test", "testing", "fsdjkaing", "rrrrr"], [r"test", r"ing"]), "\n")
    print("FUNCTION 6 => ", function_6("atestingi"), "\n")
    print("FUNCTION 7 =>", function_7("5011106221135"), function_7("1234"), "\n")
    print("FUNCTION 8 => ", function_8("../lab4", r"ex"), "\n")