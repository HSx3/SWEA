import sys
sys.stdin = open("1493_input.txt")

T = int(input())

for test_case in range(1, T+1):
    p, q = map(int, input().split())
    # p, q = input().split()
    print(p, q)
    print(type(p))

    for i in range(1, 10001):
        i = (i, )