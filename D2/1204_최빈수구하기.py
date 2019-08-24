import sys
sys.stdin = open("1204_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    check = [0]*101
    for i in score:
        check[i] += 1
    answer = []
    for idx, count in enumerate(check):
        if count == max(check):
            answer.append(idx)
    print(f'#{test_case} {max(answer)}')



# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     check = {}
#     for i in data:
#         if i in check:
#             check[i] += 1
#         else:
#             check[i] = 1
#     answer = []
#     for idx, value in enumerate(check):
#         if check[value] == max(check.values()):
#             answer.append(value)
#     print(f'#{N} {sorted(answer)[-1]}')