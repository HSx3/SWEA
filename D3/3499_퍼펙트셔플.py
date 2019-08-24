import sys
sys.stdin = open("3499_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))

    left = []
    right = []

    if N % 2 == 0:
        left += cards[:N//2]
        right += cards[N//2:]
    else:
        left += cards[:(N//2)+1]
        right += cards[(N//2)+1:]

    reversed_left = list(reversed(left))
    reversed_right = list(reversed(right))
    answer = []

    for i in range(len(reversed_right)):
        answer.append(reversed_left.pop())
        answer.append(reversed_right.pop())

    if N % 2 != 0:
        answer.append(reversed_left.pop())

    print('#{}'.format(test_case), end=' ')
    print(*answer)