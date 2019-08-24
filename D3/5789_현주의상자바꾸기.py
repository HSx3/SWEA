import sys
sys.stdin = open("5789_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0]*N
    for i in range(1, Q+1):
        Li, Ri = map(int, input().split())

        for j in range(Li-1, Ri):
            boxes[j] = i
    print('#{}'.format(test_case), end=' ')
    print(*boxes)