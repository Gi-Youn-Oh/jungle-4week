n = int(input())

wine_list = []

for i in range(n):
    wine_list.append(int(input()))

d = [0]*n

d[0] = wine_list[0]
if n > 1:
    d[1] = wine_list[0]+wine_list[1]

if n > 2:
    d[2] = max(wine_list[2]+wine_list[1], wine_list[2]+wine_list[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+wine_list[i-1]+wine_list[i], d[i-2]+wine_list[i])

print(d[n-1])

# ① 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. ( wine[i]+wine[i-1]+d[i-3] )

# ② 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( wine[i]+d[i-2] )

# ③ 현재 포도주를 마시지 않는다. ( d[i-1] )