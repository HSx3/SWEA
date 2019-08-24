import sys
sys.stdin = open("3456_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))

    for i in data:
        if data.count(i) == 1 or data.count(i) == 3:
            answer = i
            break
    print('#{} {}'.format(test_case, answer))

    # check = [0]*101
    # for i in data:
    #     check[i+1] += 1
    #
    # for j in check:
    #     if j == 1 or j == 3:
    #         answer = check.index(j)-1
    #         break



# T = int(input())
# for test_case in range(1, T+1):
#     data = list(map(int, input().split()))
#
#     for i in data:
#         if data.count(i) == 1 or data.count(i) == 3:
#             answer = i
#             break
#     print('#{} {}'.format(test_case, answer))