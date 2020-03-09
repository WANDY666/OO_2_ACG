import math
import sys

with open("javaout.txt") as java:
    javaAns = java.readlines()
with open("stout.txt") as std:
    Ans = std.readlines()
sign = False
for i in range (0, min(len(javaAns), len(Ans))):
    if not math.isclose(float(Ans[i]), float(javaAns[i])) :
        if sign:
            sys.exit(1)
        else:
            sign=True
sys.exit(0)