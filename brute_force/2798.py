from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for comb in combinations(cards, 3):
    temp_sum = sum(comb)
    if temp_sum <= m and temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)