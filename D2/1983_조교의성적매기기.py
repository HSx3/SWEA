import sys
sys.stdin = open("1983_input.txt")

import math

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # print(N, K)

    score_list = []
    grade_list = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)

    for i in range(len(data)):
        score = 0.35*data[i][0] + 0.45*data[i][1] + 0.20*data[i][2]
        score_list.append(score)
    # print(score_list)

    student_score = score_list[K-1]
    ranking = sorted(score_list).index(student_score)
    # print(ranking)
    grade = math.ceil((((ranking + 1) / N * 10) - 1))
    # print(grade)
    print(f"#{test_case} {grade_list[grade]}")



# T = int(input())
# for tc in range(T):
#     N, S = map(int, input().split())
#     arr = [[0 for _ in range(5)] for _ in range(N)]  # 번호 과목1 과목2 과목3 총점 등수 성적
#     grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
#     for i in range(N):
#         arr[i] = [i + 1] + list(map(int, input().split()))
#         arr[i].append(arr[i][1] * 0.35 + arr[i][2] * 0.45 + arr[i][3] * 0.20)
#     arr.sort(key=lambda a: (a[4]), reverse=True)
#
#     cnt = 0
#     for i in range(10):
#         for j in range(N // 10):
#             arr[cnt].append(grade[i])
#             cnt += 1
#
#     for i in range(N):
#         if arr[i][0] == S:
#             ans = arr[i][5]
#     print("#{} {}".format(tc + 1, ans))