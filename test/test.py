import sys
sys.stdin = open('보물상자비밀번호_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    data = input()

    password_list = []
    basket = ''

    for i in range(N//4):
        for j in range(len(data)):
            if j % (N//4) == (N//4)-1:
                basket += data[j]
                password_list.append(basket)
                basket = ''
            else:
                basket += data[j]
        data = data[-1] + data[0:len(data) - 1]

    password_list = list(set(password_list))
    to10 = []

    for i in password_list:
        i = int(i, 16)
        to10.append(i)

    to10.sort()
    to10.reverse()

    print('#{} {}'.format(test_case, to10[K-1]))