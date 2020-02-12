import sys
sys.stdin = open("list2_특별한정렬.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))

    for i in range(len(numbers)):
        temp_i = i
        if i % 2 == 0:
            m_i = numbers.index(max(numbers[temp_i:]))
            # numbers[temp_i], numbers[m_i] = numbers[m_i], numbers[temp_i]

        else:
            m_i = numbers.index(min(numbers[temp_i:]))
            # numbers[temp_i], numbers[m_i] = numbers[m_i], numbers[temp_i]

        numbers[temp_i], numbers[m_i] = numbers[m_i], numbers[temp_i]

    print('#{}'.format(test_case), end=' ')

    for i in range(10):
        print(numbers[i], end=' ')
    print()
