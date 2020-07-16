import sys
sys.stdin = open("day8_접두어_검색.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    check = [0]*len(B)

    for prefix in B:
        for word in A:
            if prefix + word[len(prefix):] == word:
                check[B.index(prefix)] = 1
                break

    print('#{} {}'.format(test_case, sum(check)))