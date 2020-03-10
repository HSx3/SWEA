import sys
sys.stdin = open("string_string.txt")

T = 10

for test_case in range(1, T+1):
    tc = int(input())
    keyword = input()
    data = input()
    count = 0

    for i in range(0, len(data)-len(keyword)+1):
        if data[i:i+len(keyword)] == keyword:
            count += 1

    print('#{} {}'.format(test_case, count))
