import sys
sys.stdin = open("day3_컨테이너_운반.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    cargo = sorted(w, reverse = True)
    truck = sorted(t, reverse = True)

    total = 0
    visited = [0]*N
    count = 0

    for i in range(len(cargo)):
        if count >= M:
            break
        elif cargo[i] <= truck[0] and count < M:
            visited[i] = True
            truck.pop(0)
            count += 1
            total += cargo[i]

    print('#{} {}'.format(test_case, total))