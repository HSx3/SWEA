import sys
sys.stdin = open("4466_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    sort_scores = sorted(scores, reverse=True)

    choices = 0

    for i in range(K):
        choices += sort_scores[i]

    print('#{} {}'.format(test_case, choices))