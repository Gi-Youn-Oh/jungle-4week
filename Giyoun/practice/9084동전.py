import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    kind_coins = int(input())
    coins = list(map(int, input().split()))
    coins.insert(0,0) # 0번째 인덱스에 0 추가
    target = int(input())

    dp = [[0] * (target+1) for i in range(kind_coins+1)] # 부터 시작하기에
    for i in range(kind_coins+1):
        dp[i][0] = 1 # 0원을 만들 수 있는 가지수 1

    for j in range(1, kind_coins+1): #행
       for i in range(1, target+1): #열
            dp[j][i] = dp[j-1][i] # 위의 행의 값을 그대로 가지고 내려온다.
            if i-coins[j] >= 0:
                dp[j][i] +=dp[j][i-coins[j]]  
print(dp[kind_coins][target])

import sys

T = int(input())

for _ in range(T):
    kind_coins = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp =[0] * (target+1)
    dp[0] = 1
    for  coin in coins:
        for i in range(1, target+1):
            if i-coin >= 0:
                dp[i] += dp[i-coin]

print(dp[target])