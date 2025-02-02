"""

Code
Testcase
Test Result
Test Result
Q1. Adjacent Increasing Subarrays Detection I
Easy
3 pt.
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false

 

Constraints:

2 <= nums.length <= 100
1 <= 2 * k <= nums.length
-1000 <= nums[i] <= 1000
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int], k: int) -> bool:
        ll = len(nums)

        if k == 1 and ll >= 2:
            return True

        a = 0
        max_increase = 1
        for ii in range(a+1,ll):
            if ll-a < 2*k:
                print(111, ll, k, 2*k, a, ii)
                return False
            if nums[ii] <= nums[ii-1]:
                max_increase = ii-a
                #print(a,ii, max_increase)
                a = ii
                b = ii
                if max_increase >= k*2:
                    return True
                elif max_increase >= k:
                    if ii+k > ll:
                        return False

                    for jj in range(1,k):
                        if nums[b+jj] > nums[b+jj-1]:
                            if jj == k-1:
                                print(444,a,ii,b,jj,k,max_increase)
                                return True
                        else:
                            a = b+jj
                            break


        return True

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
