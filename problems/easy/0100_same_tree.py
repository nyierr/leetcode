"""
Given the roots of two binary trees p and q, write a function to
check if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

Example 1:
  Input: p = [1,2,3], q = [1,2,3]
  Output: true
    
Example 2:
  Input: p = [1,2], q = [1,null,2]
  Output: false

Example 3:
  Input: p = [1,2,1], q = [1,1,2]
  Output: false

Constraints:
  * The number of nodes in both trees is in the range [0, 100]
  * -10^4 <= Node.val <= 10^4
"""

class Solution:          
    # O(2^n) solution, iterative
    #def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #    if p is None and q is None:
    #        return True
    #    
    #    if p is None or q is None:
    #        return False
    #    
    #    stack_p = [p.right, p.left, p]
    #    stack_q = [q.right, q.left, q]
    #    while len(stack_p) and len(stack_q):
    #        p = stack_p.pop()
    #        q = stack_q.pop()
    #    
    #        if p is None and q is None:
    #            return True
    #    
    #        if p.val != q.val:
    #            return False
    #
    #        # False, if one has a left node and the other one does not
    #        if (p.left is None) ^ (q.left is None):
    #            return False
    #        
    #        # False, if one has a right node and the other one does not
    #        if (p.right is None) ^ (q.right is None):
    #            return False
    #        
    #        if not p.right is None:
    #            stack_p.append(p.right)
    #            stack_q.append(q.right)
    #            
    #        if not p.left is None:
    #            stack_p.append(p.left)
    #            stack_q.append(q.left)
    #        
    #    return len(stack_p) == len(stack_q)
    
    # O(2^n) solution, recursive one
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) ^ (q is None):
            return False
            
        if p is None and q is None:
            return True
        
        if p.val != q.val:
            return False
        
        if self.isSameTree(p.left, q.left):
            return self.isSameTree(p.right, q.right)
            
        return False