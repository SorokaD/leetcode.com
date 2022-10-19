# 941. Valid Mountain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:

arr = [0,3,2,1]

#Solution
def solution(arr):
    if len(arr) < 3 :
        return False
    prev = arr[0]
    for i in range(1,len(arr)):
        i = 1
        prev = arr[0]
        while arr[i] < max(arr[0:len(arr)-1]):
            if arr[i] <= prev:
                return False
            prev = arr[i]
            i += 1
        prev = max(arr[0:len(arr)-1])
        i += 1
        while i < len(arr):
            if arr[i] >= prev:
                return False
            prev = arr[i]
            i += 1
    return  True

print(solution((arr)))