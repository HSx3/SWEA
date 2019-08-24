import sys
sys.stdin = open("4676_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = list(input())
    H = int(input())
    hyphen = list(map(int, input().split()))

    temp = data + ['']
    count = 0
    check = []

    for i in hyphen:
        temp[i] = '-'+temp[i]
    print('#{} {}'.format(test_case, ''.join(temp)))

