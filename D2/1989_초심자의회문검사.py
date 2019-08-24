import sys
sys.stdin = open("1989_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = input()
    # print(data)

    answer = 1

    for i in range(len(data)):
        if data[i] != data[len(data)-1-i]:
            answer = 0
    print(f'#{test_case} {answer}')