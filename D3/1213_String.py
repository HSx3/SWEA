import sys
sys.stdin = open("1213_input.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    keyword = input()
    data = input()

    count = 0
    for i in range(len(data)-len(keyword)+1):
        if data[i:i+len(keyword)] == keyword:
            count += 1
    print('#{} {}'.format(test_case, count))



# T = 10
# for test_case in range(1, T+1):
#     N = int(input())
#     keyword = list(input())
#     words = list(input())
#
#     count = 0
#     for i in range(len(words)):
#         if words[i:i+len(keyword)] == keyword:
#             count += 1
#     print('#{} {}'.format(test_case, count))