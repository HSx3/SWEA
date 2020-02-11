import sys
sys.stdin = open("특이한자석_input.txt")


T = int(input())

# for test_case in range(1, T+1):
for test_case in range(1):
    K = int(input())
    coil = []
    coil1 = input().split()
    coil.append(coil1)
    coil2 = input().split()
    coil.append(coil2)
    coil3 = input().split()
    coil.append(coil3)
    coil4 = input().split()
    coil.append(coil4)

    print(coil)

    # lotation_info = [input().split() for _ in range(K)]
    lotation_info = []
    for i in range(K):
        rotation_coil, rotation_direction = map(int, input().split())
        lotation_info.append((rotation_coil, rotation_direction))
    print('lotation_info', lotation_info)

    for i in range(K):
        # 이웃자석 체크
        check = [0, 0, 0]
        if coil[0][2] != coil[1][6]:
            check[0] = 1
        if coil[1][2] != coil[2][6]:
            check[1] = 1
        if coil[2][2] != coil[3][6]:
            check[2] = 1
        # check.insert(lotation_info[i][0]-1, 0)
        print('check', check)




        # 자석 회전
        if lotation_info[i][1] == 1:    # 회전정보의 i번째 자석의 방향이 시계방향이면
            # print(lotation_info[i][0])
            # 회전정보의 자석을 시계방향으로 회전
            coil[lotation_info[i][0]-1] = [coil[lotation_info[i][0]-1][-1]] + coil[lotation_info[i][0]-1][0:7]
            # temp = [coil[lotation_info[i][0]-1][-1]] + coil[lotation_info[i][0]-1][0:7]
            print('시계방향돌린자석', coil[lotation_info[i][0]-1])



            # 이웃 자석 회전
            # side(lotation_info[i][0], lotation_info[i][1], check)

                        # coil[lotation_info[i][0]] = coil[lotation_info[i][0]][1:8] + [coil[lotation_info[i][0]][0]]

            coil_check = [0, 1, 2, 3]
            coil_check.remove(lotation_info[i][1]-1)
            if lotation_info[i][0] == 1 or lotation_info[i][0] == 2:
                for j in coil_check:
                    if coil[0][2] != coil[1][6]:
                        coil[j] = coil[j][1:8] + coil[j][0]




        else:       # 반시계방향
            coil[lotation_info[i][0]-1] = coil[lotation_info[i][0]-1][1:8] + [coil[lotation_info[i][0]-1][0]]
            print('반시계방향돌린자석', coil[lotation_info[i][0]-1])

            # 이웃 자석 회전
            # for j in range(len(check)):



# coil[1] = coil[1][1:8] + [coil[1][0]]
# coil[2] = [coil[2][-1]] + coil[2][0:7]