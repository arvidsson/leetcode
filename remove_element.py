# remove all occurences of val in place in array, return array size
# https://leetcode.com/problems/remove-element


def removeElement(nums: [int], val: int) -> int:
    k = 0
    for i in reversed(range(len(nums))):
        if nums[i] == val:
            del nums[i]
        else:
            k += 1
    return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
excepted = [0, 1, 3, 0, 4]

removeElement(nums, val)
print("Result: ", nums)
print("Expected: ", excepted)
