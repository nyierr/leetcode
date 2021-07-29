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
    # First approach, complexity O(n)
    #def isPalindrome(self, x: int) -> bool:
    #    x = str(x)
    #    return x == x[::-1] 
    # Enough to revers half of digits and compare them
    # to the other half. Complexity log(x)
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False

        reversed = 0
        while(x > reversed):
            reversed = reversed * 10 + x % 10
            x = x // 10
        
        # reversed // 10 -> for numbers with odd number of digits
        return (x == reversed) or (x == reversed // 10)
