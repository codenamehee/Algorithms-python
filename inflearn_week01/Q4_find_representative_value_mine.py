# 주어진 숫자들을 배열로 받아 저장하고 평균 구하기
# 평균과 점수가 가깝다 => 평균과의 차이가 가장 작다 는 말이므로 배열의 점수들과의 차이를 구해서
# 새로운 배열에 다시 차례로 넣기
# 차이가 들어있는 배열을 오름차순 정리한다.
n = int(input())
a = list(map(int, input().split()))
# round_half_even 방식이기 때문에 5.5, 5.55 등 정확히 반틈인 숫자가 나올경우 6이 아닌 5가 출력되게 된다.
# ave = round(sum(a)/n)
ave = int((sum(a)/n)+0.5)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp<min:
        min=tmp
        score=x # 점수
        res = idx+1 # 학생번호
    elif tmp==min: # 평균과의 점수 차이가 가장 작은 숫자가 여러개일때
        if x>score: #현재 학생의 점수가 그 전에 답이 되었던 학생의 점수보다 클 때
            score=x # score이 현재 학생의 점수가 된다.
            res = idx+1
print(ave, res)
