"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:

Example 1:
  Input: numRows = 5
  Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
Example 2:
  Input: numRows = 1
  Output: [[1]]

Constraints:
  * 1 <= numRows <= 30
"""

class Solution:
    # O(n^2) solution, iterative
    #def generate(self, numRows: int) -> List[List[int]]:        
    #    out = [[1]]
    #    for i in range(numRows - 1):
    #        prev = out[-1]
    #        curr = [prev[0]]
    #        
    #        for j in range(1, len(prev)):
    #            curr.insert(j, prev[j] + prev[j-1])
    #        
    #        curr.append(prev[-1])
    #        out.append(curr)
    #        
    #    return out

    # O(n^2) solution, recursive
    def generate(self, numRows: int) -> List[List[int]]:        
        if numRows == 1:
            return [[1]]
        
        res = self.generate(numRows - 1)
        
        prev = res[-1]
        curr = [prev[0]]
        for i in range(1, len(prev)):
            curr.insert(i, prev[i] + prev[i-1])
        curr.append(prev[-1])
        
        return res + [curr]
        