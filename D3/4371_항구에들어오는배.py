import sys
sys.stdin = open("4371_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    happydays = []
    for i in range(N):
        data = int(input())
        happydays.append(data)
    print(happydays)