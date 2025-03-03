"""

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
    def leetcode(self, text: str, first: str, second: str) -> List[str]:
        result = []
        ltext = text.split(" ")
        ll = len(ltext)
        for ii in range(2,ll):
            if ltext[ii-2] == first and ltext[ii-1] == second:
                result.append(ltext[ii])

        return result



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
