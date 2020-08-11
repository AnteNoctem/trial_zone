import random
import sys
import os

players = int(input('Введите количество игроков (2-4): ',))
if (4 < players) or (2 > players):
    sys.exit('Ты что, дурак?')
SUITS = ['Треф', 'Бубен', 'Червей', 'Пик']
RANKS = ['2-ка', '3-ка', '4-ка', '5-ка', '6-ка', '7-ка', '8-ка', '9-ка','10-ка', 'Валет', 'Дама', 'Король', 'Туз']
deck = []
hand_count = []
hand_sum = 0
rank = random.randrange(0, len(RANKS))
suit = random.randrange(0, len(SUITS))


for  rank in RANKS:
    for suit in SUITS:
        card = rank + ' ' + suit
        deck += [card]
                
deckeys = []
for i in range(52):
    if i < 36:
        deckeys += [2 + i // 4]
    elif i < 48:
        deckeys += [10]
    else:
        deckeys += [11]
        
#игровая колода
DECK = dict(zip(deck, deckeys))

#перетасовка
random.shuffle(deck)

temp_deck = deck[:]

def take_card():
    global hand_count
    global temp_deck
    global hand_sum
    print('Берёшь карту?')
    print('Нажать (1) -> Беру')
    print('Нажать (2) -> Хватит')
    a = input()
    if a == '1':
        print('Беру')
        b = temp_deck.pop()
        hand_count += [b]
        hand_sum += DECK[b]
        print(hand_count)
        print('Ещё?')
        take_card()
    elif a == '2':
        print('Мне хватит.')
        print(hand_count)
        print(hand_sum)
    else:
        print('Дятел, тебе же говорят, выбирай 1 или 2.')
        take_card()
        
def new_round():
    global hand_count
    hand_count = []
    hand_sum = 0
    random.shuffle(deck)
    global temp_deck
    temp_deck = deck[:]
    return

def main_game(x):
    all_sum = []
    global hand_sum
    global hand_count
    for i in range(x):
        print('Ход игрока ', i+1)
        take_card()
        input('Нажмите enter, чтобы продолжить',)
        os.system('cls' if os.name == 'nt' else 'clear')
        all_sum += [hand_sum]
        hand_sum = 0
        hand_count = []
    print('Очки игроков с лева-направо, начиная с первого.')
    print(all_sum)
    input('Нажмите enter, чтобы продолжить',)
    os.system('cls' if os.name == 'nt' else 'clear')
    new_round()       
    main_game(players)

main_game(players)
