import os

def file_exist(filename):
    for file in os.listdir("."):
        if file.startswith(filename):
            return(f"found {filename}")
        return -1
print(file_exist("scribe.py"))
