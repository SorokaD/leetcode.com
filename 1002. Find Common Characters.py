# 1002. Find Common Characters
# Given a string array words, return an array of all characters that show up in all strings within the words
# (including duplicates). You may return the answer in any order.

words = ["bella", "label", "roller"]

def finder_cc(wd):
    result = list(wd[0])
    for i in range(1, len(wd)):
        result = list(set(result) & set(wd[i]))
    return result

print(finder_cc(words))
