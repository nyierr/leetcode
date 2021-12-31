"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
  Input: nums = [1,3,5,6], target = 5
  Output: 2

Example 2:
  Input: nums = [1,3,5,6], target = 2
  Output: 1

Example 3:
  Input: nums = [1,3,5,6], target = 7
  Output: 4

Constraints:
  * 1 <= nums.length <= 10^4
  * -10^4 <= nums[i] <= 10^4
  * nums contains distinct values sorted in ascending order
  * -10^4 <= target <= 10^4
"""

class Solution:
    # O(log n), iterative binary search 
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        return start
    
    # O(log n), recursive binary search
    #def searchInsert(self, nums: List[int], target: int) -> int:
    #    return self.search(nums, target, 0, len(nums) - 1)
    #    
    #def search(self, nums, target, start, end):
    #    if end < start:
    #        return start
    #    
    #    mid = start + (end - start) // 2
    #    if target == nums[mid]:
    #        return mid
        
    #    if target < nums[mid]:
    #        return self.search(nums, target, start, mid-1)
        
    #    return self.search(nums, target, mid+1, end)