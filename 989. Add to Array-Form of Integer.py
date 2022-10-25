# 989. Add to Array-Form of Integer
# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

num = [1, 2, 0, 0]
k = 34

# Solution
def array_plus_int(nm, k):
    nm = [str(x) for x in nm]
    nm = str(int(''.join(nm)) + k)
    nm = [int(i) for i in nm]

    print(nm)

array_plus_int(num,k)