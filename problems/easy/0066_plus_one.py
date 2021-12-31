"""
You are given a large integer represented as an integer
array digits, where each digits[i] is the ith digit of
the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting
array of digits.

Example 1:
  Input: digits = [1,2,3]
  Output: [1,2,4]
  Explanation: The array represents the integer 123.
  Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].

Example 2:
  Input: digits = [4,3,2,1]
  Output: [4,3,2,2]
  Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].

Example 3:
  Input: digits = [9]
  Output: [1,0]
  Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].

Constraints:
  * 1 <= digits.length <= 100
  * 0 <= digits[i] <= 9
  * digits does not contain any leading 0's.
"""

class Solution:   
    # O(n), convert from array to a number
    #def plusOne(self, digits: List[int]) -> List[int]:
    #    num = digits[0]
    #    for i in range(1, len(digits)):
    #        num = (num * 10) + digits[i]
    #        
    #    num += 1
    #    
    #    digits = []
    #    while num > 0:
    #        digits.insert(0, num % 10)
    #        num = num // 10
    #        
    #    return digits
    
    # O(n) approach, stick to array representation
    def plusOne(self, digits: List[int]) -> List[int]:
        x = digits[-1] + 1
        co = x // 10
        digits[-1] = x - 10 * co
        
        i = len(digits) - 2
        while co == 1 and i >= 0:
            x = digits[i] + co
            co = x // 10
            digits[i] = x - 10 * co
            i -= 1
            
        if i < 0 and co == 1:
            digits.insert(0, 1)
            
        return digits
    