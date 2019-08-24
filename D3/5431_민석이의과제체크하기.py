import sys
sys.stdin = open("5431_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    submit_list = list(map(int, input().split()))

    students = list(range(1, N+1))
    check = []

    for i in range(len(submit_list)):
        students.remove(submit_list[i])
    print('#{}'.format(test_case), end=' ')
    print(*students)


# for i in range(1, T+1):
#     total, cnt = map(int, input().split())
#     num_list = set(map(int, input().split()))
#     total_list = set(range(1, total+1))
#     print(f'#{i+1}', end=' ')
#     print(' '.join(map(str, total_list - num_list)))