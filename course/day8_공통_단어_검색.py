import sys
sys.stdin = open("day8_공통_단어_검색.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    print('#{} {}'.format(test_case, len(set(A) & set(B))))