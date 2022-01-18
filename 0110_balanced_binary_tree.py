"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node
differ in height by no more than 1.

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: true
    
Example 2:
  Input: root = [1,2,2,3,3,null,null,4,4]
  Output: false

Example 3:
  Input: root = []
  Output: true

Constraints:
  * The number of nodes in the tree is in the range [0, 5000]
  * -10^4 <= Node.val <= 10^4
"""

class Solution:
    # O(2^n) solution, recursive
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left = {}
        right = {}
        self.helper(root, left, right)
        
        for k in left:
            if abs(left[k] - right[k]) > 1:
                return False
            
        return True
        
    def helper(self, node, l={}, r={}):
        if not node is None:
            l[node] = 0
            r[node] = 0
            
            if not node.left is None:
                self.helper(node.left, l, r)
                l[node] = max(l[node.left], r[node.left]) + 1
                
            if not node.right is None:
                self.helper(node.right, l, r)
                r[node] = max(l[node.right], r[node.right]) + 1
    