"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing
x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = 120
    Output: 21

Example 4:
    Input: x = 0
    Output: 0
 
Constraints:
    -2^31 <= x <= 2^31 - 1
"""
class Solution:
    # First draft, not fully correct because the overflow check
    # happens to late. Complexity is O(n) because of the for-loop
    #def reverse(self, x: int) -> int:
    #    neg = -1 if x < 0 else 1
        
    #    x = abs(x)
    #    digits = []
    #    while(x > 0):
    #        digits.append(x % 10)
    #        x = x // 10
                
    #    for i in range(0, len(digits)):
    #        x += digits[i] * pow(10, len(digits) - 1 - i)
        
    #    x *= neg
    #    return x if (x >= pow(-2, 31)) and x < pow(2, 31) else 0 
    # Complexity O(log(n))
    def reverse(self, x: int) -> int:
        INT_MAX = pow(2, 31) - 1
        
        neg = 1 if x > 0 else -1
        # Get the last digit to check for overflow
        limit = INT_MAX % 10 if x > 0 else 1 + INT_MAX % 10
    
        x = abs(x)

        reversed = 0
        while(x > 0):
            digit = x % 10
            x = x // 10
            if (reversed > INT_MAX // 10) or (reversed == INT_MAX and digit > limit):
                return 0
            reversed = digit + reversed * 10
            
        return reversed * neg
