import sys
sys.stdin = open("5356_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = []
    for i in range(5):
        word = input()
        if len(word) <= 15:
            check_len = 15 - len(word)
            data.append(list(word)+['']*check_len)

    answer = ''
    for i in range(15):
        for j in range(5):
            answer += data[j][i]
    print('#{} {}'.format(test_case, answer))
