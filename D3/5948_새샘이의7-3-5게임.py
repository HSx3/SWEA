import sys
sys.stdin = open("5948_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))

    answer = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                check = data[i]+data[j]+data[k]
                if check not in answer:
                    answer.append(check)

    print('#{}'.format(test_case), end=' ')
    print(list(reversed(sorted(answer)))[4])