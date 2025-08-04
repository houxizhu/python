"""
Q1. Find Special Substring of Length K
Easy
3 pt.
You are given a string s and an integer k.

Determine if there exists a substring of length exactly k in s that satisfies the following conditions:

The substring consists of only one distinct character (e.g., "aaa" or "bbb").
If there is a character immediately before the substring, it must be different from the character in the substring.
If there is a character immediately after the substring, it must also be different from the character in the substring.
Return true if such a substring exists. Otherwise, return false.

A substring is a contiguous non-empty sequence of characters within a string.
 

Example 1:

Input: s = "aaabaaa", k = 3

Output: true

Explanation:

The substring s[4..6] == "aaa" satisfies the conditions.

It has a length of 3.
All characters are the same.
The character before "aaa" is 'b', which is different from 'a'.
There is no character after "aaa".
Example 2:

Input: s = "abc", k = 2

Output: false

Explanation:

There is no substring of length 2 that consists of one distinct character and satisfies the conditions.

 

Constraints:

1 <= k <= s.length <= 100
s consists of lowercase English letters only.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(s)
        s = "0"+s+"0"
        count = 0
        for ii in range(1,ll+2):
            if s[ii] == s[ii-1]:
                count += 1
            else:
                if count == k:
                    return True
                count = 1

        return False

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
