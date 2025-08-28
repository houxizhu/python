"""
2710. Remove Trailing Zeros From a String
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

 

Example 1:

Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
Example 2:

Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".
 

Constraints:

1 <= num.length <= 1000
num consists of only digits.
num doesn't have any leading zeros.
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, num: str) -> str:
        ll = len(num)
        for ii in range(ll-1,-1,-1):
            if num[ii] != "0":
                return num[0:ii+1]
        return num


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
