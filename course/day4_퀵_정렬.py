import sys
sys.stdin = open("day4_퀵_정렬.txt")


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr

# def quicksort(x):
#     if len(x) <= 1:
#         return x
#
#     pivot = x[len(x) // 2]
#     less = []
#     more = []
#     equal = []
#     for a in x:
#         if a < pivot:
#             less.append(a)
#         elif a > pivot:
#             more.append(a)
#         else:
#             equal.append(a)
#
#     return quicksort(less) + equal + quicksort(more)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    sorted_numbers = quick_sort(numbers, 0, N-1)
    # sorted_numbers = quicksort(numbers)

    answer = sorted_numbers[N//2]
    print('#{} {}'.format(test_case, answer))
