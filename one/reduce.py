#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
from functools import reduce
def add(x,y):
    return x + y
print(reduce(add,[2,5,76,7]))

def fn(x,y):
    return x * 10 +y
def char2num(s):
    return{
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9
    }[s]
print(list(map(char2num,'3536436')))
print(reduce(fn,map(char2num,'3536436')))

def str2int(s):
    def fn(x,y):
        return x * 10 +y
    def char2num(s):
        return{
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }[s]
    return reduce(fn,map(char2num,s))
print(str2int("3535"))

def change(name):
    return name.capitalize()
print(list(map(change,['dfegfe','dfdfd'])))

def change2(name):
    return name[:1].upper()+name[1:].lower()
print(list(map(change2,['dfegfe','dfdfd'])))

def prod(L):
    def fx(x,y):
        return x * y
    return reduce(fx,L)
print(prod([3,5,6]))
