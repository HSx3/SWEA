import sys
sys.stdin = open("1228_input.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    original = list(map(int, input().split()))
    num_of_command = int(input())
    command_i, command_x, command_y, command_s = map(str, input().split())
    print(command_s)