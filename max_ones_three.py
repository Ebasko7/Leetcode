"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = ans = 0

        for num in nums:
            if num == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
            ans = max(ans, right - left)

        return ans


"""
Revisited this problem+ 2 weeks later, similar solution below'
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        if len(nums) <= k:
            return len(nums)

        left = ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
