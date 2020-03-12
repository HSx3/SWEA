import sys
sys.stdin = open("stack1_괄호_짝짓기.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = list(input())
    stack = []
    left = ['(', '{', '[', '<']
    answer = 1

    while len(data) != 0:
        if data[0] in left:
            stack.append(data.pop(0))
        elif data[0] == ')':
            if stack[-1] != '(':
                answer = 0
                break
            else:
                data.pop(0)
                stack.pop()
        elif data[0] == '}':
            if stack[-1] != '{':
                answer = 0
                break
            else:
                data.pop(0)
                stack.pop()
        elif data[0] == ']':
            if stack[-1] != '[':
                answer = 0
                break
            else:
                data.pop(0)
                stack.pop()
        elif data[0] == '>':
            if stack[-1] != '<':
                answer = 0
                break
            else:
                data.pop(0)
                stack.pop()

    print('#{} {}'.format(test_case, answer))
