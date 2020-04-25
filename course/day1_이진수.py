import sys
sys.stdin = open("day1_이진수.txt")

def Binary(num):
    global result
    share, remainder = 0, 0

    for i in range(4):
        share = num // 2
        remainder = num % 2
        result = str(remainder) + result
        num = share

    return


T = int(input())

hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for test_case in range(1, T+1):
    N, hex = map(str, input().split())

    answer = ''
    for i in hex:
        result = ''
        Binary(hex_to_dec[i])
        answer += result
    print('#{} {}'.format(test_case, answer))