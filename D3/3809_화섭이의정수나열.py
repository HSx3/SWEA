import sys
sys.stdin = open("3809_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))