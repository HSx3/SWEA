import sys
sys.stdin = open("day5_전기버스2.txt")


def DFS(k, n):
    global min_charge_count
    if k >= n:
        battery = M[0]
        charge_count = 0

        if sum(check) >= min_charge_count:
            return

        if sum(check) == 0:
            return

        for i in range(len(check)):
            battery -= 1
            if check[i] == 1 and battery >= 0:
                battery += M[i+1]
                charge_count += 1

            if battery < 0:
                return

        if battery >= 1 and min_charge_count >= charge_count:
            min_charge_count = charge_count
        return

    else:
        check[k] = 1
        DFS(k+1, n)
        check[k] = 0
        DFS(k+1, n)


T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    M = data[1:]

    check = [0]*(len(M)-1)
    min_charge_count = 987654321

    DFS(0, len(check))    # k, n, battery
    print('#{} {}'.format(test_case, min_charge_count))