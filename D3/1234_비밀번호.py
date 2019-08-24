import sys
sys.stdin = open("1234_input.txt")

T = 10

for test_case in range(1, T+1):
    N, password = map(str, input().split())
    # print(N, password)

    password = list(password)
    # print(password)
    # temp = password
    flag = 1
    while flag != 0:
        # print(f'New {password}')
        temp = password
        flag = 0
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                delete_number = password[i]
                # temp.remove(delete_number)
                del temp[i]
                # print(temp)
                # temp.remove(delete_number)
                del temp[i]
                # print(temp)
                password = temp
                flag = 1
                break

    print(f'#{test_case}', end=' ')
    print(''.join(password))