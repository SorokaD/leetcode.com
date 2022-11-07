# 1005. Maximize Sum Of Array After K Negations
# Given an integer array nums and an integer k, modify the array in the following way:

# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.

# Return the largest possible sum of the array after modifying it in this way.

nums = [2,-3,-1,5,-4]
k = 2

def maximizer(nm, k):
    srt = sorted(nm)
    for i in range(len(nm)):
        if nm[i] in srt[0:k] and nm[i]<0:
            nm[i] = -nm[i]
    return sum(nm)

print(maximizer(nums,k))