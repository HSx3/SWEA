import sys
sys.stdin = open("1976_input.txt")

T = int(input())

for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1+h2
    if h > 12:
        h = h-12
    m = m1+m2
    if m1+m2 >= 60:
        m = m1+m2-60
        h += 1
    print(f'#{test_case} {h} {m}')



# T = int(input())
# for test_case in range(1, T+1):
#     data = list(map(int, input().split()))
#     if data[1] + data[3] >= 60:
#         answer_h = data[0] + data[2] + 1
#         answer_m = data[1] + data[3] - 60
#     else:
#         answer_h = data[0] + data[2]
#         answer_m = data[1] + data[3]
#     if answer_h > 12:
#         answer_h -= 12
#     print(f'#{test_case} {answer_h} {answer_m}')