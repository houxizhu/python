"""
773. Sliding Puzzle
Solved
Hard
Topics
Companies
Hint
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:


Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:


Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
 

Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
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
    def leetcode(self, board: List[List[int]]) -> int:
        # Convert board to tuple for easy comparison
        start = tuple(board[0] + board[1])
        target = (1, 2, 3, 4, 5, 0)
        
        # Mapping of moves based on position of 0
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS setup
        queue = deque([(start, start.index(0), 0)])  # (state, index of 0, steps)
        visited = set()
        visited.add(start)
        
        while queue:
            state, zero_idx, steps = queue.popleft()
            
            # Check if we've reached the target
            if state == target:
                return steps
            
            # Try all possible moves
            for move in moves[zero_idx]:
                new_state = list(state)
                # Swap 0 with the adjacent number
                new_state[zero_idx], new_state[move] = new_state[move], new_state[zero_idx]
                new_state_tuple = tuple(new_state)
                
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    queue.append((new_state_tuple, move, steps + 1))
        
        # If we exit the loop without finding the solution
        return -1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
