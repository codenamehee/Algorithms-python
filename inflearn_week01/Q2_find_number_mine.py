T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 두번째 줄부터 케이스가 시작되고, 각 케이스는 2줄씩 차지하며 차례로 주어진다.
# 이 때, 케이스의 첫번째 줄에는 자연수 N, s, e, k가 차례로 주어진다.
# 두 번째 줄에는 N개의 숫자가 차례로 주어진다.
# N개의 숫자열 중에서 s번째부터 e번째 까지의 수를 오름차순 정렬했을 대 k번째로 나타나는 수를 출력하기