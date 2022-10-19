import sys

input = sys.stdin.readline

weights_count = int(input())
weights = list(map(int, input().split()))

marbles_count = int(input())
marbles = list(map(int, input().split()))

dp = [False] * 40001
dp[0] = True

for weight in weights:
    canmake = set()
    for i in range(40001):
        if dp[i] == True:
            if i + weight <= 40001:
                canmake.add(i+weight) 
            canmake.add(abs(i-weight))
    for c in canmake:
        dp[c] = True

for marble in marbles:
    if dp[marble] == True:
        print('Y', end=" ")
    else:
        print('N', end=" ")
        

import sys
input = sys.stdin.readline
# 초기 입력
N = int(input()) # 추의 갯수
wgt = list(map(int, input().split())) # 추
M = int(input()) # 구슬의 갯수
mbl = list(map(int, input().split())) # 구슬
s = set()
for i in wgt:
    temp_set = set()
    for j in s:
        temp_set.add(i + j)
        temp_set.add(abs(i - j))
    temp_set.add(i)
    s |= temp_set
for i in mbl:
    print("Y" if i in s else "N", end = ' ')
print()