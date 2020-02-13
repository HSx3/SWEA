import sys
sys.stdin = open("string_문자열_비교.txt")

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    print('#{}'.format(test_case), end=' ')

    if str1 in str2:
        print(1)

    else:
        print(0)