import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    count = 1 #서류 1등은 무조건 1등
    
    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]: 
            top = i  # 서류합격 1등기준 면접순위보다 높은 사람으로 교체
            count += 1
    
    print(count)