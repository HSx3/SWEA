import sys
sys.stdin = open("5549_input.txt")

T = int(input())

for test_case in range(1, T+1):
    number = int(input())

    answer = 'Odd'
    if number % 2 == 0:
        answer = 'Even'

    print('#{} {}'.format(test_case, answer))