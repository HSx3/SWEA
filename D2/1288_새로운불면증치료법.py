import sys
sys.stdin = open("1288_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # print(N)

    check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    check_list = []

    count = 0

    while len(check_list) != 10:
        count += 1
        for i in str(count*N):
            # print(f'count*N = {count*N}', end=' ')
            if i not in check_list:
                check_list.append(i)
                # print(check_list)
    print(f'#{test_case} {count*N}')

