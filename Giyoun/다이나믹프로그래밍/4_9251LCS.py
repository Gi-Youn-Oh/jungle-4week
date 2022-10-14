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
cache = [0] * len2

for i in range(len1):
    count = 0
    for j in range(len2):
        if count < cache[j]:
            count = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = count + 1
print(max(cache))

# count 변수를 놓고 저장을 하면 리스트 인덱스 한바퀴 돌고 +1
# 이전 요소에 대해 생각할 필요가없다.
# 