import sys
sys.stdin = open("string_회문2.txt")


def check(data):
    global max_pal
    z = 1
    while z < 100:
        for i in range(100):
            for j in range(100 - z + 1):
                if data[i][j:j + z] == data[i][j:j + z][::-1]:
                    if max_pal <= len(data[i][j:j + z]):
                        max_pal = len(data[i][j:j + z])

        z += 1


T = 10

for test_case in range(1, T+1):
    tc = int(input())
    data = [list(input()) for _ in range(100)]
    max_pal = 0
    check(data)

    # data = list(zip(*data))
    for i in range(100):
        for j in range(100):
            if i < j:
                data[i][j], data[j][i] = data[j][i], data[i][j]

    check(data)

    print('#{} {}'.format(test_case, max_pal))



# def check(data):
#     global max_pal
#     z = 1
#     while z < 100:
#         for i in range(100):
#             for j in range(100 - z + 1):
#                 # print('?', data[i][j:j+z], data[i][j:j+z][::-1])
#                 # 가로
#                 if data[i][j:j + z] == data[i][j:j + z][::-1]:
#                     if max_pal <= len(data[i][j:j + z]):
#                         max_pal = len(data[i][j:j + z])
#                 # 세로
#                 col = ''
#                 for k in range(j, j + z):
#                     # print('k, i', k, i)
#                     col += data[k][i]
#                 # print('k, i, data[k][i]', k, i, data[k][i])
#                 # print('col', col)
#                 if col == col[::-1]:
#                     # if len(col) >= 13:
#                     #     # print('col', col)
#                     if max_pal <= len(col):
#                         max_pal = len(col)
#
#         z += 1