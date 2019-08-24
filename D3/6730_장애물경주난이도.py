import sys
sys.stdin = open("6730_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    # D1
    D1 = 0
    for i in range(1, len(data)):
        if data[i] - data[i-1] >= D1:
            D1 = data[i] - data[i-1]

    # D2
    D2 = 0
    for i in range(1, len(data)-1):
        if data[i] - data[i+1] >= D2:
            D2 = data[i] - data[i+1]

    print('#{} {} {}'.format(test_case, D1, D2))