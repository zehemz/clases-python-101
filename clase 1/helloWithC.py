import sys
import datetime
try:
    from ctypes import *
except ImportError:
    print("ERROR")
    sys.exit(-1)

a = datetime.datetime.now()
	
cdll.LoadLibrary("./helloLib.so").executeWork()

b = datetime.datetime.now()
print(b-a)

