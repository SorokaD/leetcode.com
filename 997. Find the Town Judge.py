# 997. Find the Town Judge
# In a town, there are n people labeled from 1 to n.
# There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi]
# representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

n = 3
trust = [[1,3],[2,3],[3,1]]

# Solution
def judge(n,tr):
    citizens = [x for x in range(1,n+1)]
    trusts = [x[0] for x in tr] # список тех, кто доверяет
    if set(citizens) == set(trusts):
        return -1
    jd = list(set(citizens) - set(trusts))[0]
    count = 0
    for i in tr:
        if i[1] == jd:
            count += 1

    if count != n-1:
        return -1
    return jd

print(judge(n,trust))