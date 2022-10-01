import sys
import py_compile



comm = "&& gcc main.c ./main && g++ main_.cpp ./main_"

py_compile.compile(f"main_shutdown.py {comm}")