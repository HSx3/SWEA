import sys
sys.stdin = open("string_글자수.txt")

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    set_str1 = set(str1)

    max_count = 0
    for i in set_str1:
        if str2.count(i) >= max_count:
            max_count = str2.count(i)

    print('#{} {}'.format(test_case, max_count))