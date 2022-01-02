"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
  Input: a = "11", b = "1"
  Output: "100"

Example 2:
  Input: a = "1010", b = "1011"
  Output: "10101" 

Constraints:
  * 1 <= a.length, b.length <= 10^4
  * a and b consist only of '0' or '1' characters
  * Each string does not contain leading zeros except for the zero itself
"""

class Solution:   
    # O(n+m) solution using built-in conversion functions
    #def addBinary(self, a: str, b: str) -> str:
    #    return bin(int(a, 2) + int(b, 2))[2:]
        
    # O(n+m) solution, convert both strings to array-form
    #def addBinary(self, a: str, b: str) -> str:
    #    a = self.to_list(a)
    #    b = self.to_list(b)
        
    #    i = len(a) - 1
    #    j = len(b) - 1
        
    #    co = 0
    #    while i > -1 and j > -1:
    #        x = a[i] + b[j] + co
    #        if x > 1:
    #            x = x - 2
    #            co = 1
    #        else:
    #            co = 0
    #        
    #        a[i] = x            
    #        i -= 1
    #        j -= 1
    #        
    #    # a is longer
    #    while i > -1:
    #        x = a[i] + co
    #        if x > 1:
    #            x = 0
    #            co = 1
    #        else:
    #            co = 0
    #        
    #        a[i] = x
    #        i -= 1
    #
    #    # b is longer
    #    while j > -1:
    #        x = b[j] + co
    #        if x > 1:
    #            x = 0
    #            co = 1
    #        else:
    #            co = 0
    #            
    #        a.insert(0, x)
    #        j -= 1
    #
    #    if co > 0:
    #        a.insert(0, co)
    # 
    #    return self.to_string(a)
    #    
    #def to_list(self, s):
    #    l = []
    #    for x in s:
    #        l.append(int(x))
    #    return l
    # 
    #def to_string(self, l):
    #    s = ""
    #    for x in l:
    #        s += str(x)
    #    return s
    
    # O(n+m) solution with manual conversion
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        
        a = self.binToDecimal(a)
        b = self.binToDecimal(b)
        
        s = a + b
        
        bs = ""
        while s > 0:
            bs = str(s % 2) + bs
            s = s // 2
            
        return bs
        
    def binToDecimal(self, bs):
        num = 0
        for c in bs:
            num = num * 2
            if c == "1":
                num += 1
                
        return num