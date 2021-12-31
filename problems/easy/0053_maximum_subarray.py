"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

A subarray is a contiguous part of an array.

Example 1:
  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
  Input: nums = [1]
  Output: 1

Example 3:
  Input: nums = [5,4,-1,7,8]
  Output: 23

Constraints:
  * 1 <= nums.length <= 10^5
  * -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding
another solution using the divide and conquer approach, which
is more subtle.
"""

class Solution:   
    # O(n^2) approach, getting Time Limit Exceeded on LeetCode
    #def maxSubArray(self, nums: List[int]) -> int:
    #    maxSum = float('-inf')
    #    curSum = 0
    #    
    #    for i in range(len(nums)):
    #        curSum += nums[i]
    #        maxSum = max(maxSum, curSum)
    #        
    #        for j in range(i+1, len(nums)):
    #            curSum += nums[j]
    #            maxSum = max(maxSum, curSum)
    #            
    #        curSum = 0
    #        
    #    return maxSum
      
    # O(N*log n) approach (divide and conquer)
    #def maxSubArray(self, nums: List[int]) -> int:
    #    return self.findMaxSubArray(nums, 0, len(nums) - 1)
    
    #def findMaxSubArray(self, nums, start, end):
    #    if start > end:
    #        return float('-inf')
        
    #    mid = start + (end - start) // 2
    #    cur_sum = 0
    #    max_left_sum = 0
    #    max_right_sum = 0
        
    #    for i in range(mid - 1, start - 1, -1):
    #        cur_sum += nums[i]
    #        max_left_sum = max(max_left_sum, cur_sum)
        
    #    cur_sum = 0
    #    for i in range(mid + 1, end + 1):
    #        cur_sum += nums[i]
    #        max_right_sum = max(max_right_sum, cur_sum)
            
    #    return max(self.findMaxSubArray(nums, start, mid - 1),
    #               self.findMaxSubArray(nums, mid + 1, end),
    #               max_left_sum + nums[mid] + max_right_sum)
    
    
    # O(n) approach, Kadane's algorithm
    # keep adding numbers up until the sum is negative
    # whatever we would add further to our negative sum,
    # will not be max
    def maxSubArray(self, nums: List[int]) -> int:
        curSum , maxSum = 0, float('-inf')
        for n in nums:
            curSum += n
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
                
        return maxSum