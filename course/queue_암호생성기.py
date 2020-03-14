import sys
sys.stdin = open("queue_암호생성기.txt")

T = 10

for test_case in range(1, T+1):
    tc = int(input())
    data = list(map(int, input().split()))

    i = 1
    while True:
        if i <= 5:
            if data[0]-i >= 1:
                data = data[1:] + [data[0]-i]

            elif data[0]-i <= 0:
                data = data[1:] + [0]
                break
            i += 1

        elif i > 5:
            i = 1

    print('#{}'.format(test_case), end=' ')
    print(*data)