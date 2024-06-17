#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    logo={}
    for i in s:
        if i in logo:
            logo[i]+=1
        else:
            logo[i]=1
    logo=dict(zip(sorted(logo, key=logo.get,reverse=True), reversed(sorted(logo.values()))))
    i=0
    for j,k in logo.items():
        i+=1
        print(j,k)
        if(i==3):
            break
