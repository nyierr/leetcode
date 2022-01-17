"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: 3
    
Example 2:
  Input: root = [1,null,2]
  Output: 2

Constraints:
  * The number of nodes in the tree is in the range [0, 10^4]
  * -100 <= Node.val <= 100
"""

class Solution:
    # O(2^n) solution, iterative
    # Use a stack to keep track of every path from the 
    # root to each leaf
    #def maxDepth(self, root: Optional[TreeNode]) -> int:
    #    if root is None:
    #        return 0
    #    
    #    left_done = {}
    #    right_done = {}
    #    
    #    stack = [root]
    #    max_depth = 0
    #    
    #    while len(stack):
    #        curr = stack[-1]
    #
    #        if not curr in left_done:
    #           left_done[curr] = True
    #            
    #            if curr.left:
    #                stack.append(curr.left)
    #            elif curr.right:
    #                right_done[curr] = True
    #                stack.append(curr.right)
    #            else:
    #                max_depth = max(max_depth, len(stack))
    #                stack.pop()
    #        elif not curr in right_done:
    #            right_done[curr] = True
    #            
    #            if curr.right:
    #                stack.append(curr.right)
    #            else:
    #                max_depth = max(max_depth, len(stack))
    #                stack.pop()
    #        else:
    #            stack.pop()
    #                
    #    return max_depth
                            
    # O(2^n) solution, recursive with a helper function
    #def maxDepth(self, root: Optional[TreeNode]) -> int:
    #    return self.findMaxDepth(root, 0)
    #    
    #def findMaxDepth(self, node, count):
    #    if node is None:
    #        return count
    #    
    #    left = self.findMaxDepth(node.left, count + 1)
    #    right = self.findMaxDepth(node.right, count + 1)
    #    
    #    return max(left, right)
    
    # O(2^n) solution, recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        
        return max(left, right)