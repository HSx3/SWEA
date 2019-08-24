import sys
sys.stdin = open("1221_input.txt")

T = int(input())

for test_case in range(1, T+1):
    case_number, counts = map(str, input().split())
    data = list(map(str, input().split()))

    check = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    answer = []
    for i in check:
        answer.append((' '+i)*data.count(i))
    print('#{}'.format(test_case), end='')
    print(*answer)



# num_list = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
# for t in range(int(input())):
#     idx, num = input().split()
#     line = input()
#     res = ''
#     for i in num_list:
#         res += (i+' ')*line.count(i)
#     print('%s\n%s' %(idx, res))