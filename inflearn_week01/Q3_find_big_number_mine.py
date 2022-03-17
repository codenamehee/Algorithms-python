import itertools
n, k = map(int, input().split())
cards = list(map(int, input().split()))
combs = list(itertools.combinations(cards, 3))
sums = []
for i in combs:
    sums.append(sum(i))

result = []
for j in sums:
    if j not in result:
        result.append(j)

result = sorted(sums, reverse=True)

print(result[2])

# 65 45 42 34 33 26 23 15 13 11
# 65 + 45 + 42 = 110 + 42 = 152
# 65 + 45 + 34 = 110 + 34 = 144
# 65 + 45 + 33 = 143