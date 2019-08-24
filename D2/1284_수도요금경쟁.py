import sys
sys.stdin = open("1284_input.txt")

T = int(input())

for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    # print(P, Q, R, S, W)

    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + S * (W-R)

    if A > B:
        answer = B
    else:
        answer = A
    print(f'#{test_case} {answer}')