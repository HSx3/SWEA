import sys
sys.stdin = open("day3_베이비진_게임.txt")


def check_run(cards, player):
    global winner
    if len(cards) < 3:
        return
    else:
        sorted_cards = sorted(list(set(cards)))
        for card in sorted_cards:
            if cards.count(card) == 3:
                winner = player
                return

def check_triplet(cards, player):
    global winner
    if len(cards) < 3 or len(set(cards)) < 3:
        return
    else:
        cards = sorted(list(set(cards)))
        for i in range(len(cards)-2):
            if cards[i+1] - cards[i] == 1 and cards[i+2] - cards[i+1] == 1:
                winner = player
                return


T = int(input())

for test_case in range(1, T+1):
    card = list(map(int, input().split()))

    winner = 0
    p1 = []
    p2 = []

    while len(card) != 0:
        p1.append(card.pop(0))

        check_run(p1, 1)
        if winner != 0:
            break

        check_triplet(p1, 1)
        if winner != 0:
            break

        p2.append(card.pop(0))

        check_run(p2, 2)
        if winner != 0:
            break

        check_triplet(p2, 2)
        if winner != 0:
            break

    print('#{} {}'.format(test_case, winner))