import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())

    nums = list(map(int, input().split()))
    for _ in range(N-1):
        _, c = map(int, input().split())  # 5x3 3x2 에서 3은 생략 
        nums.append(c)      # 5, 3, 2, 6

    # DP
    dp = [[0]*N for _ in range(N)]
    for d in range(N):  # 3
        for i in range(N - d):  # 3-0 3-1 3-2
            j = i + d

            if i == j:
                continue

            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] 
                + nums[i]*nums[k+1]*nums[j+1])

    print(dp[0][-1])   # i 행 j 열 k 는 i j 사이 어딘가 i = k 같을수도

# d = diagonal 행렬의 곱셈 횟수

# 행렬의 곱셈 (5x3) * (3x2) = 5x2  
    # 참조 https://rccode.tistory.com/155