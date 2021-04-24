#!/usr/bin/python3
# -*- Coding: utf-8 -*-
import sys
import json

lines = sys.stdin.readlines()
ret=[]
keys=[]
for i,l in enumerate(lines):
    if i==0:
        keys=[_i.strip() for _i in l.split('|')]
    elif i==1: continue
    else:
        if l[0] == "|":
            ret.append({keys[_i]:v.strip() for _i,v in enumerate(l.split('|')) if  _i>0 and _i<len(keys)-1})
        else:
            ret.append({keys[_i]:v.strip() for _i,v in enumerate(l.split('|')) if  _i>=0 and _i<=len(keys)-1})
print(json.dumps(ret, indent = 4))
