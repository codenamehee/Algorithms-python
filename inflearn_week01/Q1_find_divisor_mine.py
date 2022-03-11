N, K = map(int, input().split()) # split : 띄어쓰기를 기준으로 input된 숫자를 자른다.

import sys
# sys.stdin = open("input.txt", "rt")

def findDivisor(N, K):
    divisor = []
    for i in range(1, N+1):
        if N%i==0:
            divisor.append(i)

    for j in range(len(divisor)):
        if len(divisor) > K:
            return divisor[K-1]
    return -1

print(findDivisor(N,K))


# N의 약수들 중 K번쨰로 작은 수 구하기
# 첫째줄에 주어지는 N, K를 저장하기
# N의 약수가 K보다 적을 경우 -1 출력하기