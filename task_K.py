import numpy as np

a = int(input())
b = int(input())
c = int(input())

if a+b >c and a+c >b and  b+c >a:
    if a**2 + b**2  > c**2:
        print("acute")
    elif a**2 + b**2 < c**2:
        print("obtuse")
    else:
        print("rectangular")
else:
    print("does not exist")
