import sys
sys.stdin = open("1970_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    check = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = []
    for i in check:
        answer.append(N//i)
        N = N%i

    print(f'#{test_case}')
    print(*answer)