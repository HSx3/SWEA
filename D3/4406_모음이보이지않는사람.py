import sys
sys.stdin = open("4406_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = input()
    vowel = ['a', 'e', 'i', 'o', 'u']

    answer = ''
    for i in data:
        if i not in vowel:
            answer += i
    print(f'#{test_case} {answer}')



# T = int(input())
# for test_case in range(1, T + 1):
#     data = list(input())
#     answer = ''
#     for i in data:
#         if i not in 'aeiou':
#             answer += i
#     print('#{} {}'.format(test_case, answer))