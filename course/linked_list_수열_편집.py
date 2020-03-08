import sys
sys.stdin = open("linked_list_수열_편집.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    series = list(map(int, input().split()))

    for i in range(M):
        data = list(input().split())
        if data[0] == 'I':
            series.insert(int(data[1]), int(data[2]))
        elif data[0] == 'D':
            del series[int(data[1])]
        elif data[0] == 'C':
            series[int(data[1])] = int(data[2])

    print('#{}'.format(test_case), end=' ')

    try:
        print(series[L])
    except:                 # except IndexError:
        print(-1)