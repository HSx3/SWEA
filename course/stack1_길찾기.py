import sys
sys.stdin = open("stack1_길찾기.txt")


def find(v):
    global answer, visited
    stack = []
    stack.append(v)

    while len(stack) != 0:
        v = stack.pop()

        if v == 99:
            answer = 1
            return

        if visited_1[v] != 0 and visited[v] != 0:
            visited[v] -= 1
            stack.append(visited_1[v])

        if visited_2[v] != 0 and visited[v] != 0:
            visited[v] -= 1
            stack.append(visited_2[v])



T = 10

for test_case in range(1, T+1):
    tc, N = map(int, input().split())
    data = list(map(int, input().split()))

    answer = 0
    visited = [0]*100
    visited_1 = [0]*100
    visited_2 = [0]*100

    for i in range(0, len(data), 2):
        if visited_1[data[i]]:
            visited_2[data[i]] = data[i+1]
            visited[data[i]] += 1
        else:
            visited_1[data[i]] = data[i+1]
            visited[data[i]] += 1

    find(0)
    print('#{} {}'.format(test_case, answer))


#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 0
#9 0
#10 0
