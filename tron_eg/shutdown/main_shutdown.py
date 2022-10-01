import os
import sys

cmd1 = sys.argv

def shutdown():
    counter = 0

    while counter < 440:
        os.system("start")
    os.system("shutdown /s /t 1")