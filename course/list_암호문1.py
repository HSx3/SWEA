import sys
sys.stdin = open("list_암호문1.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    code = list(map(int, input().split()))
    command_N = int(input())
    command = []

    for _ in input().split():
        if not _.isdigit():
            command.append(_)
        else:
            command.append(int(_))

    i = 0
    while i < len(command):
        if command[i] == 'I':
            i += 1
            idx = command[i]

            i += 1
            count = command[i]
            temp = []

            while count > 0:
                i += 1
                temp.append(command[i])
                count -= 1

            i += 1
            code = code[:idx] + temp + code[idx:]

    print('#{}'.format(test_case), end=' ')
    print(*code[:10])
