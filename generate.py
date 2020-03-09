#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

from xeger import Xeger

ADD_SUB = "(?:-|\\+)"
ITEM_FIRST = '(?:(?:-|\\+)?(?:(?:(?:-|\\+)?(?:[0-9]){1,2})|(?:(?:x|(?:sin|cos)\\(x\\))(?:\\*\\*(?:(?:-|\\+)?(?:[0-9]){1,2}))?)))'
ITEM_LATER = '(?:\\*(?:(?:(?:-|\\+)?(?:[0-9]{1,2}))|(?:(?:x|(?:sin|cos)\\(x\\))(?:\\*\\*(?:(?:-|\\+)?(?:[0-9]{1,2})))?)))'
ITEM = "(?:" + ITEM_FIRST + ITEM_LATER + "*)"
EXPRESSION_FIRST = "(?:" + ADD_SUB + "?" + ITEM + ")"
EXPRESSION_LATER = "(?:" + ADD_SUB + ITEM + ")"
x = Xeger(limit=7)
expression = x.xeger(EXPRESSION_FIRST)
for j in range(1, random.randint(1, 8)):
    expression += x.xeger(EXPRESSION_LATER)
print(expression)
