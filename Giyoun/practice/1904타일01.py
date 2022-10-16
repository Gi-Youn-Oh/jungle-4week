dp = [0] * 1000001

n = int(input())

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = (dp[n-1] + dp[n-2]) % 15746

print(dp[n]) 
