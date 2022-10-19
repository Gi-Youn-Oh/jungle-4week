import sys
import heapq

jewlry_num, bag_num= map(int, sys.stdin.readline().split())
jewlry_list = []
for _ in range(jewlry_num):
    heapq.heappush(jewlry_list, list(map(int, sys.stdin.readline().split())))
# print(jewlry_list)
bag_list = []
for _ in range(bag_num):
    bag_list.append(int(sys.stdin.readline()))
bag_list.sort()
# print(bag_list)
answer = 0
test_jewlry = []
for bag in bag_list:
    while jewlry_list and bag >= jewlry_list[0][0]:
        heapq.heappush(test_jewlry, -heapq.heappop(jewlry_list)[1])
    if test_jewlry:
        answer -= heapq.heappop(test_jewlry)

print(answer)
