# 922. Sort Array By Parity II
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

nums = [4,2,5,7]

# Solution
def solution(nums):
    odds = [x for x in nums if x % 2 != 0]
    evens = [x for x in nums if x % 2 ==0]
    result = []
    for i in range(len(odds)):
        result.append(evens[i])
        result.append(odds[i])
    return result

print(solution(nums))