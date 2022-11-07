# 1021. Remove Outermost Parentheses
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into
# s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
# where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

s = "(()())(())(()(()))"

# Solution
def remover_outermost(s):
    res = ''
    begin = 0
    counter = 0
    for i, st in enumerate(s):
        if st =='(':
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            res += s[begin+1:i]
            begin = i+1
    return res

print(remover_outermost(s))
