import sys
sys.stdin = open("day5_전기버스2.txt")


def DFS(n):
    global charge_count, min_charge_count

    if n >= N:
        if min_charge_count > charge_count:
            min_charge_count = charge_count
        return

    if min_charge_count < charge_count:
        return

    start = n
    battery = data[start]

    for i in range(start+battery, start, -1):
        charge_count += 1
        DFS(i)
        charge_count -= 1


T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]

    min_charge_count = 987654321
    charge_count = 0

    DFS(1)    # n
    print('#{} {}'.format(test_case, min_charge_count-1))