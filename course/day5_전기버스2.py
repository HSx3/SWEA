import sys
sys.stdin = open("day5_전기버스2.txt")

T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    M = data[1:]
    print(N, M)

    check = [1] + [0]*(len(M)-1)
    print(check)
    min_charge_count = 987654321