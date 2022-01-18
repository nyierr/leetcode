"""
Given an integer array nums where the elements are sorted in
ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of
the two subtrees of every node never differs by more than one.

Example 1:
  Input: nums = [-10,-3,0,5,9]
  Output: [0,-3,9,-10,null,5]
  Explanation: [0,-10,5,null,-3,null,9] is also accepted
    
Example 2:
  Input: nums = [1,3]
  Output: [3,1]
  Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

Constraints:
  * 1 <= nums.length <= 10^4
  * -10^4 <= nums[i] <= 10^4
  * nums is sorted in a strictly increasing order
"""

import math

class Solution:
    # O(n) solution, recursive
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)
        
    def helper(self, nums, start, end):
        if start <= end:
            if start == end:
                return TreeNode(nums[start])
        
            # Using math.ceil creates a tree which is matching
            # the expected LeetCode output
            mid = math.ceil(start + (end - start) / 2)
        
            # Rounding down will also work and produce a balance tree
            # but it will be different from the exepected LeetCode one
            #mid = start + (end - start) // 2
        
            node = TreeNode(nums[mid])
        
            node.left = self.helper(nums, start, mid - 1)
            node.right = self.helper(nums, mid + 1, end)
        
            return node