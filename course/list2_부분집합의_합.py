import sys
sys.stdin = open("list2_부분집합의_합.txt")

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # data = list(range(1, N+1))
    data = list(range(1, 13))
    # print(data)

    n = len(data)

    for i in range(1<<n):
        count = 0
        check_sum = 0
        time = 0
        for j in range(n):
            if i&(1<<j):
                check_sum += data[j]
                time += 1
            if time == N and check_sum == K:
                count += 1


    print('#{} {}'.format(test_case, count))



# TC  = int(input())
# num = [1,2,3,4,5,6,7,8,9,10,11,12]
# Len = len(num)
#
# #부분집합 구하기
# lst = []
# for i in range(1<<Len):
#     sub_lst = []
#     for j in range(Len):
#         if i & (1<<j):
#             sub_lst.append(num[j])
#     lst.append(sub_lst)
#
# print(lst)
#
#
# for tc in range(1, TC+1):
#     N, K = map(int, input().split())
#
#     #길이 맞는 리스트 구하기
#     len_lst = []
#     for i in lst:
#         if len(i) == N:
#             len_lst.append(i)
#
#
#     #합 일치 유무 확인
#     result = 0
#     for i in len_lst:
#         if sum(i) == K:
#             result += 1
#
#     print('#%s %d'%(tc, result))