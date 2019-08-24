import sys
sys.stdin = open("1946_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = []
    for i in range(N):
        Ci, Ki = map(str, input().split())
        Ki = int(Ki)
        # print(Ci, Ki)
        for j in range(Ki):
            data.append(Ci)
    # print(data)
    print(f'#{test_case}')
    count = 0
    for k in data:
        print(k, end='')
        count += 1
        if count == 10:
            count = 0
            print()
    print()



# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     print(f'#{test_case}')
#     array = ''
#     for i in range(N):
#         word, times = map(str, input().split())
#         array += word*int(times)
#
#     for i in range(0, len(array), 10):
#         print(array[i:i+10])