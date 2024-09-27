"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

"""


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        prefix = [0]
        total = 0

        for val in nums:
            total += val
            prefix.append(total)

        avgs = []
        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                avgs.append(-1)
            else:
                window_sum = prefix[i + k + 1] - prefix[i - k]
                current = window_sum // (2 * k + 1)
                avgs.append(current)

        return avgs


