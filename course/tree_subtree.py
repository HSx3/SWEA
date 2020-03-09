import sys
sys.stdin = open("tree_subtree.txt")


# 전위
def preorder(start):
    global count
    if start:
        preorder(tree[start][0])
        preorder(tree[start][1])
        count += 1

# 중위
def inorder(start):
    global count
    if start:
        inorder(tree[start][0])
        count += 1
        inorder(tree[start][1])

# 후위
def postorder(start):
    global count
    if start:
        count += 1
        postorder(tree[start][0])
        postorder(tree[start][1])


T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())

    # 노드 번호는 E+1까지 존재 (간선의 개수 + 1)
    tree = [[0 for _ in range(2)] for _ in range(E+2)]
    data = list(map(int, input().split()))

    for i in range(0, len(data), 2):
        if tree[data[i]][0]:
            tree[data[i]][1] = data[i+1]
        else:
            tree[data[i]][0] = data[i+1]

    count = 0
    preorder(N)
    # inorder(N)
    # postorder(N)

    print('#{} {}'.format(test_case, count))