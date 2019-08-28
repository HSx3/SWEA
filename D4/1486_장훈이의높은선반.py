import sys
sys.stdin = open('1486_input.txt')


def DFS(no, hsum):
    global count, check_hsum
    if no >= N:
        if hsum < B:
            return

        check_hsum.append(hsum)

    else:
        check[no] = 1
        DFS(no+1, hsum+heights[no])
        check[no] = 0
        DFS(no+1, hsum)


T = int(input())

for test_case in range(1, T+1):
    count = 0
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    # print(N, B)
    # print(heights)
    check = [0] * N
    check_hsum = []
    DFS(0, 0)
    check_hsum.sort()
    print('#{} {}'.format(test_case, check_hsum[0]-B))