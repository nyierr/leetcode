"""
Given the root of a binary tree, check whether it is a mirror of
itself (i.e., symmetric around its center).

Example 1:
  Input: root = [1,2,2,3,4,4,3]
  Output: true
    
Example 2:
  Input: root = [1,2,2,null,3,null,3]
  Output: false

Constraints:
  * The number of nodes in the tree is in the range [1, 1000]
  * -100 <= Node.val <= 100
"""

class Solution:          
    # O(2^n) solution, iterative
    #def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #    if root.left is None and root.right is None:
    #        return True
    #    
    #    left_stack = [root.left]
    #    right_stack = [root.right]
    #    
    #    while len(left_stack) and len(right_stack):
    #        l_node = left_stack.pop()
    #        r_node= right_stack.pop()
    #        
    #        # False if one is null and the other not
    #        if (l_node is None) ^ (r_node is None):
    #            return False
    #        
    #        if not l_node is None:
    #            if l_node.val != r_node.val:
    #                return False
    #        
    #            left_stack.append(l_node.right)
    #            left_stack.append(l_node.left)
    #        
    #            right_stack.append(r_node.left)
    #            right_stack.append(r_node.right)
    #        
    #    return len(left_stack) == len(right_stack)
        
    # O(2^n) solution, recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:       
        return self.helper(root.left, root.right)
        
    def helper(self, l_node, r_node):
        if (l_node is None) ^ (r_node is None):
            return False
        
        if l_node is None:
            return True
        
        if l_node.val != r_node.val:
            return False
        
        if self.helper(l_node.left, r_node.right):
            return self.helper(l_node.right, r_node.left)
        
        return False