import sys
sys.stdin = open("day2_전자카트.txt")

import itertools

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    numbers = list(range(1, N))
    perm = list(itertools.permutations(numbers, N-1))

    min_consumption = 987654321

    for i in range(len(perm)):
        consumption = 0
        root = perm[i]

        consumption += e[0][root[0]]
        consumption += e[root[-1]][0]

        j = 0
        while j != len(root)-1:
            consumption += e[root[j]][root[j+1]]
            j += 1

        if consumption <= min_consumption:
            min_consumption = consumption

    print('#{} {}'.format(test_case, min_consumption))
