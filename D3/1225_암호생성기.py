import sys
sys.stdin = open("1225_input.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)

    temp = data
    flag = 1
    while flag != 0:
        if flag == 0:
            break
        for i in range(1, 6):
            # print(f'i={i}')
            # print(f'temp[0]={temp[0]}')
            temp[0] = temp[0]-i
            # print(temp[1:])
            # print(temp[0])
            temp = temp[1:] + [temp[0]]
            # print(f'temp={temp}')
            if temp[-1] <= 0:
                temp[-1] = 0
                flag = 0
                break
    # print(''.join(temp))
    # print(*temp)
    int_to_str = [str(x) for x in temp]
    # print(int_to_str)
    answer = ' '.join(int_to_str)
    print('#{} {}'.format(test_case, answer))