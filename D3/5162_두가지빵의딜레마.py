import sys
sys.stdin = open("5162_input.txt")

T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())

    A_only = C//A
    B_only = C//B
    answer = max(A_only, B_only)

    print('#{} {}'.format(test_case, answer))