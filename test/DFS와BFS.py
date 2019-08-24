import sys
sys.stdin = open('DFS와BFS_input.txt')

def DFS(v):
    visited[v] = 1

    print(v, end=' ')

    # for w in G[v]:
    for w in range(N + 1):
        if G[v][w] == 1 and visited[w] == 0:
            DFS(w)


def BFS(v):
    visited = [0 for _ in range(N + 1)]
    queue = []
    queue.append(v)

    while len(queue) != 0:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in range(N + 1):
                if G[v][w] == 1 and visited[w] == 0:
                    queue.append(w)


N, M, V = map(int, input().split())

# G = [[] for _ in range(N+1)]
G = [[0 for i in range(N+1)] for j in range(N+1)]

visited = [0 for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    # G[u].append(v)
    # G[v].append(u)
    G[u][v] = 1
    G[v][u] = 1

DFS(V)
print()

BFS(V)
print()