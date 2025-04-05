import os
from subprocess import Popen
from time import time


def os_module_tips(arg = None):
    print(os.Popen('whoami'))
    print(*os.Popen('whoami'))
    print(Popen("ls -la"))
    print(*Popen("ls"))
    print(*Popen("pwd"))
    print(*Popen("clear"))


# #
# # Create Three Test files
# # Using Cat create files
# ---------------------------
# from os import popen
# print(*popen('pwd'))
# print(*popen("ls -ltr /Users/zayan"))

## Carrage Return
## Line Feed


################
# Files and Path
################

#   File Group


# Stat file meta-data using 100% Python

# from os import popen
# zfile = "./naju.txt"
#
# with open(zfile, "w") as fh:
#     fh.write("hello naju")
#
# with open(zfile) as fh:
#     print(*fh)
#
# print(*popen("stat " + zfile))

#
# from os import stat
#
# import time
#
# # Directory Group

#####
# Subprocess
#####
# from subprocess import Popen
#
# Popen(['mkdir', 'NAJU']).wait()
#
# Popen(['cd', './NAJU'], shell=True).wait()
#
# from os import walk
# var = walk('./Python-Concept')
#

# from subprocess import Popen
# def FindByPopenFind(Zpattern):
#     cmd = Popen(["find", "/", "-type", "-f", "-name", Zpattern])
#     code = cmd.wait()
#     if code == 0:
#         return True
#     return False


# def findByPythonWalk(Zpattern):
#     from os import walk
#     for root, dirs, node in walk('/'):
#         pass
#     return True


# ##
#
#


# for i in range(0,1):
#     st = time()
#     Popen(["ls", "-la"])
#     et = time()
# print("result", et - st, sep='\t')
#
# #

# import os
# help(os.unlink)

#cal
#od

# Compare 2 files



#cut -c 1-3,4-6 filename.txt

# Compare 3 files and get the values
# cal 3 > filename.txt
# root = "filename.txt"
# from subprocess import Popen

# print('Code:', Popen(["cal", "-3", ">", root], shell=True).wait())

# with open(root) as fh:
#     for line in fh:
#         print(line)
#         print(line[14:17], line[36:39], line[58:62])

print(os_module_tips())