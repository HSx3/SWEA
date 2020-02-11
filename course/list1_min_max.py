import sys
sys.stdin = open("list1_min_max.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    print('#{} {}'.format(test_case, max(data)-min(data)))