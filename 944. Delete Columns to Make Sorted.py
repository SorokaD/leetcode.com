# 944. Delete Columns to Make Sorted
# You are given an array of n strings strs, all of the same length.
# The strings can be arranged such that there is one on each line, making a grid.
# For example, strs = ["abc", "bce", "cae"] can be arranged as:
# You want to delete the columns that are not sorted lexicographically.
# In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column
# 1 ('b', 'c', 'a') is not, so you would delete column 1.
# Return the number of columns that you will delete.

strs = ["cba","daf","ghi"]

# Solution
def solution(srs):
    result = 0
    for i in range(len(srs)):
        res = []
        for j in range(len(srs[0])):
            res.append(srs[j][i])
        if res != sorted(res):
            result += 1
    return result

print(solution(strs))

