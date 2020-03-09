import sys
sys.stdin = open("tree_노드의_합.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]

    for i in range(M):
        node, number = list(map(int, input().split()))
        tree[node] = number

    # N이 짝수인 경우, 자식이 하나 => 부모 값 = 자식 값
    if N % 2 == 0:
        tree[N//2] = tree[N]
        N -= 1  # N을 부모 값으로

    while N > 1:
        tree[N//2] = tree[N] + tree[N-1]
        N -= 2  # N을 부모 값으로

    print('#{} {}'.format(test_case, tree[L]))