import sys
sys.stdin = open("3314_input.txt")

T = int(input())

for test_case in range(1, T+1):
    scores = list(map(int, input().split()))

    for i in range(len(scores)):
        if scores[i] < 40:
            scores[i] = 40

    answer = int(sum(scores)/len(scores))
    print(f'#{test_case} {answer}')



# T = int(input())
# for test_case in range(1, T+1):
#     data = list(map(int, input().split()))
#
#     for i in range(len(data)):
#         if data[i] < 40:
#             data[i] = 40
#     print('#{} {}'.format(test_case, int(sum(data)/len(data))))