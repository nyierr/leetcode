"""
Given a string s consisting of some words separated by some
number of spaces, return the length of the last word in
the string.

A word is a maximal substring consisting of non-space
characters only.

Example 1:
  Input: s = "Hello World"
  Output: 5
  Explanation: The last word is "World" with length 5.

Example 2:
  Input: s = "   fly me   to   the moon  "
  Output: 4
  Explanation: The last word is "moon" with length 4.

Example 3:
  Input: s = "luffy is still joyboy"
  Output: 6
  Explanation: The last word is "joyboy" with length 6.

Constraints:
  * 1 <= s.length <= 10^4
  * s consists of only English letters and spaces ' '
  * There will be at least one word in s
"""

class Solution:   
    # O(n) approach, we are starting from the beginning
    #def lengthOfLastWord(self, s: str) -> int:
    #    word = ""
    #    for i in range(len(s)):
    #        if word != "" and s[i-1] == " " and s[i] != " ":
    #            word = ""
    #            
    #        if s[i] != " ":
    #            word += s[i]
    #            
    #    return len(word)
    
    # O(n) approach, start from the end
    # it will be O(n) if the string consist of a single word
    # (with or without spaces at the end)
    # otherwise it will be O(k) where k = length of last word
    # + the number of space after the last word
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                c += 1
            
            if c > 0 and s[i] == " ":
                break
                
        return c