# 976. Largest Perimeter Triangle
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
# formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

nums = [2,2,3]

# Solution
def solution(nms):
    nms = sorted(nms)
    if nms[0]+nms[1] > nms[2]:
        return sum(nms)
    return 0

print(solution(nums))