import sys
sys.stdin = open("stack1_종이붙이기.txt")

T = int(input())

m = [1, 1]                          # f(0) = 1, f(1) = 1
for i in range(2, 31):
    m.append(m[i-1] + 2*m[i-2])     # 점화식 f(n) = f(n-1) + 2*f(n-2)

for tc in range (1, T+1):
    N = int(input())//10
    print('#{} {}'.format(tc, m[N]))