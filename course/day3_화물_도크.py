import sys
sys.stdin = open("day3_화물_도크.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = []

    for i in range(N):
        s, e = (map(int, input().split()))
        length = e-s
        data.append([length, s, e])

    data = sorted(data)
    visited = [0]*24
    count = 0

    for l, s, e in data:
        flag = 1
        for i in range(s, e):
            if visited[i]:
                flag = 0
                break
        if flag:
            visited[s:e] = [1]*(e-s)
            count += 1

    print('#{} {}'.format(test_case, count))