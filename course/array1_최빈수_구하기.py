import sys
sys.stdin = open("array1_최빈수_구하기.txt")

T = int(input())

for test_case in range(1, T+1):
    tc = int(input())
    scores = list(map(int, input().split()))
    check = [0] * (max(scores)+1)

    for score in scores:
        if check[score]:
            check[score] += 1
        else:
            check[score] = 1

    check = check[::-1]
    print('#{} {}'.format(test_case, len(check)-1-check.index(max(check))))