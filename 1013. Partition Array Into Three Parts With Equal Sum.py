# 1013. Partition Array Into Three Parts With Equal Sum
# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

arr = [0,2,1,-6,6,7,9,-1,2,0,1]

# Solution
def partitioner(ary):
    p_sum_3 = sum(arr)/3
    p_sum = 0
    cntr = 0
    for i in ary:
        p_sum += i
        if p_sum == p_sum_3:
            cntr += 1
            if cntr == 3:
                return True
            p_sum = 0
    return False

print(partitioner(arr))