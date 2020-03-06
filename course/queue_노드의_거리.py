import sys
sys.stdin = open("queue_노드의_거리.txt")


def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1

    while len(queue) != 0:
        t = queue.pop(0)

        if t == G:
            return visited[t] - 1

        for w in range(V+1):
            if data[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1

    return 0



T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0] * (V + 1)
    print(data)

    for i in range(E):
        u, v = map(int, input().split())
        data[u][v] = 1
        data[v][u] = 1

    print(data)

    S, G = map(int, input().split())

    print('#{} {}'.format(test_case, BFS(S)))


