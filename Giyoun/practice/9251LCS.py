import sys
input = sys.stdin.readline

word1, word2 = input().strip(), input().strip()

height , width = len(word1), len(word2)
dp = [[0] * (width + 1) for _ in range(height+1)]

for i in range(1, height+1):
    for j in range(1,width +1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])

import sys
input =sys.stdin.readline
word1, word2 = input().strip(), input().strip()
len1, len2 = len(word1), len(word2)
dp = [0] * len2

for i in range(len1):
    count = 0
    for j in range(len2):
        if count < dp[j]:
            count = dp[j]
        elif word1[i] == word2[j]:
            dp[j]  = count +1

print(max(dp))

# https://myjamong.tistory.com/m/317