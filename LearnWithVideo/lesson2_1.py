#!/usr/bin/python3
import string 

a = ''
if a is None:
    print("None")
else:
    print('empty') 

S=['2','3','5']
print('-'.join(S))
s=['jj']
print(S + s)

S.extend(s)
print(S)

S.append('hoo')
print(S)

print(str(S.insert(0,'35353')))

print(S.pop())

del S[0]
print(S)
