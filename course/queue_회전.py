import sys
sys.stdin = open("queue_회전.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for time in range(M):
        number = numbers.pop(0)
        numbers.append(number)

    print('#{} {}'.format(test_case, numbers[0]))