# 1046. Last Stone Weight
# ou are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0

stones = [2,7,4,1,8,1,1]

# Solution
def ls_weight(st):
    cnt = 0
    while len(st) >= 2:
        s1 = max(st)
        st.remove(s1)
        s2 = max(st)
        st.remove(s2)
        if abs(s1-s2):
            st.append(abs(s1-s2))
    return sum(st)

print(ls_weight(stones))