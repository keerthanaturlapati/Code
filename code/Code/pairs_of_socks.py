#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    dict_1={}
    for i in ar:
        if i in dict_1:
            dict_1.update({i:dict_1[i]+1})
        else:
            dict_1[i]=1
        print(dict_1)
        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    print(n)

    ar = list(map(int, input().rstrip().split()))
    print(ar)

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
