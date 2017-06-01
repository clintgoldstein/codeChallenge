#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:05:10 2017

@author: clintongoldstein
"""

print("input cipher")


cypher = [int(x) for x in input().split(',')]
print (cypher)

print("input book")
buffer =input()
l_buffer =list(buffer) 

message=""


for x in cypher:
    message+=l_buffer[x]
    
print (message)