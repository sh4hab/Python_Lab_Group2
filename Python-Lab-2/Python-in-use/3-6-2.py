import re

#finding cept
with open("GPL-1") as file:
    m = file.read()
    for word in m.split():
        if re.findall("cept",word):
            print(word)