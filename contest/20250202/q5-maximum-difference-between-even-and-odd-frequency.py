"""
Q1. Maximum Difference Between Even and Odd Frequency I
Easy
3 pt.
You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:

One of the characters has an even frequency in the string.
The other character has an odd frequency in the string.
Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency.

 

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 

Constraints:

3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, s: str) -> int:
        dd = defaultdict(int)
        maxodd = 0
        maxeven = 0
        minodd = len(s)
        mineven = len(s)
        for each in s:
            dd[each] += 1
        for each in dd:
            if dd[each] % 2 == 0:
                maxeven = max(maxeven, dd[each])
                mineven = min(mineven, dd[each])
            else:
                maxodd = max(maxodd, dd[each])
                minodd = max(minodd, dd[each])

        return maxodd-mineven©leetcode

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
