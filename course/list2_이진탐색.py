import sys
sys.stdin = open("list2_이진탐색.txt")


def binary_search_A(P, Pa, Pb, l, r, c):
    count_a = 1
    while c != Pa:
        if Pa > c:
            l = c
            c = int((l+r) / 2)
            count_a += 1

        elif Pa < c:
            r = c
            c = int((l+r) / 2)
            count_a += 1

        elif Pa == c:
            return count_a

    return count_a


def binary_search_B(P, Pa, Pb, l, r, c):
    count_b = 1
    while c != Pb:
        if Pb > c:
            l = c
            c = int((l+r) / 2)
            count_b += 1

        elif Pb < c:
            r = c
            c = int((l+r) / 2)
            count_b += 1

        elif Pb == c:
            return count_b

    return count_b


T = int(input())

for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    l = 1
    r = P
    c = int((l+r) / 2)

    A = binary_search_A(P, Pa, Pb, l, r, c)
    B = binary_search_B(P, Pa, Pb, l, r, c)

    print('#{}'.format(test_case), end=' ')
    if A < B:
        print('A')
    elif A > B:
        print('B')
    else:
        print(0)