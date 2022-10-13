# 908. Smallest Range I
# You are given an integer array nums and an integer k.
# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.
# The score of nums is the difference between the maximum and minimum elements in nums.
# Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

nums = [0,10]
k = 2

# Solution
def solution(nums, k):
    mn = min(nums)
    mx = max(nums)
    return max(mx-mn-k * 2, 0)

print(solution(nums,k))