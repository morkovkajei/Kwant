import numpy as np
 
 
def define(box1, box2):
    b1s = np.array(box1)
    b1s.sort()
    b2s = np.array(box2)
    b2s.sort()
 
    if np.all(b1s==b2s):
        return "equal"
    elif np.all(b1s>=b2s):
        return "box1 bigger"
    elif np.all(b1s<=b2s):
        return "box2 bigger"
    else:
        return "incomparable"
