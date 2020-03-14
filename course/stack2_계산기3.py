import sys
sys.stdin = open("stack2_계산기3.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = list(input())
    stack = []
    operator = []

    for i in data:
        if i == '(':
            operator.append(i)

        elif i == '*':
            if not operator or operator[-1] != '*':
                operator.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)

        elif i == '+':
            if not operator or operator[-1] == '(':
                operator.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                c = operator.pop()
                if c == '*':
                    stack.append(a*b)
                    operator.append(i)
                else:
                    stack.append(a+b)
                    operator.append(i)

        elif i == ')':
            c = operator.pop()
            while c != '(':
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    stack.append(a+b)
                else:
                    stack.append(a*b)
                c = operator.pop()

        else:
            stack.append(int(i))

    print('#{} {}'.format(test_case, stack[0]))