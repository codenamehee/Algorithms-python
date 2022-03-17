n, k = map(int, input().split())
cards = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(cards[i] + cards[j] + cards[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])