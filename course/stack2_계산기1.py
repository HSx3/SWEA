import sys
sys.stdin = open("stack2_계산기1.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = list(input())

    stack = []
    plus = []
    answer = 0

    while len(data) != 0:
        check = data.pop(0)

        if check == '+':
            plus.append(check)

        else:
            stack.append(int(check))
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                plus.pop()
                stack.append(a + b)

    print('#{} {}'.format(test_case, stack[0]))

#1 267
#2 197
#3 345
#4 149
#5 149
#6 213
#7 180
#8 221
#9 158
#10 205
