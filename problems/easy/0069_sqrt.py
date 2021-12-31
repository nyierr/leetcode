"""
Given a non-negative integer x, compute and return the
square root of x.

Since the return type is an integer, the decimal digits
are truncated, and only the integer part of the result
is returned.

Note: You are not allowed to use any built-in exponent
function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
  Input: x = 4
  Output: 2

Example 2:
  Input: x = 8
  Output: 2
  Explanation: The square root of 8 is 2.82842..., and
  since the decimal part is truncated, 2 is returned. 

Constraints:
  * 0 <= x <= 2^31 - 1
"""

class Solution:   
    # O(log n) solution using Newton's algorithm
    #def mySqrt(self, x: int) -> int:
    #    ap = x
    #    
    #    while abs(x - ap * ap) >= 1:
    #        ap = (ap + (x / ap)) / 2
    #
    #    return int(ap)
    
    # O(log n) solution
    def mySqrt(self, x: int) -> int:
        half = x // 2
        
        while half * half > x:
            half = half // 2
            
        if half * half == x:
            return half
                
        while half * half < x: 
            half += 1
            
        if half * half == x:
            return half
        
        return half - 1    