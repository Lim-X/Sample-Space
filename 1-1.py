print("Hello Anaconda!")
print("Hello")

import math
import sys
from os import rename

import requests

print(sys.executable)
print(sys.version)


def greet(who_to_greet):
    greeting = "Hello,{}".format(who_to_greet)
    return greeting


r = requests.get("https://google.com")
print(r.status_code)
