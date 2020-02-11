import sys
sys.stdin = open("list1_숫자_카드.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(input())

    counters = [0] * 10

    for number in numbers:
        counters[int(number)] += 1

    max_count = 0
    max_index = 0

    for idx, val in enumerate(counters):
        if val >= max_count:
            max_count = val
            max_index = idx

    print('#{} {} {}'.format(test_case, max_index, max_count))


    # print('4', counters(reverse = True)))

    # for idx, val in enumerate(counters[::-1]):
    #
    #     if val == max(counters):
    #         print('#{} {} {}'.format(test_case, 9-idx, val))
    #         break