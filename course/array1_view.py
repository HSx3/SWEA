import sys
sys.stdin = open("array1_view.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    count = 0
    for i in range(2, N-1):
        if buildings[i-2] >= buildings[i]:
            continue
        if buildings[i-1] >= buildings[i]:
            continue
        if buildings[i+1] >= buildings[i]:
            continue
        if buildings[i+2] >= buildings[i]:
            continue
        count += abs(buildings[i] - max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]))

    print('#{} {}'.format(test_case, count))