#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:29:17 2017

@author: clintongoldstein
"""

buffer =input()
l_buffer =list(buffer) 

action= [0]*len(l_buffer)

total=2017

for i in range(0, (len(l_buffer))):
    if l_buffer[i] == '*':
        action[i]=1
    if l_buffer[i] == '#':
        action[i]=-1
    if l_buffer[i] == '<':
        if l_buffer[i-2] == '<':
            action[i]=(action[(i-2)]*2)
        else:
            action[i]=(action[(i-2)])

print(action)
      
for j in range(0, len(action)):
    total+=action[j]
        
print(total)