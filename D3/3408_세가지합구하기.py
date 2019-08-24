import sys
sys.stdin = open("3408_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    S1 = N*(N+1)//2
    S2 = N ** 2
    S3 = S1 * 2
    print('#%d %d %d %d'% (test_case, S1, S2, S3))
    # S2 = int(N*(2*1+(N-1)*2)/2)
    # S3 = int(N*(2*2+(N-1)*2)/2)
    # print('#{} {} {} {}'.format(test_case, S1, S2, S3))