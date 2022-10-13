# 905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

nums = [3,1,2,4]

# Solution
def solution(nums):
    chet = []
    nechet = []
    for i in nums:
        if i%2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
    return chet+nechet

print(solution(nums))

