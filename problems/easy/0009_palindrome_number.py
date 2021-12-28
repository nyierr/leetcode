"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:
  Input: x = 121
  Output: true

Example 2:
  Input: x = -121
  Output: false
  Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
  Input: x = 10
  Output: false
  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
  Input: x = -101
  Output: false
 
Constraints:
  -2^31 <= x <= 2^31 - 1
"""
class Solution:
    # First approach, complexity O(n) and using string conversion
    #def isPalindrome(self, x: int) -> bool:
    #    x = str(x)
    #    return x == x[::-1] 
    
    # Enough to revers half of digits and compare them
    # to the other half. Complexity log(x)
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
    
        if x >= 0 and x < 10:
            return True
        
        p = 0
        while x > 0:
            p = (10 * p) + x % 10
            if (p == x) or (p == x // 10):
                return True
            x = x // 10
        
        return False   
