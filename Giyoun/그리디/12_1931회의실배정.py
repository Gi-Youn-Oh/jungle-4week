N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])
# [3,6] [4,6] 인경우 시작시간 먼저 정렬해줘야 됨
time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
print(time)
# [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
print(time)

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)
