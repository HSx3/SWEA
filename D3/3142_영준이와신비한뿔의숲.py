import sys
sys.stdin = open("3142_input.txt")

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    y = n-m
    x = m-y
    print('#{} {} {}'.format(test_case, x, y))



# T = int(input())
# for case in range(1, T + 1):
#     n, m = map(int, input().split())
#     # 뿔이 한 개 달린 유니콘과 뿔이 두 개 달린 트윈혼
#     # n - 뿔, m - 짐승 수
#     twin = 0
#     uni = 0
#     for i in range(0, m + 1):
#         if i * 2 + (m - i) == n:
#             twin = i
#             uni = m - i
#             break
#
#     print(f"#{case} {uni} {twin}")