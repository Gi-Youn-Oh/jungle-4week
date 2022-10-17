# import sys
# input = sys.stdin.readline

# word1, word2 = input().strip(), ().strip()
# heihgt, width = len(word1), len(word2)
# cache = [[0] * (width+1) for _ in range(heihgt+1)]

# for i in range(1, heihgt+1):
#     for j in range(1, width+1):
#         if word1[i-1] == word2[j-1]:
#             cache[i][j] = cache[i-1][j-1] + 1
#         else:
#             cache[i][j] = max(cache[i][j-1], cache[i-1][j])
# print(cache[-1][-1])

# 대각선 방향 -> 
# 왼쪽 위방향 맥스값 ->

import sys
input = sys.stdin.readline

word1, word2 = input().strip(), input().strip()
len1, len2 = len(word1), len(word2)
dp = [0] * len2

for i in range(len1):
    count = 0
    for j in range(len2):
        if count < dp[j]:
            count = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = count + 1
print(max(dp))

# count를 누적 변수로 사용한다.
# 누적 변수의 값이 캐시값보다 작으면 교체한다.
# 글자가 같은 경우 누적 변수에서 1을 더한다
# 글자 하나를 기준으로 1차원 배열을 만들어주고 같은 글자를 순회하는 경우 누적 값에서 1을 더한 값을 넣어주는 방식이다. 
# 순회할 때마다 누적값을 저장할 변수를 하나 사용하고 만약 글자가 다른 경우 누적 변수의 값이 해당 위치의 값보다 작은 경우 해당 값으로 교체해준다.
#  이렇게 하면 누적 값에는 이전 위치까지 까지의 최대값이 계속해서 저장된다.