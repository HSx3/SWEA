import sys
sys.stdin = open("day4_병합_정렬.txt")


def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global count

    left_N, right_N = len(left), len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    i = 0

    if left[-1] > right[-1]:
        count += 1

    while left_i != left_N and right_i != right_N:
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    if left_i != left_N:
        while left_i != left_N:
            result[i] += left[left_i]
            i += 1
            left_i += 1

    if right_i != right_N:
        while right_i != right_N:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    return result


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    count = 0
    a = merge_sort(a)

    print('#{} {} {}'.format(test_case, a[N//2], count))