import sys
sys.stdin = open("list1_전기버스.txt")

T = int(input())

for test_case in range(1, T+1):
    # K : 최대 이동거리 // N : 종점 번호 // M : 정류장 개수
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))

    bus_stop = list(range(N+1))
    recharge = 0
    location = 0
    flag = 0

    for i in range(len(data)-1):
        if abs(data[i] - data[i+1]) > K and flag == 0:
            flag = 1
            break

    if flag == 1:
        print('#{} {}'.format(test_case, 0))
        continue

    while flag != 1:
        location += 1
        check = bus_stop[location:location+K]

        for j in check[::-1]:
            if j in data:
                location = j
                recharge += 1
                break

        if location + K >= N:
            flag = 1
            break

    if flag == 1:
        print('#{} {}'.format(test_case, recharge))

    # elif flag == 0:
    #     print('#{} {}'.format(test_case, 0))