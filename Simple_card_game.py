import random


def create_deck(deck, meaning, suit):
  for i in suit:
    for j in meaning:
      deck.append(i + j)


def fill_cards_players(player, deck, count_cards):
  if len(deck) > 0:
    for i in range(count_cards):
      tmp_cards = random.choice(deck)
      player.append(tmp_cards)
      deck.remove(tmp_cards)


def user_hod(player, table):
  if len(player) > 0:
    while True:
      user = input('user:')
      if user in player:
        table.append(user)
        player.remove(user)
        break
  else:
    print('no cards user')


def bot_hod(player, table):
  if len(player) > 0:
    tmp = random.choice(player)
    table.append(tmp)
    player.remove(tmp)

def trump_count(player, player_name, count):
    count = []
    for i in range(len(player)):
        if player[i][0] == trump:
            count.append(trump)
    print(f"Player {player_name} has {len(count)} trump cards")
    return count


# def trump_check(user, bot1, bot2, bot3, meaning, values):
#   general = user + bot1 + bot2 + bot3
#   trump_cards = []
#   for i in general:
#       suit = i[0]
#       if suit == trump: 
#           trump_cards.append(i)
#   value = i[1]

def min_max_trump(player, player_name, meaning, values):
  min_card = ''
  max_card = ''
  min_value = 1000
  max_value = -1
  trump_count = 0

  i = 0
  while i < len(player):
      card = player[i]

      # find suit and value by checking all possible cards
      j = 0
      suit_of_card = ''
      value_str = ''
      found = 0
      while j < len(suit):
          k = 0
          while k < len(meaning):
              possible_card = suit[j] + meaning[k]
              if card == possible_card:
                  suit_of_card = suit[j]
                  value_str = meaning[k]
                  found = 1
              k = k + 1
          j = j + 1

      # if card found and suit matches trump
      if found == 1 and suit_of_card == trump:
          # find the value in values list
          v = 0
          card_value = -1
          while v < len(meaning):
              if meaning[v] == value_str:
                  card_value = values[v]
              v = v + 1

          if card_value != -1:
              if trump_count == 0:
                  min_value = card_value
                  max_value = card_value
                  min_card = card
                  max_card = card
              else:
                  if card_value < min_value:
                      min_value = card_value
                      min_card = card
                  if card_value > max_value:
                      max_value = card_value
                      max_card = card

              trump_count = trump_count + 1
      i = i + 1

  if trump_count > 0:
      print(f"Player {player_name} - Min trump: {min_card}, Max trump: {max_card}")
  else:
      print(f"Player {player_name} has no trump cards.")



meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
suit = ['♥', '♦', '♣', '♠']
values = [0, 1, 2, 3, 4, 5, 6, 7, 8]


deck = []
table = []

user = []
bot1 = []
bot2 = []
bot3 = []

standart_count_cards = 6

create_deck(deck, meaning, suit)

random.shuffle(deck)

trump = random.choice(suit)

print('trump:', trump)

fill_cards_players(user, deck, standart_count_cards)
fill_cards_players(bot1, deck, standart_count_cards)
fill_cards_players(bot2, deck, standart_count_cards)
fill_cards_players(bot3, deck, standart_count_cards)

while True:
    print('user:', user)
    print('bot1:', bot1)
    print('bot2:', bot2)
    print('bot3:', bot3)
    trump_count(user, 'User', count)
    trump_count(bot1, 'bot1', count)
    trump_count(bot2, 'bot2', count)
    trump_count(bot3, 'bot3', count)

    min_max_trump(user, 'User', meaning, values)
    min_max_trump(bot1, 'Bot1', meaning, values)
    min_max_trump(bot2, 'Bot2', meaning, values)
    min_max_trump(bot3, 'Bot3', meaning, values)

    print('table:', table)

    user_hod(user, table)
    bot_hod(bot1, table)
    bot_hod(bot2, table)
    bot_hod(bot3, table)

    fill_cards_players(user, deck, standart_count_cards - len(user))
    fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
    fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
    fill_cards_players(bot3, deck, standart_count_cards - len(bot3))