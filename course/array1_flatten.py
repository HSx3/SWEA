import sys
sys.stdin = open("array1_flatten.txt")

T = 10

for test_case in range(1, T+1):
    dump = int(input())
    data = list(map(int, input().split()))

    while dump != 0:
        max_idx = data.index(max(data))
        min_idx = data.index(min(data))
        data[max_idx] -= 1
        data[min_idx] += 1
        dump -= 1

    answer = max(data) - min(data)
    print('#{} {}'.format(test_case, answer))