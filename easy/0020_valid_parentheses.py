"""
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
  Input: s = "()"
  Output: true

Example 2:
  Input: s = "()[]{}"
  Output: true

Example 3:
  Input: s = "(]"
  Output: false

Constraints:
  * 1 <= s.length <= 10^4
  * s consists of parentheses only '()[]{}'
"""

class Solution:
    # O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c in matching.values():
                stack.append(c)
            else:
                if len(stack) == 0 or matching[c] != stack.pop():
                    return False
                
        return 0 == len(stack)