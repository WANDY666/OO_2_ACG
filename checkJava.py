#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sympy import sympify, pprint
from sympy.abc import x

expr = sympify(input())
for i in range(-9, 10):
    print(expr.evalf(subs={x:i}))


