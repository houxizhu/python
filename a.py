"""
Testing
"""

import string
import heapq
from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int]) -> List[int]:
        ll = len(nums)
        result = 0
        
        for ii, item in enumerate(nums):
            print(ii, item)

        sl = SortedList([item, ii] for ii, item in enumerate(nums))
        print(sl)


        for ii in range(ll):
            pass

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
