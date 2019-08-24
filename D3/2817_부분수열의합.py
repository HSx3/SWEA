import sys
sys.stdin = open("2817_input.txt")

def combination(no):
    global count
    if no >= len(A):
        check_sum = 0
        for i in range(len(A)):
            check_sum += empty_list[i]
        if check_sum == K:
            count += 1
        return

    empty_list[no] = A[no]
    combination(no+1)
    empty_list[no] = 0
    combination(no+1)


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    empty_list = [0]*len(A)
    count = 0
    combination(0)
    print('#{} {}'.format(test_case, count))