import sys
sys.stdin = open("list2_특별한정렬.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))

    for i in range(len(numbers)):
        temp_i = i
        if i % 2 == 0:
            max_i = numbers.index(max(numbers[temp_i:]))
            numbers[temp_i], numbers[max_i] = numbers[max_i], numbers[temp_i]

        else:
            min_i = numbers.index(min(numbers[temp_i:]))
            numbers[temp_i], numbers[min_i] = numbers[min_i], numbers[temp_i]

    print('#{}'.format(test_case), end=' ')

    for i in range(10):
        print(numbers[i], end=' ')
    print()


    # for i in range(len(numbers)):
    #     if i % 2 == 0:
    #         even.append(numbers[i])
    #     else:
    #         odd.append(numbers[i])
    #
    # # odd = odd[::-1]
    # answer = []
    #
    # # 짝수개 = odd 뒤집기
    # # 홀수개 = even 뒤집기
    #
    # if N % 2 == 0:
    #     odd = odd[::-1]
    #
    #     for i in range
    #
    # else:
    #     even = even[::-1]
    #
    # print(even)
    # print(odd)
    #
    # # print('#{} {}'.format(test_case, ))
