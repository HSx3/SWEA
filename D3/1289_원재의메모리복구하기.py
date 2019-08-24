import sys
sys.stdin = open("1289_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = input()

    N = len(data)
    default = '0'*N

    check = ''
    count = 0
    for i in range(len(data)):
        if data[i] != default[i]:
            if data[i] == '0':
                default = default[0:i] + '0' * (len(data)-i)
                count += 1
            if data[i] == '1':
                default = default[0:i] + '1'*(len(data)-i)
                count += 1
        if default == data:
            print(f'#{test_case} {count}')
            break



# T = int(input())
# for test_case in range(1, T+1):
#     data = list(map(int, input()))
#     # print(data)
#     base = [0] * len(data)
#     # print(base)
#     count = 0
#
#     for i in range(len(base)):
#         if base[i] != data[i]:
#             if data[i] == 1:
#                 for j in range(i, len(base)):
#                     base[j] = 1
#                 count += 1
#             elif data[i] == 0:
#                 for j in range(i, len(base)):
#                     base[j] = 0
#                 count += 1
#     print('#{} {}'.format(test_case, count))