import sys
sys.stdin = open("4047_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = input()
    cards = []
    for i in range(0, len(data), 3):
        cards.append(data[i:i+3])

    S, D, H, C = 13, 13, 13, 13
    if len(cards) != len(set(cards)):
        print('#{} {}'.format(test_case, 'ERROR'))
    else:
        for i in cards:
            if i[0] == 'S':
                S -= 1
            elif i[0] == 'D':
                D -= 1
            elif i[0] == 'H':
                H -= 1
            else:
                C -= 1
        print('#{}'.format(test_case), end=' ')
        print(S, D, H, C)