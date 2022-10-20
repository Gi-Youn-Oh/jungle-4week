import sys
input = sys.stdin.readline
INF = 1e9

need_customer, city_num = map(int, input().split())
data = []

min_cost = [INF] * (need_customer+100)
min_cost[0] = 0

for _ in range(city_num):
    # cost, cus
    data.append(list(map(int, input().split())))

# cost 작은 순서로 정리
data_sort = sorted(data, key = lambda x: x[0])


for cost, cus in data_sort:
    for i in range(cus, need_customer+100): # 원하는 최소값이 딱 인원수 맞춰서가 아닌 인원수가 초과 되었을때 나올수도 있다.
        min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])

print(min(min_cost[need_customer:])) 