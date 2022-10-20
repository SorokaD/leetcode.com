# 961. N-Repeated Element in Size 2N Array
# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

nums = [5,1,5,2,5,3,5,4]

# Solution
def solution(nm):
    for i in set(nm):
        if nm.count(i) == len(nm)/2:
            return i
    return None

print(solution(nums))