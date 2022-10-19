import sys
input = sys.stdin.readline

# 사용한 추의 개수, num개의 추를 사용하여 만든 구슬의 무게
def cal(num, make_weight):
  # 사용할 수 있는 추의 개수를 넘어가면 종료
  if num > weight_num:  return

  # 1. num번째까지 추로 make_weight 무게를 만들 수 있음이 이미 기록되어있으면 종료
  if dp[num][make_weight]:  return
  # 2. num번째까지 추로 make_weight 무게를 만들 수 있음을 체크
  dp[num][make_weight] = True 
    
  # 3가지 경우 수행 / 0번부터 실행했기 때문에 num -1 
  cal(num + 1, make_weight + weight_list[num - 1])  # 추의 무게를 더함
  cal(num + 1, abs(make_weight - weight_list[num - 1]))  # 추의 무게를 뺌
  cal(num + 1, make_weight)  # 추를 사용하지 않음

weight_num = int(input())  # 추 개수
weight_list = list(map(int, input().split()))  # n개의 추의 무게
marble_num = int(input())  # 구슬 개수
marble_list = list(map(int, input().split()))  # m개의 구슬 무게
# dp[i][j]: i번째까지 추를 사용했을 때 j무게를 만들 수 있는지 여부
dp = [[False] * 15001 for _ in range(31)]

cal(0, 0)  # 지금까지 사용한 추 개수, 추로 만든 구슬의 무게를 0으로 시작

# m개의 구슬 무게를 확인할 수 있는지
for t in marble_list:
  # 만들 수 있는 구슬의 무게는 30*500이 최대임
  if t > 15000:  print("N", end=" ") 
  elif dp[weight_num][t]: print("Y", end=" ")
  else:  print("N", end=" ")