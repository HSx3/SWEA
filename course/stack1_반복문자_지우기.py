import sys
sys.stdin = open("stack1_반복문자_지우기.txt")

T = int(input())

for test_case in range(1, T+1):
    str = input()
    stack = []

    for i in range(len(str)):
        if len(stack) == 0:
            stack.append(str[i])
        else:
            if stack[len(stack)-1] == str[i]:
                stack.pop()
            else:
                stack.append(str[i])

    print("#{} {}".format(test_case, len(stack)))