from itertools import combinations, permutations
friends = 'jim james bob'.split()

def friends_teams(friends, team_size=2, order_does_matter=False):
    if not order_does_matter:
        return combinations(friends, team_size)
    else:
        return permutations(friends, team_size)

if __name__ == '__main__':
    print(list(friends_teams(friends)))
