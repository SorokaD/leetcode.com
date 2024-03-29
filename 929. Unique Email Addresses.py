# 929. Unique Email Addresses
# Every valid email consists of a local name and a domain name, separated by the '@' sign.
# Besides lowercase letters, the email may contain one or more '.' or '+'.
# f you add periods '.' between some characters in the local name part of an email address,
# mail sent there will be forwarded to the same address without dots in the local name.
# Note that this rule does not apply to domain names.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered. Note that this rule does not apply to domain names.
# It is possible to use both of these rules at the same time.
# Given an array of strings emails where we send one email to each emails[i],
# return the number of different addresses that actually receive mails.

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

# Solution
def solution(mails):
    result = []
    for i in mails:
        k = i.split('@')
        k_before = [x for x in k[0].split('+')[0] if x not in ['.']]
        k_after = [x for x in k[1]]
        result.append(''.join(k_before)+'@'+''.join(k_after))
    return len(set(result))

print(solution(emails))
