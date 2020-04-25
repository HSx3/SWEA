import sys
sys.stdin = open("day1_이진수2.txt")

def Binary(n):
    global answer, count
    while True:
        if count > 13:
            answer = 'overflow'
            return

        check_n = n * 2

        if check_n - int(check_n):
            answer += str(int(check_n))
            count += 1
            n = check_n - int(check_n)

        else:
            answer += str(int(check_n))
            count += 1
            return


T = int(input())

for test_case in range(1, T+1):
    N = float(input())
    answer = ''
    count = 0
    Binary(N)

    print('#{} {}'.format(test_case, answer))