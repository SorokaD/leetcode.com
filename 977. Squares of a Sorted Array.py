# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

nums = [-4, -1, 0, 3, 10]

# Solution1
def asc_squares_py(nm):
    return sorted([x ** 2 for x in nm])

# Solution2
def asc_squares_buble(nm):
    nm = [x ** 2 for x in nm]
    for i in range(len(nm)-1):
        for j in range(len(nm)-i-1):
            if nm[j]>nm[j+1]:
                nm[j], nm[j+1] = nm[j+1], nm[j]
    return nm

print(asc_squares_buble(nums))
print(asc_squares_py(nums))
