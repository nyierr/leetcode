"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
  Input: strs = ["flower","flow","flight"]
  Output: "fl"

Example 2:
  Input: strs = ["dog","racecar","car"]
  Output: ""
  Explanation: There is no common prefix among the input strings. 

Constraints:
  * 1 <= strs.length <= 200
  * 0 <= strs[i].length <= 200
  * strs[i] consists of only lower-case English letters.
"""

class Solution:
    # O(S) where S is the total number of characters    
    #def longestCommonPrefix(self, strs: List[str]) -> str: 
    #    prefix = strs[0]
    #    
    #    for s in strs[1:]:
    #        if len(prefix) == 0 or len(s) == 0:
    #            prefix = ""
    #            break
                
    #        no_change = True
    #        max_i = min(len(s), len(prefix))
            
    #        for i in range(max_i):
    #            if s[i] != prefix[i]:
    #                prefix = prefix[:i]
    #                no_change = False
    #                break
                    
    #        if no_change and i == len(s) - 1:
    #            prefix = s[:i+1]
                
    #    return prefix
    
    # O(S) where S is the total number of characters
    # Similar to the previous one but using recursion
    #def longestCommonPrefix(self, strs: List[str]) -> str: 
    #    if len(strs) == 1:
    #        return strs[0]
        
    #    mid = len(strs) // 2
    #    prefix = self.longestCommonPrefix(strs[:mid])
    #    check = self.longestCommonPrefix(strs[mid:])
        
    #    if prefix == "" or check == "":
    #        return ""
        
    #    matched = True
    #    max_i = min(len(prefix), len(check))
    #    for i in range(max_i):
    #        if prefix[i] != check[i]:
    #            prefix = prefix[:i]
    #            matched = False
    #            break
                
    #    if matched and i == len(check) - 1:
    #        prefix = check[:i+1]
    #        
    #    return prefix

    # O(S*log m) Binary-search-like approach
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        r = len(strs[0])
        for s in strs[1:]:
            r = min(r, len(s))

        l = 1
        while l <= r:
            mid = (l + r) // 2
            if self.isShared(strs, mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return strs[0][:(l+r) // 2]
            
    def isShared(self, strs, mid):
        prefix = strs[0][:mid]
        for s in strs[1:]:
            if prefix != s[:mid]:
                return False
        return True