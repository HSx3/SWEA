import sys
sys.stdin = open("stack2_계산기2.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = list(input())

    stack = []
    operator = []

    while len(data):
        check = data.pop(0)

        if check == '+' or check == '*':
            operator.append(check)
        else:
            stack.append(int(check))
            if len(stack) >= 2:
                if operator[-1] == '*':
                    b = stack.pop()
                    a = stack.pop()
                    operator.pop()
                    stack.append(a*b)

    print('#{} {}'.format(test_case, sum(stack)))

    # 1 28134
    # 2 195767
    # 3 4293
    # 4 1592
    # 5 477326
    # 6 45647
    # 7 102951
    # 8 6548
    # 9 1394
    # 10 4285
