import sys
sys.stdin = open("1926_input.txt")

N = int(input())
data = list(range(1, N+1))

check = ['3', '6', '9']
answer = []

for i in data:
    temp = ''
    for j in str(i):
        if j not in check:
            temp+=j
        if j in check:
            temp+='-'
    if temp.count('-') == 1:
        temp = '-'
    answer.append(temp)
print(*answer)


# N = int(input())
# for i in range(1, N+1):
#     i = str(i)
#     clap = i.count('3') + i.count('6') + i.count('9')
#     if clap > 0:
#         i = '-'* clap
#     print(i, end=' ')