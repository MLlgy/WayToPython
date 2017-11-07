#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[3,56,7,8,9])))