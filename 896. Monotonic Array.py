# 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

nums = [1,2,2,3,7]

# Solution
def solution(nums):
    prev = nums[0]
    sign = None
    if nums[0] > sum(nums[1:])/len(nums[1:]) : sign = 'desc'
    else: sign = 'asc'
    for i in nums:
        if i<prev and sign=='asc':
            return False
        else: prev = i
        if i>prev and sign=='desc':
            return False
        else: prev = i
    return True

print(solution(nums))