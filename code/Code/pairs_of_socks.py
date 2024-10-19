# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example

# n=7

# arr=[1,2,1,2,1,3,2]

# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

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
    match=0
    match_arr=[]
    for i in ar:
        if i in match_arr:
            match=match+1
            match_arr.remove(i)
        else:
            match_arr.append(i)
    return(match)

        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
