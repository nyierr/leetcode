"""
You are climbing a staircase. It takes n steps to reach
the top.

Each time you can either climb 1 or 2 steps. In how many
distinct ways can you climb to the top?

Example 1:
  Input: n = 2
  Output: 2
  Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
  Input: n = 3
  Output: 3
  Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step 

Constraints:
  * 1 <= n <= 45
"""

class Solution:          
    # O(2^n) solution, pure recursion (time limit exceeded)
    # O(2^n) because we double the number of nodes in the
    # recursion tree every time we increase n
    #def climbStairs(self, n: int) -> int:
    #    if n < 0:
    #        return 0
    #    elif n == 0:
    #        return 1
    #    
    #    return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    # O(n) solution using memoization
    # O(n) -> in fact O(2n+1) because if we increase
    # n by 1, we add only 2 extra nodes in the recursion tree
    #def climbStairs(self, n: int) -> int:
    #    return self.find(n, {})
    #
    #def find(self, n, d={}):
    #    if n in d:
    #        return d[n]
    #    
    #    if n < 0:
    #        return 0
    #    elif n == 0:
    #        return 1
    #    
    #    d[n] = self.find(n-1, d) + self.find(n-2, d)
    #    
    #    return d[n]
    
    # O(n) solution, dynamic programming
    # f(n) is f(n-1) + f(n-2) -> so if we start
    # "collecting" results from f(1) and f(2) up to
    # n, we will get the number of distinct ways for n
    def climbStairs(self, n: int) -> int:
        r = [0, 1, 1] + (n - 1) * [0]
        
        for i in range(1, n):
            r[i+1] += r[i]
            r[i+2] += r[i]
            
        return r[n]