import sys
sys.stdin = open("2005_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = [[0]*i for i in range(1, N+1)]
    # print(data)

    for i in range(len(data)):
        data[i][0] = 1
        data[i][-1] = 1
    for i in range(2, len(data)):
        for j in range(1, len(data)-1):
            data[i][j] = data[i-1][j-1] + data[i-1][j]

    print(data)



    # 출력
    for i in range(len(data)):
        print(*data[i])