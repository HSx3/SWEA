import sys
sys.stdin = open('1218_input.txt')

T = 10

brace = ['(', ')', '[', ']', '{', '}', '<', '>']
check_open = ['(', '[', '{', '<']
check_close = [')', ']', '}', '>']
for test_case in range(1, T+1):
    length = int(input())
    data = list(input())

    answer = 1
    print('#{}'.format(test_case), end=' ')

    # 여는 괄호 / 닫는 괄호 개수가 다른 경우
    for i in range(0, 2, len(brace)):
        if data.count(brace[i]) != data.count(brace[i+1]):
            answer = 0
            break

    # 순서가 틀린 경우
    left = []
    while len(data) != 0:
        a = data.pop(0)
        if a in check_open:
            left.append(a)
        elif a in check_close:
            if check_open.index(left.pop()) != check_close.index(a):
                answer = 0
                break
    print(answer)