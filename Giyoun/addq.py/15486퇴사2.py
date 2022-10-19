import sys 
input = sys.stdin.readline 

n = int(input())
need_time,get_point = [],[]
dp = [0] * (n+1)
for i in range(n):
    x,y = map(int,input().split())
    need_time.append(x)
    get_point.append(y)
result = 0 
for i in range(n):
    result = max(result,dp[i])  
    if i+need_time[i] > n :  
        continue 
    dp[i+need_time[i]] = max(result+get_point[i],dp[i+need_time[i]])
print(max(dp))
# 각각의 날들을 '그날 상담을 시작하는 경우'와 '그날 상담을 시작하지 않는 경우'로 나눌 수 있다
# 만약 1일이라면 T = 3인 일을 시작할 수도 있고, 시작하지 않을 수도 있는 것이다
# 상담을 시작한다면, 상담이 끝난 다음 날의 수익이 P[i]만큼 증가한다
# n = 1이면 n = 4일 때의 수익이 10이 되는 것이다
# 상담을 시작하지 않는다면
# n에 +1을 해줘서 다음 날로 넘어간다
# n+1번째 날에도 동일한 처리를 반복해 나간다
# M은 이전에 저장된 M의 값과 dp[i]중 큰 것으로 갱신한다 
# dp[i]는 '현재까지의 수익에 이번 상담의 수익을 더한 값'과 '오늘의 상담이 끝나는 시점의 수익' 중 큰 값을 저장한다