#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[3,56,7,8,9])))

def susu(n):
    if n <= 2:
      return True
    for i in range(2,n):
        if n % i == 0:
          return False
        else:
            return True
print(list(filter(susu,range(1,101))))
print(list(range(1,101)))