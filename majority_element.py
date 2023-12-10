# find the majority element in array, where majority means existing in the array at least array length / 2 times
# https://leetcode.com/problems/majority-element


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        majority = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1
        numbers = {}
        element = 0
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1
            if numbers[num] >= majority:
                element = num
        return element
