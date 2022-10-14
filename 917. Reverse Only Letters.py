# 917. Reverse Only Letters
# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

s = "a-bC-dEf-ghIj"

# Solution()
def solution(s):
    leters = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    s_leters = [x for x in s if x in leters]
    result = ''
    counter = len(s_leters)-1
    for i in range(len(s)):
        if s[i] not in leters:
            result += s[i]
            continue
        result += s_leters[counter]
        counter -= 1
    return result


print(solution(s))

