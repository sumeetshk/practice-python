accounts = [[2, 3], [2, 6], [4, 3]]


def maximumWealth(accounts):
    return max([sum(acc) for acc in accounts])


print(maximumWealth(accounts))
