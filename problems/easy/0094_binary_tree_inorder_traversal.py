"""
Given the root of a binary tree, return the inorder traversal of its
nodes' values.

Example 1:
  Input: root = [1,null,2,3]
  Output: [1,3,2]
    
Example 2:
  Input: root = []
  Output: []

Example 3:
  Input: root = [1]
  Output: [1]

Constraints:
  * The number of nodes in the tree is in the range [0, 100]
  * -100 <= Node.val <= 100
  
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

class Solution:          
    # O(2^n) recursive solution, using default arg to collect result
    #def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #    res = []
    #    self.helper(root, res)
    #    return res
    #
    #def helper(self, node, res=[]):
    #    if not node is None:
    #        self.helper(node.left, res)
    #        res.append(node.val)
    #        self.helper(node.right, res)
    
    # O(2^n) recursive solution
    #def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #    if root is None:
    #        return [] 
    #    res = self.inorderTraversal(root.left)
    #    res.append(root.val)
    #    res += self.inorderTraversal(root.right)
    #    return res
    
    # O(2^n) iterative solution (breadth-first)
    #def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #    if root is None:
    #        return []
    #    
    #    to_do = [root.right, root, root.left]
    #    visited = {root: True}
    #    
    #    res = []
    #    while len(to_do):
    #        curr = to_do[-1]
    #        if curr is None:
    #            to_do.pop()
    #            continue
    #        
    #        # Already visited or a leaf
    #        if curr in visited or (curr.left is None and curr.right is None):
    #            to_do.pop()
    #            res.append(curr.val)
    #            continue
    #
    #        if not curr.right is None:
    #            to_do.insert(-1, curr.right)
    #        if not curr.left is None:
    #            to_do.append(curr.left)
    #            
    #        visited[curr] = True                
    #        
    #    return res
    
    # O(2^n) iterative solution (depth-first)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if len(stack) == 0:
                return res
            
            curr = stack.pop()
            res.append(curr.val)
            root = curr.right