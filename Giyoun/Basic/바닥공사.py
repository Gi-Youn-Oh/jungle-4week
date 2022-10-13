# 정수 n 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍 진행 (bottom up)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[n-1] + 2 *d[n-2] % 796796)

print(d[n])