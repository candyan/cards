#-*-coding:utf-8
import random

own_cards_num = 26    #max:26

def main():
    all_cards = range(52)
    
    playerA = random.sample(all_cards, own_cards_num)
    all_cards = list(set(all_cards) - set(playerA))
    playerB = random.sample(all_cards, own_cards_num)

    now_player = []
    game_queue = []

    for num in xrange(own_cards_num):
        playerA[num] = playerA[num] % 13
        playerB[num] = playerB[num] % 13

    print "PlayerA: "
    print playerA
    print '\n'
    print "PlayerB: "
    print playerB
    print '\n'

    all_steps = 0

    while playerA != [] and playerB != []:
        all_steps += 1
        if all_steps % 2 == 1:
            now_player = playerA
        else:
            now_player = playerB

        while True:
            card = now_player.pop(0)
            if card in game_queue:
                same_card_index = game_queue.index(card)
                harvest_list = game_queue[same_card_index:]
                now_player.extend(harvest_list)
                now_player.append(card)
                game_queue = list(set(game_queue) - set(harvest_list))
            else:
                game_queue.append(card)
                break
    print all_steps
    if playerA == []:
        print "playerB win"
    else:
        print "playerA win"

if __name__ == "__main__":
    main()

