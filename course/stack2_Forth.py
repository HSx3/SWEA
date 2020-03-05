import sys
sys.stdin = open("stack2_Forth.txt")


def calc(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    else:
        return a//b


T = int(input())

for test_case in range(1, T+1):
    data = list(map(str, input().split()))
    stack = []

    for i in range(len(data)):
        if data[i].isdigit():
            stack.append(int(data[i]))
        elif not data[i].isdigit():
            if data[i] == '.':
                if len(stack) != 1:
                    answer = 'error'
                    break
                else:
                    answer = stack[0]
                    break

            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                value = calc(a, b, data[i])
                stack.append(value)
            else:
                answer = 'error'
                break

    print('#{} {}'.format(test_case, answer))