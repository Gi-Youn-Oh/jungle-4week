# n, m , k 공백 입력
n, m, k  = map(int, input().split())
# n 개의수 공백으로 입력받기
data = list(map(int, input().split()))

data.sort() # 정렬
first = data[n-1] # 가장 큰수
second = data[n-2] # 두 번째로 가장 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m -count) * second  #두 번째로 큰 수 더하기

print(result)

# 반복되는 수열 줄이기
# 반복되는 수열 길이 = (K+1)
# m을 (k+1) 로 나눈 목시 수열이 반복되는 횟수
# 다시 여기에 k를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
# M이 (k+1)로 나누어 떨어지지 않는 경우
# m을 (k+1) 로 나눈 나머지 만큼 가장 큰 수가 추가로 더해짐
int(M / (k+1)) * k + M % (k + 1)


# 원래 답안
# # n, m , k 공백 입력
# n, m, k  = map(int, input().split())
# # n 개의수 공백으로 입력받기
# data = list(map(int, input().split()))

# data.sort() # 정렬
# first = data[n-1] # 가장 큰수
# second = data[n-2] # 두 번째로 가장 큰 수

# result= 0

# while True:
#     for i in range(k): # 가장 큰수를 k 번 더하기
#         if m == 0: # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1 # 더할 때마다 1씩 빼기
#     if m == 0: # m이 0이라면 반복문 탈출
#         break
#     result += second # 두 번째로 큰 수를 한번 더하기
#     m -= 1 #더할 때마다 1씩 빼기

# print(result)