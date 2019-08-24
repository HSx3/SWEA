import sys
sys.stdin = open("1215_input.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(str, ','.join(input().split()))) for _ in range(8)]
    print(data)

    test = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    a = test[0:4]
    # print(a)
    # print(a[::-1])
    count = 0
    check_col = ''
    for i in range(len(data)-N+1):
        for j in range(len(data)-N+1):
            # print(data[i][j:j+N])
            # print(data[i][j:j+N][::-1])
            # print(data[j][i:i + N])
            # print(data[j][i:i + N][::-1])
            # print(data[j:j+N][i])
            # print(data[j:j+N][i][::-1])
            check_col += data[j][i]
            print(check_col)
            if len(check_col) == N and check_col == check_col[::-1]:
                count += 1
                check_col = ''
            if data[i][j:j+N] == data[i][j:j+N][::-1]:
                count += 1
            # if data[j][i:i+N] == data[j][i:i+N][::-1]:
            #     count += 1
    # for j in range(len(data)-N+1):
    #     for i in range(len(data)-N+1):
    #         if data[j][i:i+N] == data[j][i:i+N][::-1]:
    #             count+=1
    print(count)