import sys
sys.stdin = open("stack1_그래프_경로.txt")


def DFS(s):
    global G, flag
    stack = []
    stack.append(s)

    while len(stack):
        node = stack.pop()

        if node == G:
            return 1

        if not visited[node]:
            visited[node] = 1
            for w in range(1, V+1):
                if data[node][w] == 1 and visited[w] == 0:
                    stack.append(w)

    return 0


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in range(E):
        u, v = map(int, input().split())
        data[u][v] = 1

    S, G = map(int, input().split())
    visited = [0 for _ in range(V+1)]

    flag = DFS(S)

    print('#{} {}'.format(test_case, flag))