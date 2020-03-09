#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sympy import sympify, diff
from sympy.abc import x
import re

s = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", input())
expr = sympify(s)
expr_diff = diff(expr, x)
for i in range(-9, 10):
    print(expr_diff.evalf(subs={x:i}))