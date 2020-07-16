import sys
sys.stdin = open("day8_부분_문자열.txt")

T = int(input())

for test_case in range(1, T+1):
    N, word = map(str, input().split())
    N = int(N)
    substr = []

    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            if word[i:j] not in substr:
                substr.append(word[i:j])

    substr = sorted(substr)
    print('#{} {} {}'.format(test_case, substr[N-1][0], len(substr[N-1])))

# Suffix Array 참고