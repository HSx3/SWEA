import sys
sys.stdin = open("stack1_괄호검사.txt")

T = int(input())

for test_case in range(1, T+1):
    words = input()

    parenthesis = ['[', '{', '(', ']', '}', ')']
    check = []
    flag = 1

    for word in words:
        if word not in parenthesis:
            continue
        elif word == '[':
            check.append(word)
        elif word == '{':
            check.append(word)
        elif word == '(':
            check.append(word)
        elif word == ']':
            if len(check) >= 1 and check[-1] == '[':
                check.pop()
            else:
                flag = 0
                break
        elif word == '}':
            if len(check) >= 1 and check[-1] == '{':
                check.pop()
            else:
                flag = 0
                break
        elif word == ')':
            if len(check) >= 1 and check[-1] == '(':
                check.pop()
            else:
                flag = 0
                break
        else:
            break

    print('#{}'.format(test_case), end=' ')
    if flag == 0:
        print(0)
    elif flag == 1:
        if len(check) == 0:
            print(1)
        else:
            print(0)
