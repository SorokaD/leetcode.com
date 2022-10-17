# 925. Long Pressed Name
# Your friend is typing his name into a keyboard. Sometimes,
# when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
# with some characters (possibly none) being long pressed.
# решение "не оптимамльно, упражнялся со словарями"

name = "alex"
typed = "alexxxx"

# Solution
def solution(name, typed):
    if len(set(name)) != len(set(typed)):
        return True
    dict_name = {}
    dict_typed = {}
    for i in set(name):
        dict_name[i] = name.count(i)
        dict_typed[i] = typed.count(i)
    for i in dict_name.keys():
        if dict_name[i] != dict_typed[i]:
            return True
    return False

print(solution(name, typed))
