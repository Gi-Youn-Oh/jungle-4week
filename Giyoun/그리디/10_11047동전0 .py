import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
print(coin_list)
count = 0
for coin in coin_list:
    if coin <= k :
        count += k//coin
        k %= coin

print(count)
