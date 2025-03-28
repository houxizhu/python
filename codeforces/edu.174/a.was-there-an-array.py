# -*- coding: utf-8 -*-

"""
A. Was there an Array?
time limit per test2 seconds
memory limit per test512 megabytes
For an array of integers a1,a2,…,an
, we define its equality characteristic as the array b2,b3,…,bn−1
, where bi=1
 if the i
-th element of the array a
 is equal to both of its neighbors, and bi=0
 if the i
-th element of the array a
 is not equal to at least one of its neighbors.

For example, for the array [1,2,2,2,3,3,4,4,4,4]
, the equality characteristic will be [0,1,0,0,0,0,1,1]
.

You are given the array b2,b3,…,bn−1
. Your task is to determine whether there exists such an array a
 for which the given array is the equality characteristic.

Input
The first line contains one integer t
 (1≤t≤1000
) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer n
 (3≤n≤100
);
the second line contains n−2
 integers b2,b3,…,bn−1
 (0≤bi≤1
).
Output
For each test case, output YES if the array a
 exists, or NO if such an array does not exist. Each letter can be printed in any case.

Example
InputCopy
3
10
0 1 0 0 0 0 1 1
3
1
10
0 1 0 1 1 0 0 1
OutputCopy
YES
YES
NO
Note
In the first example, the array a=[1,2,2,2,3,3,4,4,4,4]
 is suitable.

In the second example, the array a=[7,7,7]
 is suitable.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, arr: list):
    ll = len(arr)
    if ll < 3:
        return "yes"
    for ii in range(1,ll-1):
        if arr[ii] == 0 and arr[ii-1] == 1 and arr[ii+1] == 1:
            return "no"
    return "yes"
    
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(codeforces(n,arr))