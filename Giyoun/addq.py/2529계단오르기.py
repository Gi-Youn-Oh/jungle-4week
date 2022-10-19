import sys
input = sys.stdin.readline
arr = []
dp = []

l = int(input())
for _ in range(l):
    arr.append(int(input()))

dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1]))
dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
for i in range(3,l):
    dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

print(dp.pop())

# 진섭이형
import sys
input = sys.stdin.readline
number_stair = int(input())
list_stair = [0]
for _ in range(number_stair):
    list_stair.append(int(input()))
dp = [[0, 0, 0] for _ in range(number_stair+1)]
for i in range(1, number_stair+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + list_stair[i]
    dp[i][2] = dp[i-1][1] + list_stair[i]
answer = max(dp[number_stair][1], dp[number_stair][2])
print(answer)