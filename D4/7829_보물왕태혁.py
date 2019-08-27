import sys
sys.stdin = open('7829_input.txt')

T = int(input())

for test_case in range(1, T+1):
    P = int(input())
    divisors = list(map(int, input().split()))

    print('#{}'.format(test_case), end=' ')
    if P != 1:
        divisors.sort()
        print(divisors[0] * divisors[-1])
    else:
        print(divisors[0]**2)