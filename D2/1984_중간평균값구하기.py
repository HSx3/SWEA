import sys
sys.stdin = open("1984_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))

    total = sum(data) - max(data) - min(data)
    avg = round(total/(len(data)-2))
    print(f'#{test_case} {avg}')



# T = int(input())
# for test_case in range(1, T+1):
#     data = list(map(int, input().split()))
#
#     for i in range(len(data)-1, 0, -1):
#         for j in range(0, i):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#     answer = sum(data[1:-1])/(len(data)-2)
#     print('#%d %.0f' % (test_case, answer))