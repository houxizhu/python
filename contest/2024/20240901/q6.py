"""
3275. K-th Nearest Obstacle Queries
Attempted
Medium
Companies
Hint
There is an infinite 2D plane.

You are given a positive integer k. You are also given a 2D array queries, which contains the following queries:

queries[i] = [x, y]: Build an obstacle at coordinate (x, y) in the plane. It is guaranteed that there is no obstacle at this coordinate when this query is made.
After each query, you need to find the distance of the kth nearest obstacle from the origin.

Return an integer array results where results[i] denotes the kth nearest obstacle after query i, or results[i] == -1 if there are less than k obstacles.

Note that initially there are no obstacles anywhere.

The distance of an obstacle at coordinate (x, y) from the origin is given by |x| + |y|.



Example 1:

Input: queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2

Output: [-1,7,5,3]

Explanation:

Initially, there are 0 obstacles.
After queries[0], there are less than 2 obstacles.
After queries[1], there are obstacles at distances 3 and 7.
After queries[2], there are obstacles at distances 3, 5, and 7.
After queries[3], there are obstacles at distances 3, 3, 5, and 7.
Example 2:

Input: queries = [[5,5],[4,4],[3,3]], k = 1

Output: [10,8,6]

Explanation:

After queries[0], there is an obstacle at distance 10.
After queries[1], there are obstacles at distances 8 and 10.
After queries[2], there are obstacles at distances 6, 8, and 10.


Constraints:

1 <= queries.length <= 2 * 105
All queries[i] are unique.
-109 <= queries[i][0], queries[i][1] <= 109
1 <= k <= 105
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
    def leetcode(self, queries: List[List[int]], k: int) -> List[int]:
        ### time exceeded
        a = queries
        ll = len(a)
        d = [abs(x)+abs(y) for x,y in a]
        #print(d)

        result = [-1] * ll

        for ii in range(ll):
            for jj in range(ii-1,-1,-1):
                if d[jj] <= d[jj+1]:
                    break
                d[jj],d[jj+1] = d[jj+1],d[jj]
            #print(d,result)
            if ii >= k-1:
                result[ii] = d[k-1]
            #print(d,result)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
