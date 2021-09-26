import random
suits = (1,2,3,4,5,6,7,8,9,10,11,12,13)
ranks = ('Heart','Diamond','Spade','Club')

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit} of {self.rank}'

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_deck = Card(suit,rank)
                self.deck.append(new_deck)

    def rearrange(self):
        random.shuffle(self.deck)

    def remove(self):
        return self.deck.pop(0)

class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f'Hello {self.name}. You have {len(self.cards)} cards left'

    def remove_card(self):
        return self.cards.pop(0)

    def add_card(self,new):
        if type(new) == type([]):
            self.cards.extend(new)
        else:
            self.cards.append(new)

def tie():
    while True:
        try:
            player1_try = int(input('Player 1 Enter an Index from 0 to 2 to select a card:  '))
            player2_try = int(input('Player 2 Enter an Index from 0 to 2 to select a card:  '))
        except:
            print('Enter an Integer from 0 to 2')
        else:
            if player1_try in [0, 1, 2] and player2_try in [0, 1, 2]:
                break
            else:
                continue
    return player1_try,player2_try

card_list = Deck()
card_list.rearrange()
player1 = Player('D')
player2 = Player('S')
for i in range(26):
    player1.add_card(card_list.remove())
    player2.add_card(card_list.remove())

print(player1.cards[0].suit)

round = 0
game_on = True

while game_on:
    round += 1
    if len(player1.cards)==0:
        print("Player 1 is out of cards")
        print('Player 2 won!!')
        print(f'It took {round} times to finish the game')
        game_on = False
        break


    if len(player2.cards)==0:
        print("Player 2 is out of cards")
        print('Player 1 won!!')
        print(f'It took {round} times to finish the game')
        game_on = False
        break

    player1_cards = []
    player1_cards.append(player1.remove_card())
    player2_cards = []
    player2_cards.append(player2.remove_card())

    war_game = True

    while war_game:
        if player1_cards[-1].suit > player2_cards[-1].suit:
            player1.cards.append(player1_cards[-1])
            player1.cards.append(player2_cards[-1])
            print(f'{player1_cards[-1].suit} > {player2_cards[-1].suit}')
            print('Player 1 wins this round')
            print(f'Player 1 has {len(player1.cards)} cards left and Player 2 has {len(player2.cards)} cards left')
            war_game = False

        elif player2_cards[-1].suit > player1_cards[-1].suit:
            player2.cards.append(player2_cards[-1])
            player2.cards.append(player1_cards[-1])
            print(f'{player2_cards[-1].suit} > {player1_cards[-1].suit}')
            print('Player 2 wins this round')
            print(f'Player 2 has {len(player2.cards)} cards left and Player 1 has {len(player1.cards)} cards left')
            war_game = False

        else:
            print('Suits are the same')
            if len(player1.cards) > 3 and len(player2.cards) > 3:
                p_1 = []
                p_2 = []

                for i in range(3):
                    p_1.append(player1.remove_card())
                    p_2.append(player2.remove_card())

                player1_try,player2_try = tie()

                if p_1[player1_try].suit > p_2[player2_try].suit:
                    player1.cards.append(p_1[0])
                    player1.cards.append(p_1[1])
                    player1.cards.append(p_1[2])
                    player1.cards.append(p_2[0])
                    player1.cards.append(p_2[1])
                    player1.cards.append(p_2[2])
                    player1.cards.append(player1_cards[-1])
                    player1.cards.append(player2_cards[-1])
                    print('Player 1 wins this round')
                    print(f'Player 1 has {len(player1.cards)} and Player 2 has {len(player2.cards)} cards')
                    war_game = False
                    break

                elif p_2[player2_try].suit > p_1[player1_try].suit:
                    player2.cards.append(p_1[0])
                    player2.cards.append(p_1[1])
                    player2.cards.append(p_1[2])
                    player2.cards.append(p_2[0])
                    player2.cards.append(p_2[1])
                    player2.cards.append(p_2[2])
                    player2.cards.append(player1_cards[-1])
                    player2.cards.append(player2_cards[-1])
                    print('Player 2 wins this round')
                    print(f'Player 2 has {len(player2.cards)} and Player 1 has {len(player1.cards)}')
                    war_game = False
                    break

                else:
                    player1_try, player2_try = tie()
                    continue
            else:
                if len(player1.cards) < 3:
                    print('Player 1 does not have enough cards to continue')
                    print('Player 2 won!!')
                    print(f'It took {round} times to finish the game')
                    war_game = False
                    break
                else:
                    print('Player 2 does not have enough cards to continue')
                    print('Player 1 won!!')
                    print(f'It took {round} times to finish the game')
                    war_game = False
                    break