import sys
sys.stdin = open("tree_이진_힙.txt")

import heapq

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    heap = []

    for number in numbers:
        heapq.heappush(heap, number)

    # 부모 노드 = 자식노드 // 2
    answer = 0
    while N > 1:
        answer += heap[(N//2) - 1]  # 마지막 노드 => N
        N = N // 2

    print('#{} {}'.format(test_case, answer))