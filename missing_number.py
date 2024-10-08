"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        numset = set(nums)

        for number in range(n + 1):
            if number not in numset:
                return number
