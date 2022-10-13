# 914. X of a Kind in a Deck of Cards
# ou are given an integer array deck where deck[i] represents the number written on the ith card.
# Partition the cards into one or more groups such that:
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

deck = [1,2,3,4,4,3,2,1]

# Solution
def solution(deck):
    set_deck = set(deck)
    rslt = []
    for i in set_deck:
        rslt.append(deck.count(i))
    if len(set(rslt)) > 1:
        return False
    return True

print(solution(deck))