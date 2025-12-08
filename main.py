
# import random

# minefield = []
# user_field = []

# def create_minefield(field, size_a, size_b):
#     for a in range(11):
#         field.append([])
#         for b in range(11):
#             field[a].append('[_]')

# def create_user_field(field, size_n, size_m):
#     for n in range(11):
#         field.append([])
#         for m in range(11):
#             field[n].append('[_]')

# def show_user_field(field, size_n, size_m):
#     for m in range(11):
#         print('   ', end='')
#     print()
#     for n in range(11):
#         print(' ', ' ', end='')
#         for m in range(size_m):
#             print(field[n][m], ' ', end='')
#         print()

# def show_minefield(minefield, size_a, size_b):
#   for a in range(11):
#       print('   ', end='')
#   print()
#   for b in range(11):
#       print(' ', ' ', end='')
#       for a in range(size_a):
#           print(minefield[a][b], ' ', end='')
#       print()

# size_a = size_n = 10

# size_b = size_m = 10

# def placing_items(minefield, size_a, size_b, items_number):
#     for i in range(items_number):
#         while True:
#             rand_a = random.randint(0, size_a - 1)
#             rand_b = random.randint(0, size_b - 1)
#             if minefield[rand_a][rand_b] == '[_]':
#               minefield[rand_a][rand_b] = random.choice(['[C]', '[U]', '[D]', '[H]'])

#               break

# def user(user_n, user_m, user_choice):
#     user_choice = input("Please enter the directio in which you want to move (W,A,S,D):")
    
#   for i in range(len(minefield)):
#     if user_choice == 'W':
#       user_field[user_n][user_m] = user_field[i-1][0] = 'X'
#     if user_choice == 'S':
#       user_field[user_n][user_m] = user_field[i+1][0] = 'X'
#     if user_choice == 'D':
#       user_field[user_n][user_m] = user_field[0][i+1] = 'X'
#     if user_choice == 'S':
#       user_field[user_n][user_m] = user_field[0][i-1] = 'X'

# # def flag(user_field, size_n, size_m):
# #     user_n = int(input('Enter row of the cell you want to flag: '))
# #     user_m = int(input('Enter column the cell you want to flag: '))
# #     user_field[user_n][user_m] = '[#]'
# #     show_user_field(user_field, size_n, size_m)

# create_minefield(minefield, size_a, size_b)
# create_user_field(user_field, size_n, size_m)
# placing_items(minefield, size_a, size_b, 10)
# show_user_field(user_field, size_n, size_m)
# show_minefield(minefield, size_a, size_b)
# user(user_n, user_m, user_choice = input("Please enter the directio in which you want to move (W,A,S,D)"))

# ======================================================================
# def separate_date(start, stop, text):
#     param = ''
#     for i in range(start, stop):
#         param += text[i]
#     print(param)
#     return param

# def determining_month_time(period):
#     if int(period) >= 1 and int(period) <= 10:
#         print('beginnning')
#     elif int(period) > 10 and int(period) < 20:
#         print('middle')
#     elif int(period) >= 20 and int(period) < 31:
#         print('end')
#     else:
#         print('Error')
        
# def separator(symbol):
#     for i in range(len(date)):
#         if date[i] == symbol:
#             dot_location.append(i)
#     print(dot_location)

# date = input("Please enter your date following the correct format (xx.xx.xx):")
# dot_location = []
# day = ''
# month = ''
# year = ''
# months_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december']

# def month_determination(month, months_names):
#     for i in range(len(months_names)):
#         if int(month) == i+1:
#             print(f'it is {months_names[i]}')

# # for i in range(dot_location[0]):
# #     day += date[i]
# # print(day)

# # for i in range(dot_location[0]+1, dot_location[1]):
# #     month += date[i]
# # print(month)

# # for i in range(dot_location[1]+1, len(date)):
# #     year += date[i]
# # print(year)

# separator('.')
# day = separate_date(0, dot_location[0], date)
# month = separate_date(dot_location[0]+1, dot_location[1], date)
# year = separate_date(dot_location[1]+1, len(date), date)

# determining_month_time(month)
# month_determination(month, months_names)

# # if int(day) >= 1 and int(day) <= 10:
# #     print('beginnning')
# # elif int(day) > 10 and int(day) < 20:
# #     print('middle')
# # elif int(day) >= 20 and int(day) < 31:
# #     print('end')
# # else:
# #     print('Error')
# =====================================================================
# Teacher code
# import random


# def create_pole(pole, size_i, size_j, symbol_empty):
#   for i in range(size_i):
#     pole.append([])
#     for j in range(size_j):
#       pole[i].append(symbol_empty)


# def show_pole(pole, size_i, size_j):
#   for i in range(size_i):
#     for j in range(size_j):
#       print(pole[i][j], ' ', end='')
#     print()


# def fill_items(pole, size_i, size_j, count_items, symbol_items, symbol_empty):
#   for i in range(count_items):
#     while True:
#       rand_pos_i = random.randint(0, size_i - 1)
#       rand_pos_j = random.randint(0, size_j - 1)
#       if pole[rand_pos_i][rand_pos_j] == symbol_empty:
#         pole[rand_pos_i][rand_pos_j] = '[' + symbol_items + ']'
#         break


# def check_cell(cell, cell_user, symbol_armor, symbol_attack, symbol_hp,
#                symbol_coin, symbol_enemy, symbol_empty, user_armor,
#                user_attack, user_hp, user_coins, symbol_user):

#   if cell == '[' + symbol_enemy + ']':
#     if fight(
#         parameters(user_armor, user_attack, user_hp),
#         parameters(random.randint(0, 5), random.randint(1, 5),
#                    random.randint(1, 5))) == 'user_win':
#       print('user_win')
#     elif fight(
#         parameters(user_armor, user_attack, user_hp),
#         parameters(random.randint(0, 5), random.randint(1, 5),
#                    random.randint(1, 5))) == 'bot_win':
#       print('bot_win')
#     else:
#       print('error fight')
#   else:
#     if cell == '[' + symbol_armor + ']':
#       user_armor += 1
#     elif cell == '[' + symbol_attack + ']':
#       user_attack += 1
#     elif cell == '[' + symbol_hp + ']':
#       user_hp += 1
#     elif cell == '[' + symbol_coin + ']':
#       user_coins += 1

#     cell = '[' + symbol_user + ']'
#     cell_user = symbol_empty

#   return user_armor, user_attack, user_hp, user_coins, cell, cell_user


# def user(pole, size_i, size_j, pos_user_i, pos_user_j, symbol_armor,
#          symbol_attack, symbol_hp, symbol_coin, symbol_enemy, symbol_empty,
#          user_armor, user_attack, user_hp, user_coins):

#   user_hod = input('user_hod: ').lower()

#   if user_hod == 's' and pos_user_i + 1 < size_i:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i + 1][pos_user_j], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i + 1][pos_user_j] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i + 1, pos_user_j, user_armor, user_attack, user_hp, user_coins

#   if user_hod == 'w' and pos_user_i - 1 >= 0:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i - 1][pos_user_j], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i - 1][pos_user_j] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i - 1, pos_user_j, user_armor, user_attack, user_hp, user_coins

#   if user_hod == 'a' and pos_user_j - 1 >= 0:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i][pos_user_j - 1], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i][pos_user_j - 1] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i, pos_user_j - 1, user_armor, user_attack, user_hp, user_coins

#   if user_hod == 'd' and pos_user_j + 1 < size_j:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i][pos_user_j + 1], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i][pos_user_j + 1] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i, pos_user_j + 1, user_armor, user_attack, user_hp, user_coins

#   return pos_user_i, pos_user_j, user_armor, user_attack, user_hp, user_coins


# def fight(avg_user, avg_bot):
#   if avg_user > avg_bot:
#     return 'user_win'
#   elif avg_user < avg_bot:
#     return 'bot_win'
#   else:
#     return 'user_win'


# def parameters(parameters_armor, parameters_attack, parameters_hp):
#   avg = 0
#   rand_crit_user = random.randint(1, 2)
#   if rand_crit_user == 1:
#     avg = (parameters_armor + parameters_attack + parameters_hp +
#            (parameters_attack * random.randint(50, 100) / 100 +
#             parameters_attack)) / 4
#   elif rand_crit_user == 2:
#     avg = (parameters_armor + parameters_attack + parameters_hp) / 4
#   else:
#     print('Error critical')

#   return avg


# pole = []
# size_i = 10
# size_j = 10

# symbol_armor = 'A'
# count_armor = 5
# user_armor = 0

# symbol_attack = 'D'
# count_attack = 5
# user_attack = 1

# symbol_hp = 'H'
# count_hp = 5
# user_hp = 1

# symbol_coin = 'C'
# count_coin = 5
# user_coins = 0

# symbol_enemy = 'E'
# count_enemy = 5

# symbol_empty = '[_]'

# create_pole(pole, size_i, size_j, symbol_empty)

# symbol_user = '*'
# pos_user_i = 0
# pos_user_j = 0
# pole[pos_user_i][pos_user_j] = '[' + symbol_user + ']'

# fill_items(pole, size_i, size_j, count_coin, symbol_coin, symbol_empty)
# fill_items(pole, size_i, size_j, count_armor, symbol_armor, symbol_empty)
# fill_items(pole, size_i, size_j, count_attack, symbol_attack, symbol_empty)
# fill_items(pole, size_i, size_j, count_hp, symbol_hp, symbol_empty)
# fill_items(pole, size_i, size_j, count_enemy, symbol_enemy, symbol_empty)

# while True:
#   show_pole(pole, size_i, size_j)
#   print(
#       f'user_coins:{user_coins}, user_hp:{user_hp}, user_armor:{user_armor}, user_attack:{user_attack}'
#   )
#   pos_user_i, pos_user_j, user_armor, user_attack, user_hp, user_coins = user(
#       pole, size_i, size_j, pos_user_i, pos_user_j, symbol_armor,
#       symbol_attack, symbol_hp, symbol_coin, symbol_enemy, symbol_empty,
#       user_armor, user_attack, user_hp, user_coins)
 

# MAZE HARDCODED ===========================================================

# labyrinth = [
#     "███████████████",
#     "█    █        █",
#     "█ ███ █ ███ █ █",
#     "█ █    █    █ █",
#     "█ █ █████ ███ █",
#     "█ █       █   █",
#     "█ █████ ███ ███",
#     "█         █   █",
#     "█ ███ █ █ ███ █",
#     "█   █ █ █ █ █ █",
#     "█ █ █ ███ █ █ █",
#     "█ █       █ █ █",
#     "█ █████████ █ █",
#     "█           █E█",
#     "███████████████"
# ]
    
# labyrinth_2d = []
# for row in labyrinth:
#     new_row = list(row)
#     labyrinth_2d.append(new_row)

# def print_labyrinth(lab):
#     for row in lab:
#         print("".join(row))
        
# labyrinth_2d[1][1] = '*'
# user_m = 1
# user_n = 1

# for row in labyrinth_2d:
#     print("".join(row))

# def move_user(user_n, user_m, command, labyrinth_2d):
#     new_n = user_n
#     new_m = user_m 
#     if command == 's':
#         new_n += 1
#     elif command == 'w':
#         new_n -= 1
#     elif command == 'a':
#         new_m -= 1
#     elif command == 'd':
#         new_m += 1
#     else:
#         print("Error Try again.")
#     if labyrinth_2d[new_n][new_m] == '█':
#         print("WALL!!!")
#         return user_n, user_m
#     else:
#         return new_n, new_m
        
    
# while True:
#     command = input("Move (W,A,S,D): ").lower()
#     labyrinth_2d[user_n][user_m] = ' '
#     user_n, user_m = move_user(user_n, user_m, command, labyrinth_2d)
#     labyrinth_2d[user_n][user_m] = '*'
#     print_labyrinth(labyrinth_2d)
    
# MAZE AUTOMATED ========================================================== 
# import random
# size_a = size_b = 10

# damage_user = 0
# armour_user = 0
# health_user = 0
# user_coins = 0
# user_health = 0
# uron = 1
# result = ''
# check = 0

# minefield = []

# def enemy_power():
#     damage_enemy = random.randint(0, 5)
#     armour_enemy = random.randint(0, 5)
#     health_enemy = random.randint(0, 5)
#     enemy_stats = int((damage_enemy + armour_enemy + health_enemy) / 3)
#     return enemy_stats


# def create_minefield(field, size_a, size_b):
#     for a in range(size_a):
#         field.append([])
#         for b in range(size_b):
#             field[a].append('[_]')


# def placing_items(minefield, size_a, size_b, items_number, item_type):
#     for i in range(items_number):
#         while True:
#             rand_a = random.randint(0, size_a - 1)
#             rand_b = random.randint(0, size_b - 1)
#             if minefield[rand_a][rand_b] == '[_]':
#                 minefield[rand_a][rand_b] = item_type
#                 break
              
# def show_minefield(minefield, size_a, size_b):
#   for a in range(10):
#       print('   ', end='')
#   print()
#   for b in range(10):
#       print(' ', ' ', end='')
#       for a in range(size_a):
#           print(minefield[a][b], ' ', end='')
#       print()

# def move_user(user_n, user_m, command):
#     if command == 'W' or command == 'w' and user_m > 0:
#         user_m -= 1
#     elif command == 'S' or command == 's' and user_m < size_a - 1:
#         user_m += 1
#     elif command == 'A' or command == 'a' and user_n > 0:
#         user_n -= 1
#     elif command == 'D' or  command == 'd' and user_n < size_b - 1:
#         user_n += 1
#     else:
#         print("Error Try again.")
#     return user_n, user_m

# def game(minefield, user_n, user_m, user_coins, damage_user, armour_user, health_user, user_health, uron, result, check):
  
#     user_stats = int(((damage_user + armour_user + health_user) / 3)*uron)
#     if minefield[user_n][user_m] == '[C]':
#         minefield[user_n][user_m] = '[C]'
#         user_coins += 1
#         print(f"Collected a Coin, your coins:{user_coins}")
#     elif minefield[user_n][user_m] == '[D]':
#         minefield[user_n][user_m] = '[D]'
#         damage_user += 1
#         print(f"Damage!:{damage_user}")
#     elif minefield[user_n][user_m] == '[H]':
#         minefield[user_n][user_m] = '[H]'
#         health_user += 1
#         print(f"Collected a Heart!, your health:{health_user}")
#     elif minefield[user_n][user_m] == '[A]':
#         minefield[user_n][user_m] = '[A]'
#         armour_user += 1
#         print(f"Armour!, your armour:{armour_user}")
#     elif minefield[user_n][user_m] == '[E]':
#         enemy_stats = enemy_power()
#         if user_stats <= enemy_stats:
#             print("You lost")
#             minefield[user_n][user_m] = '[_]'
#             user_n, user_m = 0,0
#             result = 'reset'
#             check = 0
#         else:
#             print("You won")
#             check += 1
#             if check == 5:
#              result = 'new level'
#         minefield[user_n][user_m] = '[E]'
# #     elif minefield[user_n][user_m] == '[U]':
# #         uron = random.randint(0,10) / 100

# #     if minefield[user_n][user_m] != '[#]':
# #         minefield[user_n][user_m] = '[_]'

# #     return user_coins, damage_user, armour_user, health_user, user_health, uron, user_n, user_m, result, check

# # def clear_field(minefield, size_a, size_b):
# #         for a in range(size_a):
# #             for b in range(size_b):
# #                 if minefield[a][b] != '[E]':
# #                     minefield[a][b] = '[_]'
# #                     user_n, user_m = 0,0
# #         placing_items(minefield, size_a, size_b, 5, '[C]')
# #         placing_items(minefield, size_a, size_b, 5, '[D]')
# #         placing_items(minefield, size_a, size_b, 5, '[H]')
# #         placing_items(minefield, size_a, size_b, 5, '[A]')
# #         placing_items(minefield, size_a, size_b, 5, '[E]')
# #         placing_items(minefield, size_a, size_b, 5, '[U]')


# # def portal(minefield, size_a, size_b):
# #     for a in range(size_a):
# #         for b in range(size_b):
# #             if minefield[a][b] == '[#]':
# #                 minefield[a][b] = '[_]'
# #     while True:
# #         rand_a = random.randint(0, size_a - 1)
# #         rand_b = random.randint(0, size_b - 1)
# #         if minefield[rand_a][rand_b] == '[_]':
# #             minefield[rand_a][rand_b] = '[#]'
# #             print("Go to #!")
# #             break

# # create_minefield(minefield, size_a, size_b)
# # placing_items(minefield, size_a, size_b, 5, '[C]')
# # placing_items(minefield, size_a, size_b, 5, '[D]')
# # placing_items(minefield, size_a, size_b, 5, '[H]')
# # placing_items(minefield, size_a, size_b, 5, '[A]')
# # placing_items(minefield, size_a, size_b, 5, '[E]')
# # placing_items(minefield, size_a, size_b, 5, '[U]')

# # user_n = 0
# # user_m = 0
# # minefield[user_n][user_m] = '[*]'

# # while True:
# #     show_minefield(minefield, size_a, size_b)

# #     move = input("Move (W,A,S,D): ").lower()

# #     minefield[user_n][user_m] = '[_]'

# #     user_n, user_m = move_user(user_n, user_m, move)


# #     user_coins, damage_user, armour_user, health_user, user_health, uron, user_n, user_m, result, check = game(minefield, user_n, user_m, user_coins, damage_user, armour_user, health_user, user_health, uron, result, check)


# #     if result == 'reset':
# #         clear_field(minefield, size_a, size_b)
# #         result = ''
# #     elif result == 'new level':
# #         portal(minefield, size_a, size_b)
# #         result = ''

# #     if minefield[user_n][user_m] == '[#]':
# #         print("\nWelcome to the Labyrinth!\n")
# #         break

# #     minefield[user_n][user_m] = '[*]' 
    
# # # LEVEL 2

# # def create_labyrinth(width, height):
# #     labyrinth_width = width * 2 + 1
# #     labyrinth_height = height * 2 + 1

# #     labyrinth = [['█' for _ in range(labyrinth_width)] for _ in range(labyrinth_height)]

# #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# #     def create_passages(cx, cy):
# #         directions_shuffled = directions[:]
# #         random.shuffle(directions_shuffled)

# #         for dy, dx in directions_shuffled:
# #             nx, ny = cx + dx, cy + dy
# #             if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
# #                 visited[ny][nx] = True
# #                 wall_y = cy * 2 + 1 + dy 
# #                 wall_x = cx * 2 + 1 + dx
# #                 labyrinth[cy * 2 + 1][cx * 2 + 1] = ' '
# #                 labyrinth[wall_y][wall_x] = ' '
# #                 labyrinth[ny * 2 + 1][nx * 2 + 1] = ' '
# #                 create_passages(nx, ny)

# #     visited = [[False for _ in range(width)] for _ in range(height)]

# #     start_x, start_y = 0, 0
# #     visited[start_y][start_x] = True
# #     create_passages(start_x, start_y)

# #     labyrinth[1][0] = '*'  
# #     labyrinth[labyrinth_height - 2][labyrinth_width - 1] = 'E' 

# #     return labyrinth

# # def print_labyrinth(labyrinth):
# #     for row in labyrinth:
# #         print("".join(row))

# # def move_user2(user_n, user_m, command, labyrinth):
# #     new_n = user_n
# #     new_m = user_m 
# #     if command == 's':
# #         new_n += 1
# #     elif command == 'w':
# #         new_n -= 1
# #     elif command == 'a':
# #         new_m -= 1
# #     elif command == 'd':
# #         new_m += 1
# #     else:
# #         print("Error Try again.")
# #     if new_n < 0 or new_n >= len(labyrinth) or new_m < 0 or new_m >= len(labyrinth[0]):
# #         print("Out of bounds!")
# #         return user_n, user_m
# #     if labyrinth[new_n][new_m] == '█':
# #         print("WALL!!!")
# #         return user_n, user_m
# #     else:
# #         return new_n, new_m
        
# # labyrinth = create_labyrinth(10, 5)
# # user_n, user_m = 1, 0

# # while True:
# #     print_labyrinth(labyrinth)
# #     command = input("Move (W,A,S,D): ").lower()
# #     labyrinth[user_n][user_m] = ' '
# #     user_n, user_m = move_user2(user_n, user_m, command, labyrinth)
# #     labyrinth[user_n][user_m] = '*'


# # ======================================================================

# import random


# def create_deck(deck, meaning, suit):
#   for i in suit:
#     for j in meaning:
#       deck.append(i + j)


# def fill_cards_players(player, deck, count_cards):
#   if len(deck) > 0:
#     for i in range(count_cards):
#       tmp_cards = random.choice(deck)
#       player.append(tmp_cards)
#       deck.remove(tmp_cards)


# def user_hod(player, table):
#   if len(player) > 0:
#     while True:
#       user = input('user:')
#       if user in player:
#         table.append(user)
#         player.remove(user)
#         break
#   else:
#     print('no cards user')


# def bot_hod(player, table):
#   if len(player) > 0:
#     tmp = random.choice(player)
#     table.append(tmp)
#     player.remove(tmp)

# def trump_count(player, player_name, count):
#     count = []
#     for i in range(len(player)):
#         if player[i][0] == trump:
#             count.append(trump)
#     print(f"Player {player_name} has {len(count)} trump cards")
#     return count
  

# # def trump_check(user, bot1, bot2, bot3, meaning, values):
# #   general = user + bot1 + bot2 + bot3
# #   trump_cards = []
# #   for i in general:
# #       suit = i[0]
# #       if suit == trump: 
# #           trump_cards.append(i)
# #   value = i[1]

# def min_max_trump(player, player_name, meaning, values):
#   min_card = ''
#   max_card = ''
#   min_value = 1000
#   max_value = -1
#   trump_count = 0

#   i = 0
#   while i < len(player):
#       card = player[i]

#       # find suit and value by checking all possible cards
#       j = 0
#       suit_of_card = ''
#       value_str = ''
#       found = 0
#       while j < len(suit):
#           k = 0
#           while k < len(meaning):
#               possible_card = suit[j] + meaning[k]
#               if card == possible_card:
#                   suit_of_card = suit[j]
#                   value_str = meaning[k]
#                   found = 1
#               k = k + 1
#           j = j + 1

#       # if card found and suit matches trump
#       if found == 1 and suit_of_card == trump:
#           # find the value in values list
#           v = 0
#           card_value = -1
#           while v < len(meaning):
#               if meaning[v] == value_str:
#                   card_value = values[v]
#               v = v + 1

#           if card_value != -1:
#               if trump_count == 0:
#                   min_value = card_value
#                   max_value = card_value
#                   min_card = card
#                   max_card = card
#               else:
#                   if card_value < min_value:
#                       min_value = card_value
#                       min_card = card
#                   if card_value > max_value:
#                       max_value = card_value
#                       max_card = card

#               trump_count = trump_count + 1
#       i = i + 1

#   if trump_count > 0:
#       print(f"Player {player_name} - Min trump: {min_card}, Max trump: {max_card}")
#   else:
#       print(f"Player {player_name} has no trump cards.")
            

    
# meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
# suit = ['♥', '♦', '♣', '♠']
# values = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# deck = []
# table = []

# user = []
# bot1 = []
# bot2 = []
# bot3 = []

# standart_count_cards = 6

# create_deck(deck, meaning, suit)

# random.shuffle(deck)

# trump = random.choice(suit)

# print('trump:', trump)

# fill_cards_players(user, deck, standart_count_cards)
# fill_cards_players(bot1, deck, standart_count_cards)
# fill_cards_players(bot2, deck, standart_count_cards)
# fill_cards_players(bot3, deck, standart_count_cards)

# while True:
#     print('user:', user)
#     print('bot1:', bot1)
#     print('bot2:', bot2)
#     print('bot3:', bot3)
#     trump_count(user, 'User', count)
#     trump_count(bot1, 'bot1', count)
#     trump_count(bot2, 'bot2', count)
#     trump_count(bot3, 'bot3', count)

#     min_max_trump(user, 'User', meaning, values)
#     min_max_trump(bot1, 'Bot1', meaning, values)
#     min_max_trump(bot2, 'Bot2', meaning, values)
#     min_max_trump(bot3, 'Bot3', meaning, values)
    
#     print('table:', table)
    
#     user_hod(user, table)
#     bot_hod(bot1, table)
#     bot_hod(bot2, table)
#     bot_hod(bot3, table)
    
#     fill_cards_players(user, deck, standart_count_cards - len(user))
#     fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
#     fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
#     fill_cards_players(bot3, deck, standart_count_cards - len(bot3))

# # import random


# # def create_deck(deck, meaning, suit):
# #   for i in suit:
# #     for j in meaning:
# #       deck.append(i + j)


# # def fill_cards_players(player, deck, count_cards):
# #   if len(deck) > 0:  
# #     for i in range(min(count_cards, len(deck))):
# #       tmp_cards = random.choice(deck)
# #       player.append(tmp_cards)
# #       deck.remove(tmp_cards)


# # def user_hod(player, table):
# #   if len(player) > 0:
# #     while True:
# #       user = input('user:')
# #       if user in player:
# #         table.append(user)
# #         player.remove(user)
# #         cover_card(table, player)
# #         break
# #   else:
# #     print('no cards user')

# # def bot_hod(player, table, name):
# #   if len(player) > 0:
# #     tmp = random.choice(player)
# #     print(f'{name} played: {tmp}')
# #     table.append(tmp)
# #     player.remove(tmp)
# #     cover_card(table, player)
# #   else:
# #     print('Bot has no cards.')


# # def find_min_trump(player, symbol_trump, meaning):
# #   tmp_mss = []
# #   tmp_mss_index = []
# #   tmp_res = ''
# #   for item in player:
# #     if symbol_trump == item[0]:
# #       tmp_mss.append(item)

# #   if len(tmp_mss) > 0:
# #     for i in tmp_mss:
# #       for j in range(len(meaning)):
# #         if i[1] == meaning[j]:
# #           tmp_mss_index.append(j)

# #   if len(tmp_mss_index) > 0:
# #     tmp_mss_index.sort()
# #     tmp_res = symbol_trump + meaning[tmp_mss_index[0]]

# #   if tmp_res != None:
# #     return tmp_res

# # def first_move(user, bot1, bot2, bot3, trump, meaning):
# #         players = [user, bot1, bot2, bot3]
# #         names = ['user', 'bot1', 'bot2', 'bot3']
# #         cards = []

# #         for i in range(4):
# #             min_card = find_min_trump(players[i], trump, meaning)
# #             cards.append(min_card)

# #         lowest_rank = None
# #         first_player_index = None

# #         # Step 2: Find the player with the lowest-ranked trump card
# #         for i in range(4):
# #             card = cards[i]
# #             if card != '':
# #                 # Get rank manually (without index())
# #                 rank = -1
# #                 for j in range(len(meaning)):
# #                     if card[1] == meaning[j]:
# #                         rank = j
# #                         break
# #                 if rank != -1:
# #                     if lowest_rank is None or rank < lowest_rank:
# #                         lowest_rank = rank
# #                         first_player_index = i

# #         if first_player_index is not None:
# #             return names[first_player_index]
# #         else:
# #             return None  # No one has trump cards

# # def play_round(first_player, players, player_names, deck, table, max_hand_size=6):
# #     order = []

# #     if first_player == 'user':
# #         order = [0, 1, 2, 3] 
# #     elif first_player == 'bot1':
# #         order = [1, 2, 3, 0]
# #     elif first_player == 'bot2':
# #         order = [2, 1, 3, 0]
# #     elif first_player == 'bot3':
# #         order = [3, 1, 2, 0]

# #     for i in order:
# #         name = player_names[i]
# #         if name == 'user':
# #             user_hod(players[i], table)
# #             print(table)
# #         else:
# #             bot_hod(players[i], table, name)
# #             print(table)

# #     for i in range(len(players)):
# #         missing_cards = max_hand_size - len(players[i])
# #         fill_cards_players(players[i], deck, missing_cards)

# #     print('user:', players[0])

# # # def all_trump_cards(player, trump):
# # #     all_player_trump_cards = []
# # #     for i in player:
# # #         if i[0] == trump:
# # #             all_player_trump_cards.append(i)
# # #     return all_player_trump_cards


# # def cover_card(table, player):
# #         tmp_player_index = []

# #         # Step 1: Sort player by meaning rank
# #         if len(player) > 0:
# #             for card in player:
# #                 for i in range(len(meaning)):
# #                     if card[1] == meaning[i]:
# #                         tmp_player_index.append(card)

# #             for i in range(len(player)):
# #                 for j in range(len(player)):
# #                     rank_i = 0
# #                     for k in range(len(meaning)):
# #                         if player[i][1] == meaning[k]:
# #                             rank_i = k
# #                             break
# #                     rank_j = 0
# #                     for k in range(len(meaning)):
# #                         if player[j][1] == meaning[k]:
# #                             rank_j = k
# #                             break

# #                     if rank_i > rank_j:
# #                         player[i], player[j] = player[j], player[i]

# #         # Step 2: Compare last table card with player's cards
# #         if len(table) > 0 and len(player) > 0:
# #             table_card_value = table[-1][1]  # e.g., '9'
# #             table_card_suit = table[-1][0]   # e.g., '♥'

# #             table_rank = 0
# #             for i in range(len(meaning)):
# #                 if table_card_value == meaning[i]:
# #                     table_rank = i
# #                     break

# #             # Instead of True/False, we print and exit inside the loop
# #             for card in player:
# #                 if card[0] == table_card_suit:
# #                     card_rank = 0
# #                     for j in range(len(meaning)):
# #                         if card[1] == meaning[j]:
# #                             card_rank = j
# #                             break

# #                     if card_rank > table_rank:
# #                         print("YES — player can cover the card.")
# #                         break
# #             else:
# #                 # The else block of a for loop runs only if the loop wasn't broken
# #                 print("NO — player cannot cover the card.")
    

# # meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
# # suit = ['♥', '♦', '♣', '♠']

# # deck = []
# # table = []

# # user = []
# # bot1 = []
# # bot2 = []
# # bot3 = []

# # standart_count_cards = 6

# # create_deck(deck, meaning, suit)

# # random.shuffle(deck)

# # trump = random.choice(suit)
# # print('trump:', trump)

# # fill_cards_players(user, deck, standart_count_cards - len(user))
# # fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
# # fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
# # fill_cards_players(bot3, deck, standart_count_cards - len(bot3))

# # print('user:', user)
# # print('bot1:', bot1)
# # print('bot2:', bot2)
# # print('bot3:', bot3)

# # print('table:', table)

# # a = find_min_trump(user, trump, meaning)
# # print('1 ', a)
# # b = find_min_trump(bot1, trump, meaning)
# # print('2 ', b)
# # c = find_min_trump(bot2, trump, meaning)
# # print('3 ', c)
# # d = find_min_trump(bot3, trump, meaning)
# # print('4 ', d)

# # first = first_move(user, bot1, bot2, bot3, trump, meaning)

# # if first:
# #     print(f'\nFirst to move: {first}')
# # else:
# #     print('\nNo player has a trump card.')

# # while len(user) > 0 or len(bot1) > 0 or len(bot2) > 0 or len(bot3) > 0 or len(deck) > 0:
# #     players = [user, bot1, bot2, bot3]
# #     player_names = ['user', 'bot1', 'bot2', 'bot3']
# #     play_round(first, players, player_names, deck, table, standart_count_cards)

# # person = {
# #   'name': 'qwerty',
# #   'age' : 25,
# #   'name1': 'qwerty2',
# # }

# # print(person)
# # # print(person['name'])
# # # print(person['age'])
# # print('=====')
# # # print(person['qwerty'])
# # # print(person['name'])
# # person['name'] = 'poni'
# # # print(person['name'])
# # print('=====')
# # person['city'] = 'Dnipro'
# # print(person)
# # print('=====')
# # del person['name1']
# # print(person)

# # for jsdhvfjds, sdfklskdfs in person.items():
# #     print(f'{jsdhvfjds}: {sdfklskdfs}')

# # print(person.keys())
# # print(person.values())


# # print(person.get('asd', 'error keys'))

# # def uniq(user_cat, user_value):
# #     if user_cat in dictionary:
# #         print('Enter something else')

# # def change_value():
# #     user_cat = input('Please enter the CAR of the value:')
# #     new_value = input('Please enter the NEW value:')
# #     dictionary[user_cat] = new_value
# #     return new_value

# # def delete_value(dictionary):
# #     to_delete = input('What would u like to delete:')
# #     del dictionary[to_delete]

# # def safe_show(dictionary, element_name):
# #     print(dictionary.get(element_name))
# #     return element_name
        

# # dictionary = {}

# # while True:
# #     user_cat = input('Please enter the category:')
# #     user_value = input('Please enter the value:')
# #     uniq(user_cat, user_value)
# #     dictionary[user_cat] = user_value
# #     print(dictionary)
# #     if user_cat == 'break' or user_value == 'break':
# #         break
# #     user_change = input('Do you want to change the dictionary: Y -fir yes; N -no:').lower()
# #     if user_change == 'yes':
# #          change_value()
# #     else:
# #         continue
# #     user_delet = input('Do you want to delete an element: Y -fir yes; N -no:').lower()
# #     if user_change == 'yes':
# #          delete_value(dictionary)
# #     else:
# #         continue
# #     print(dictionary)
# #     element_name = input('What element u want to see: ')
# #     safe_show(dictionary, element_name)

# # import random

# # cell = '[_]'
# # field = []

# # def create_field(field):
# #     for a in range(3):              
# #         field.append([])            
# #         for b in range(3):
# #             field[a].append(cell) 

# # def show_field(field):
# #     for row in field:
# #         for cell in row:
# #             print(cell, end='')
# #         print()

# # def bot_move():
# #     while True:
# #         bot_x = random.randint(0,2)
# #         bot_y = random.randint(0,2)
# #         if field[bot_x][bot_y] != '[X]':
# #             field[bot_x][bot_y] = '[O]'
# #             break
# #         return bot_x, bot_y
    
# # def winner():
# #     options = {
# #                 'r1': [field[0][0], field[0][1], field[0][2]],
# #                 'r2': [field[1][0], field[1][1], field[1][2]],
# #                 'r3': [field[2][0], field[2][1], field[2][2]],
# #                 'c1': [field[0][0], field[1][0], field[2][0]],
# #                 'c2': [field[0][1], field[1][1], field[2][1]],
# #                 'c3': [field[0][2], field[1][2], field[2][2]],
# #                 'd1': [field[0][0], field[1][1], field[2][2]],
# #                 'd2': [field[0][2], field[1][1], field[2][0]]
# #             }
# #     for i in options:
# #         row = options[i]
# #         if row == ['[O]','[O]','[O]']:
# #             print('Bot wins')
# #             return True
# #         elif row == ['[X]','[X]','[X]']:
# #             print('User wins')
# #             return True
# #     return False


# # create_field(field)
# # show_field(field)

# # while True:
# #     user_x = int(input('Enter the x (0-2): '))
# #     if user_x > 2:
# #         print('!')
# #     user_y = int(input('Enter the y (0-2): ')) 
# #     if user_y > 2:
# #         print('!')
# #     field[user_x][user_y] = '[X]'
# #     bot_move()
# #     show_field(field)
# #     if winner():
# #         break
    
# #===========================(tuple)
# # point = (10,20)
# # print(point)
# #
# # # print(type(point))
# # print(point[0])
# #
# # x, y = point
# # print(x,y)
# #===========================(set)

# # nums = {1,2,3,4,3,2, 5}
# # print(nums)
# #
# # nums.add(6)
# # print(nums)
# # nums.add(1)
# # print(nums)
# #
# # nums.remove(1)
# # print(nums)

# # nums1 = {1,2,3}
# # nums2 = {3,4,5}

# # print(nums1, nums2)
# # print(nums1 | nums2)
# # print(nums1 & nums2)
# # print(nums1 ^ nums2)
# # print(nums1 - nums2)

# # tuple_1 = ('d', 'b', 'c', 'd')
# # tuple_2 = ('c', 'e', 'f', 'b')

# # new_tuple = tuple_1 + tuple_2

# # for i in range(3):
# #     print(new_tuple[i])

# # tuple_1 = (1, 2, 3)
# # tuple_2 = (4, 5, 6)
# # tmp = []

# # new_tuple = tuple_1 + tuple_2
# # for i in new_tuple:
# #     tmp.append(i)
# # tmp.remove(2)
# # tmp.append(10)
# # print(tmp)

# # nums = (2, 45, 3, 654, 425, 563, 42, 246, 9090)

# # while True:
# #     user_num = int(input('Ur num?:'))
# #     if user_num in nums:
# #         print('+')
# #         break
# #     elif user_num == 'break':
# #         break
# #     else:
# #         print('-')

# # TRY AGAIN ======================================================================================
# # alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',]
# # my_tuple = ()
# # tmp = []

# # nums = input("Ur nums, using a comma(e.g. 4,5):")

# # for i in nums:
# #     if i != ',' and i !=' ':
# #         tmp.append(i)
# # print(tmp)
# # for i in tmp:
# #     my_tuple += (i,)
# # print(my_tuple)
# # ===============================================================================================

# # bet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',]
# # my_tuple = (tuple(range(1, 100)))


# # for i in my_tuple:
# #     print(f"Coordinate is {my_tuple[i]} = {bet[i]}")
# # ===============================================================================================

# # user_word = input('Enter one word:')
# # tmp_list = []
# # tmp = {1,2}
# # for i in user_word:
# #     tmp_list.append(i)
# # for i in tmp_list:
# #     tmp.add(i)
# # for i in tmp(range(len(1))):
# #     tmp.remove(i)
# # print(tmp)
# # ===============================================================================================

# # import random

# # cell = '[_]'
# # field = []

# # def create_field(field):
# #     for a in range(3):              
# #         field.append([])            
# #         for b in range(3):
# #             field[a].append(cell) 

# # def show_field(field):
# #     for row in field:
# #         for cell in row:
# #             print(cell, end='')
# #         print()

# # def bot_move():
# #     while True:
# #         bot_x = random.randint(0,2)
# #         bot_y = random.randint(0,2)
# #         if field[bot_x][bot_y] != '[X]':
# #             field[bot_x][bot_y] = '[O]'
# #             break
# #         return bot_x, bot_y

# # def winner():
# #     options = {
# #         (field[0][0], field[0][1], field[0][2]),
# #         (field[1][0], field[1][1], field[1][2]),
# #         (field[2][0], field[2][1], field[2][2]),
# #         (field[0][0], field[1][0], field[2][0]),
# #         (field[0][1], field[1][1], field[2][1]),
# #         (field[0][2], field[1][2], field[2][2]),
# #         (field[0][0], field[1][1], field[2][2]),
# #         (field[0][2], field[1][1], field[2][0])
# #     }



# #     for i in options:
# #         if i == ('[O]', '[O]', '[O]'):
# #             print('Bot wins')
# #             return True
# #         elif i == ('[X]', '[X]', '[X]'):
# #             print('User wins')
# #             return True
# #     return False



# # create_field(field)
# # show_field(field)

# # while True:
# #     user_x = int(input('Enter the x (0-2): '))
# #     if user_x > 2:
# #         print('!')
# #     user_y = int(input('Enter the y (0-2): ')) 
# #     if user_y > 2:
# #         print('!')
# #     field[user_x][user_y] = '[X]'
# #     bot_move()
# #     show_field(field)
# #     if winner():
# #         break
# # ===============================================================================================


# # def fav_color():
# #     user_color = input("What is their favourite color:").lower()
# #     if user_color == "blue":
# #         print("Correct")
# #         return 1
# #     else:
# #         print("Incorrect")
# #         return 0


# # while True:
# #     result = fav_color()
# #     if result == 0:
# #        continue
# #     elif result == 1:
# #        break
# # ===============================================================================================
# # def make_coffee(size, flavor = "regular"):
# #     print(f"Making a {size} {flavor} coffee...")

# # make_coffee("large")
# # make_coffee("small", "macchiato")
# # ===============================================================================================

# # import random

# # def create_deck(deck, meaning, suit):
# #   for i in suit:
# #     for j in meaning:
# #       deck.append(i + j)
# #   print(deck)

# # def fill_cards_players(player, deck, count_cards):
# #   if len(deck) > 0:
# #     for i in range(count_cards):
# #       tmp_cards = random.choice(deck)
# #       player.append(tmp_cards)
# #       deck.remove(tmp_cards)

# # def game_order(deck, user, bot1, bot2):
# #   players = [user, bot1, bot2]
  
# #   while len(deck) > 0:
# #     first_player = random.choice(players)
# #     if first_player == user:
# #       user_choice = input("Enter the card u want: ")
# #       user_choice_function(user, bot1, "Bot1", user_choice)
# #       user_choice_function(user, bot2, "Bot2", user_choice)
# #       bot_choice_function(bot1, deck, "Bot1", user)
# #       bot_choice_function(bot1, deck, "Bot1", bot2)
# #       fill_cards_players(user, deck, standart_count_cards - len(user))
# #       fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
# #       fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
# #       print("Bot-1's hand", bot1)
# #       print("Bot-2's hand", bot2)
# #       print("User's hand", user)
# #     elif first_player == bot1:
# #       bot_choice_function(bot1, deck, "Bot1", user)
# #       bot_choice_function(bot1, deck, "Bot1", bot2)
# #       user_choice = input("Enter the card u want: ")
# #       user_choice_function(user, bot1, "Bot1", user_choice)
# #       user_choice_function(user, bot2, "Bot2", user_choice)
# #       fill_cards_players(user, deck, standart_count_cards - len(user))
# #       fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
# #       fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
# #       print("Bot-1's hand", bot1)
# #       print("Bot-2's hand", bot2)
# #       print("User's hand", user)
# #     elif first_player == bot2:
# #       bot_choice_function(bot2, deck, "Bot2", user)
# #       bot_choice_function(bot2, deck, "Bot2", bot1)
# #       user_choice = input("Enter the card u want: ")
# #       user_choice_function(user, bot1, "Bot1", user_choice)
# #       user_choice_function(user, bot2, "Bot2", user_choice)
# #       fill_cards_players(user, deck, standart_count_cards - len(user))
# #       fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
# #       fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
# #       print("Bot-1's hand", bot1)
# #       print("Bot-2's hand", bot2)
# #       print("User's hand", user)

# # def user_choice_function(user, bot, bot_name, chosen_card):
# #   user_cards = []
# #   if chosen_card in bot:
# #       bot.remove(chosen_card)
# #       user.append(chosen_card)
# #       print("You took", chosen_card, f"from {bot_name}!")
# #   else:
# #       print(f"{bot_name} does not have this card")
# #   for i in range(len(user)):
# #     meaning1 = ""
# #     for a in user[i]:
# #         if a not in ['♥', '♦', '♣', '♠']:
# #           meaning1 = meaning1 + a

# #     for j in range(i + 1, len(user)):
# #       meaning2 = ""
# #       for a in user[j]:
# #             if a not in ['♥', '♦', '♣', '♠']:
# #               meaning2 += a

# #       if meaning1 == meaning2:
# #             if user[i] not in user_cards:
# #                 user_cards.append(user[i])
# #             if user[j] not in user_cards:
# #                 user_cards.append(user[j])
# #   print(user_cards)
# #   return user_cards

# # def bot_choice_function(player, deck, bot_name, opponent):
# #   bot_cards = []
# #   for i in range(len(player)):
# #       meaning1 = ""
# #       for a in player[i]:
# #           if a not in ['♥', '♦', '♣', '♠']:
# #             meaning1 = a + meaning1

# #       for j in range(i + 1, len(player)):
# #         meaning2 = ""
# #         for a in player[j]:
# #               if a not in ['♥', '♦', '♣', '♠']:
# #                 meaning2 = a + meaning2

# #         if meaning1 == meaning2:
# #               if player[i] not in bot_cards:
# #                   bot_cards.append(player[i])
# #               if player[j] not in bot_cards:
# #                   bot_cards.append(player[j])
                
# #   if len(bot_cards) > 0:
# #     chosen_card = random.choice(bot_cards)
# #     meaning = ""
# #     for a in chosen_card:
# #         if a not in ['♥', '♦', '♣', '♠']:
# #             meaning = meaning + a
# #     bot_suite = random.choice(['♥', '♦', '♣', '♠'])
# #     bot_choice = bot_suite + meaning
# #     print(f"{bot_name} chose", bot_choice)
    
# #     if bot_choice in opponent:
# #       opponent.remove(bot_choice)
# #       player.append(bot_choice)
# #       print(f"{bot_name} took", bot_choice, f"from {opponent}!")
# #     else:
# #         print(f"Wrong guess, {bot_name}.")
# #   else:
# #     if len(deck) == 0:
# #       print("The deck is empty")
# #       return bot_cards
# #     bot_choice = random.choice(deck)
# #     print(bot_choice)
# #     if bot_choice in opponent:
# #       opponent.remove(bot_choice)
# #       player.append(bot_choice)
# #       print(f"{bot_name} took", bot_choice, "from u!")
# #     else:
# #         print(f"Wrong guess, {bot_name}.")
# #   return bot_cards
    
# # def winner(user_cards, bot_cards, deck):
# #   if len(user_cards) < len(bot_cards) and len(deck) == 0:
# #     print("User won!")
# #   elif len(bot_cards) < len(user_cards) and len(deck) == 0:
# #     print("User won!")

# # meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
# # suit = ['♥', '♦', '♣', '♠']

# # deck = []

# # user = []
# # bot1 = []
# # bot2 = []
# # bot3 = []

# # standart_count_cards = 4

# # create_deck(deck, meaning, suit)


# # fill_cards_players(user, deck, standart_count_cards)
# # fill_cards_players(bot1, deck, standart_count_cards)
# # fill_cards_players(bot2, deck, standart_count_cards)

# # while len(deck) > 0:
# #     game_order(deck, user, bot1, bot2)
# # winner(user, [bot1, bot2], deck)

# # file = open('t.txt', 'r' )
# # text_file = file.read()
# # print(text_file)
# # file.close()

# # with open('t.txt', 'r') as file:
# #     text_file = file.read()
# #     print(text_file)

# # file = open('t.txt', 'w' )
# # file.write("Hello World")
# # file.write("\nHello World")
# # file.write("\nHello World")
# # file.write("\nHello World")
# # file.close()

# # with open('t.txt', 'w') as file:
# #     file.write('Hello World1')
# #     file.write('\nHello World1')
# #
# # with open('t.txt', 'w') as file:
# #     file.write('Hello World2')
# #     file.write('\nHello World2')


# # with open('t.txt', 'a') as file:
# #     file.write('Hello World1')
# #     file.write('\nHello World1')

# # while True:
# #   user_input = input("Pls enter ur text:")
# #   with open('user_text.txt', 'a') as file:
# #       file.write(user_input)
# #   if "stop" in user_input:
# #     break
# # with open('user_text.txt', 'r') as fil_

# # def calc():
# #   user_num1 = int(input("Pls enter num1:"))
# #   sign = input("pls enter ur sin:")
# #   user_num2 = int(input("Pls enter num2:"))
# #   result = 0
# #   if sign == '-':
# #     result = user_num1 - user_num2
# #   elif sign == '+':
# #     result = user_num1 + user_num2
# #   elif sign == '/':
# #     result = user_num1 / user_num2
# #   elif sign == '*':
# #     result = user_num1 * user_num2
# #   else:
# #     "No"
# #   print(result)
# #   result = (f"{user_num1} {sign} {user_num2} = {result}")
# #   return result

# # while True:
# #   log = calc()
# #   with open('log.txt', 'a') as file:
# #    file.write(log)
# #   with open('log.txt', 'r') as file:
# #    log = file.read()
# #   print(log)  

# # with open('t.txt', 'a') as file:
# #   file.write('\nЖдем ввода первого числа')
# #   user_nun_one = int(input('user_nun_one: '))
# #   file.write('\nЮзер ввел первое числа')
# #   file.write('\n')
# #   file.write(str(user_nun_one))
# #   file.write('\nЖдем ввод знака')
# #   user_ch = input('user_ch: ')
# #   file.write('\nЮзер ввел знак, ждем ввод второго числа')
# #   user_nun_two = int(input('user_nun_two: '))
# #   file.write('\nЮзер ввел второе число, ждем ввод второго числа')

# #   if user_ch == '+':

# #       print(user_nun_one+user_nun_two)

# #   elif user_ch == '-':
# #       print(user_nun_one-user_nun_two)
# #   elif user_ch == '*':
# #       print(user_nun_one*user_nun_two)
# #   elif user_ch == '/':
# #       if user_nun_two != 0:
# #           print(user_nun_one/user_nun_two)
# #       else:
# #           print('Error del')
# #   else:
# #       print('Error ch')
    
# # import random

# # cell = '[_]'
# # field = []

# # def create_field(field):
# #     for a in range(3):              
# #         field.append([])            
# #         for b in range(3):
# #             field[a].append(cell) 

# # def show_field(field):
# #     for row in field:
# #         for cell in row:
# #             print(cell, end='')
# #         print()


# # def bot_move():
# #     while True:
# #         bot_x = random.randint(0, 2)
# #         bot_y = random.randint(0, 2)
# #         if field[bot_x][bot_y] == '[_]':
# #             field[bot_x][bot_y] = '[O]'
# #             break

# # def winner(field):
# #     options = {
# #                 'r1': [field[0][0], field[0][1], field[0][2]],
# #                 'r2': [field[1][0], field[1][1], field[1][2]],
# #                 'r3': [field[2][0], field[2][1], field[2][2]],
# #                 'c1': [field[0][0], field[1][0], field[2][0]],
# #                 'c2': [field[0][1], field[1][1], field[2][1]],
# #                 'c3': [field[0][2], field[1][2], field[2][2]],
# #                 'd1': [field[0][0], field[1][1], field[2][2]],
# #                 'd2': [field[0][2], field[1][1], field[2][0]]
# #             }
# #     for i in options:
# #         row = options[i]
# #         if row == ['[O]','[O]','[O]']:
# #             print('Bot wins')
# #             return True
# #         elif row == ['[X]','[X]','[X]']:
# #             print('User wins')
# #             return True
            
# #     for row in field:
# #         for i in row:
# #             if i == "[_]":
# #              return False
            
# #     print("It's a tie!")
# #     return True
  
# # def save_game(field):
# #   user_save = input("If you want to save the save press 'S', if no press 'N':").lower()
# #   if user_save == 's':
# #       with open('game_save.txt', 'w') as file:
# #           for i in field:
# #               for j in i:
# #                   file.write(j)  
# #               file.write('\n')        
# #       print("Game saved")
# #       load_game()
     
# #       with open('game_save.txt', 'r') as file:
# #        game_save = file.read()
# #       print(game_save)  

# #   elif user_save == 'n':
# #       show_field(field)
# #   else:
# #       print('!')
# #       save_game(field)

# # def load_game():
# #   saved_field = [['[_]','[_]','[_]'],
# #     ['[_]','[_]','[_]'],
# #     ['[_]','[_]','[_]']]
  
# #   user_again = input("If you want to load the save press 'L':").lower()
# #   if user_again == 'l':
# #     with open('game_save.txt', 'r') as file:
# #       for i in range(3):
# #         for j in range(3):
# #           cell = ''
# #           for k in range(3):
# #               cell += file.read(1)
# #           saved_field[i][j] = cell
# #         file.read(1)   

# # def user_move():
# #     while True:
# #         user_x = int(input('Enter the x (0-2): '))
# #         user_y = int(input('Enter the y (0-2): '))

# #         if not (0 <= user_x <= 2 and 0 <= user_y <= 2):
# #             print('!')
# #             continue

# #         if field[user_x][user_y] != '[_]':
# #             print('!')
# #             continue  

# #         field[user_x][user_y] = '[X]'
# #         break

# # create_field(field)
# # show_field(field)

# # while True:
# #     user_move()
# #     show_field(field)
# #     if winner(field):
# #         break
# #     bot_move()
# #     show_field(field)
# #     if winner(field):
# #         break
# #     save_game(field)
# # ==========================================================================

# # examples = "10+23, 999+1, 5-4, 10+3"
 

# # with open('text.txt', 'w') as file:
# #   file.write(examples)

# # with open('text.txt', 'r') as file:
# #     text = file.read()

# # text_new = []
# # results = [] 

# # def examples_function():

# #   tmp = ''
# #   for i in text:
# #     if i not in [',', ' ']: 
# #         tmp += i
# #     else:
# #         if tmp: 
# #             text_new.append(tmp)
# #             tmp = ''
# #   if tmp:
# #     text_new.append(tmp)


# # def calc():
# #   for example in text_new:   
# #       num1 = ''
# #       num2 = ''
# #       sym = ''
  
# #       for i in example:
# #           if i in '+-*/' and sym == '':
# #               sym = i
# #           elif sym == '':
# #               num1 += i
# #           else:
# #               num2 += i
  
# #       num1 = int(num1)
# #       num2 = int(num2)
  
# #       if sym == '+':
# #           res = num1 + num2
# #       elif sym == '-':
# #           res = num1 - num2
# #       elif sym == '*':
# #           res = num1 * num2
# #       elif sym == '/':
# #           res = num1 / num2
# #       else:
# #           res = 0
  
# #       results.append(float(res))

# # def user_answer():
# #   for i in range(len(text_new)):
# #     print(text_new[i])
# #     user_input = input("User answer: ")
# #     if user_input.isdigit():
# #       user_input = float(user_input)
# #     else:
# #       print("!")
# #     while user_input != results[i]:
# #       print('-')
# #       user_input = float(input("User answer: "))
# #     if user_input == results[i]:
# #         print("+")
        

# # examples_function()
# # calc()
# # user_answer() 
# # ==========================================================================
# # examples = "10+23, 999+1, 5-4, 10+3"


# # with open('t.txt', 'w') as file:
# #   file.write(examples)

# # def read_file(filename, complete):
# #   with open(filename, 'r') as file:
# #       complete.append(file.read())

# # def primer(obg, mss_primer):
# #   tmp = ''
# #   for i in range(len(obg[0])):
# #       if obg[0][i] != '\n':
# #          tmp += obg[0][i]
# #       else:
# #           mss_primer.append(tmp)
# #           tmp = ''
# #   mss_primer.append(tmp)


# # def search_ch(obj, mss_ch):
# #   for i in range(len(obj)):
# # #       if obj[i] == '+' or obj[i] == '-' or obj[i] == '*' or obj[i] == '/':
# # #           mss_ch.append(i)

# # # def add_number(start, stop, obj, mss_num):
# # #   tmp = ''
# # #   for i in range(start, stop):
# # #       tmp += obj[i]
# # #   mss_num.append(tmp)

# # # c_file = []
# # # mss_primer = []
# # # mss_index_ch = []
# # # mss_num = []

# # # read_file('t.txt', c_file)
# # # primer(c_file, mss_primer)

# # # for i in range(len(mss_primer)):
# # #   search_ch(mss_primer[i],mss_index_ch)

# # # for i in range(len(mss_primer)):
# # #   add_number(0, mss_index_ch[i], mss_primer[i], mss_num)
# # #   add_number(mss_index_ch[i]+1, len(mss_primer[i]), mss_primer[i], mss_num)


# # # print(c_file)
# # # print(mss_primer)
# # # print(mss_index_ch)
# # # print(mss_num)

# # # user = int(input(': '))
# # # if mss_primer[0][mss_index_ch[0]] == '+' and user == (int(mss_num[0]) + int(mss_num[1])):
# # #   print('OK')
# # # else:
# # #   print('NO')


# # # with open('t.txt', 'r') as file:
# # #   for line in file:
# # #       print(line)

# # # ========================================================WORDLE

# # # wordle = 'START'
# # # word_list = []


# # # for i in wordle:
# # #   word_list.append(i)

# # # field = ['[_]','[_]','[_]','[_]','[_]']

# # # for j in range(5):
# # #   for i in range(len(word_list)):
# # #     user_input = input(f"\nPlease enter {i+1} letter:").upper()
# # #     if user_input == word_list[i]:
# # #       print("Correct")
# # #       field[i] = f'[{user_input}]'
# # #     elif user_input in word_list and user_input != word_list[i]:
# # #       print("Yellow")
# # #       while user_input in word_list and user_input != word_list[i]:
# # #         user_input = input(f"\nPlease enter {i+1} letter:").upper()
# # #         print("Yellow")
# # #     else: 
# # #       print("Try again")
# # #     for i in field:
# # #       print(i, end='')
# # # VERSION1 =========================================================

# # import random

# # def fill_pole(pole, size_i,size_j):
# #     for i in range(size_i):
# #         pole.append([])
# #         for _ in range(size_j):
# #             pole[i].append('[_]')


# # def show_pole(pole, size_i, size_j):
# #     for i in range(size_i):
# #         for j in range(size_j):
# #             print(pole[i][j],' ', end='')
# #         print('')

# # def win(pole_user, pole_bot, symbol_damage):
# #   user_strike = 0
# #   bot_strike = 0
# #   total_ship_cells = 4+6+6+4

# #   for i in pole_bot:
# #     for j in i:
# #       if j == symbol_damage:
# #         user_strike += 1
        
# #     for a in pole_user:
# #       for b in a:
# #         if b == symbol_damage:
# #           bot_strike += 1
          
# #       if user_strike == total_ship_cells:
# #           print("User won")
# #           return True
# #       elif bot_strike == total_ship_cells:
# #           print("Bot won")
# #           return True
# #       elif user_strike == bot_strike and user_strike > 0:
# #           print("It's a tie")
# #           return True
# #       return False
    
# # def check_fill_ships():
# #     pass

# # def hand_fill_ships(pole, size_i, size_j, deck_total, deck_lenght):
# #   deck_counter = 0
# #   # 4 однопалубных корабля - 4 
# #   # 3 двухпалубных корабля - 6 
# #   # 2 трехпалубных корабля - 6 
# #   # 1 четырехпалубный корабль - 4 

# #   while deck_counter < deck_total:
# #       show_pole(pole, size_i, size_j)
# #       user_ship_i = int(input(f"(user_ship_i) X,   {deck_lenght} deck(s), {deck_counter+1} out of {deck_total} :"))
# #       user_ship_j = int(input(f"(user_ship_j) Y,  {deck_lenght}, {deck_counter+1} deck(s) out of {deck_total} :"))
# #       if deck_lenght > 1:
# #         user_direction = input("H or V:").upper()
# #         deck_counter += 1
# #         if user_direction == 'H':
# #                 if pole[user_ship_i][user_ship_j] == '[_]':
# #                     for i in range(deck_lenght):    
# #                         pole[user_ship_i][user_ship_j+i] = '[#]'
# #         elif user_direction == 'V':
# #             if pole[user_ship_i][user_ship_j] == '[_]':
# #                 for k in range(deck_lenght):    
# #                     pole[user_ship_i+k][user_ship_j] = '[#]'
# #         else: 
# #             print("!1")
# #       elif deck_lenght == 1:
# #           if pole[user_ship_i][user_ship_j] == '[_]':
# #             pole[user_ship_i][user_ship_j] = '[#]'
# #             deck_counter += 1
# #           else:
# #             print("!2")

# # # =================================================================
# # # def rand_fill_ships(pole_bot, ship_number, ship_size):
# # #     # if ship_size == 1:
# # #         for i in range(ship_number):
# # #             rand_i = random.randint(0, size_i - 1)
# # #             rand_j = random.randint(0, size_j- 1)
# # #             if pole_bot[rand_i][rand_j] == '[_]':
# # #                pole_bot[rand_i][rand_j] = '[#]'

# # #                x_cells = [(rand_i + 1, rand_j), (rand_i, rand_j +1), (rand_i - 1, rand_j), (rand_i, rand_j - 1), (rand_i + 1, rand_j), (rand_i + 1, rand_j+1), (rand_i - 1, rand_j-1), (rand_i + 1, rand_j-1), (rand_i - 1, rand_j + 1)]
            
# # #                for i,j  in x_cells:
# # #                     if 0 <= i < size_i  and 0 <=j < size_j :
# # #                         if pole_bot[i][j] == '[_]':
# # #                          pole_bot[i][j] = '[X]'
# # # ================================================================ 
# # def rand_fill_ships(pole_bot, ship_number, ship_size):
# #           deck_counter = 0

# #           while deck_counter < ship_number:
# #               rand_i = random.randint(0, size_i - 1)
# #               rand_j = random.randint(0, size_j- 1)
# #               if ship_size > 1:
# #                 direction = random.choice(['H', 'V'])
# #                 if direction == 'H':
# #                         if pole_bot[rand_i][rand_j] == '[_]' and 0 <= rand_i < size_i and 0 <= rand_j < size_j and pole_bot[rand_i][rand_j+1] != '[#]' and pole_bot[rand_i+1][rand_j] != '[#]' and pole_bot[rand_i][rand_j-1] != '[#]' and pole_bot[rand_i-1][rand_j] != '[#]':
# #                             for i in range(ship_size):    
# #                                 pole_bot[rand_i][rand_j+i] = '[#]'
# #                 elif direction == 'V':
# #                         if pole_bot[rand_i][rand_j] == '[_]' and 0 <= rand_i < size_i and 0 <= rand_j < size_j and pole_bot[rand_i][rand_j+1] != '[#]' and pole_bot[rand_i+1][rand_j] != '[#]' and pole_bot[rand_i][rand_j-1] != '[#]' and pole_bot[rand_i-1][rand_j] != '[#]':
# #                             for k in range(ship_size):    
# #                                 pole_bot[rand_i+k][rand_j] = '[#]'
# #                 deck_counter += 1


# #               elif ship_size == 1:
# #                   if pole_bot[rand_i][rand_j] == '[_]' and 0 < rand_i < size_i and 0 < rand_j < size_j:
# #                     pole_bot[rand_i][rand_j] = '[#]'
# #                     deck_counter += 1
# #                   else:
# #                     print("!2")

    
# # def save_game(pole, filename):
# #   if pole == pole_user: 
# #     user_save = input("If you want to save the save, press 'S', if no, press 'N':").lower()
# #     if user_save == 's':
# #         with open(filename, 'w') as file:
# #           for i in pole:
# #               for j in i:
# #                   file.write(j)  
# #               file.write('\n')        
# #         print("Game saved")

# #         with open(filename, 'r') as file:
# #             game_save = file.read()
# #             print("Bot game", '\n')
# #             print(game_save)

# #         load_game('pole_user.txt', pole_user)
# #         load_game('pole_bot.txt', pole_bot)
# #     elif user_save == 'n':
# #           pass
# #     else:
# #           print('!')
# #   else:
# #       with open(filename, 'w') as file:
# #             for i in pole:
# #                 for j in i:
# #                     file.write(j)  
# #                 file.write('\n')        

# #       with open(filename, 'r') as file:
# #               game_save = file.read()
# #               print(game_save)  

# # def load_game(filename, pole):
# #     if pole == pole_user:
# #         user_load = input("If you want to load your saved game, press 'L'; if not, press 'N': ").lower()
# #         if user_load == 'n':
# #             return None
# #         elif user_load != 'l':
# #             print("Invalid input!")
# #             return load_game(filename, pole)

# #     file = open(filename, 'r')
# #     lines = file.readlines()
# #     file.close()

# #     pole = []

# #     for i in lines:
# #         row = []
# #         cell = ''
# #         for j in i:
# #             cell += j
# #             if j == ']': 
# #                 if j in ('[_]', '[#]', '[%]', '[@]'):
# #                     row.append(j)
# #                 j = '' 
# #         if len(row) > 0:
# #             pole.append(row)

# #     return pole
    

# # def user_figth(pole,size_i, size_j, symbol_ship, symbol_damage, symbol_empty, symbol_miss):
# #     while True:
# #         user_i = input('user_i: ')
# #         user_j = input('user_j: ')
# #         if  not user_i.isdigit() or not user_j.isdigit():
# #           print("!")
# #         user_i = int(user_i)  
# #         user_j = int(user_j) 

# #         if pole[user_i][user_j] == symbol_ship:
# #             pole[user_i][user_j] = symbol_damage
# #         elif pole[user_i][user_j] == symbol_empty:
# #             pole[user_i][user_j] = symbol_miss
# #             break
 

# # def bot_figth(pole, size_i, size_j, symbol_ship, symbol_damage, symbol_empty, symbol_miss):
# #     while True:
# #         rand_i = random.randint(0, size_i-1)
# #         rand_j = random.randint(0, size_j - 1)
# #         if pole[rand_i][rand_j] == symbol_ship:
# #             pole[rand_i][rand_j] = symbol_damage
# #         elif pole[rand_i][rand_j] == symbol_empty:
# #             pole[rand_i][rand_j] = symbol_miss
# #             break


# # pole_user = []
# # pole_bot = []
# # size_i, size_j = 10,10

# # symbol_ship = '[#]'
# # symbol_damage = '[%]'
# # symbol_empty = '[_]'
# # symbol_miss = '[@]'

# # fill_pole(pole_user, size_i, size_j)
# # fill_pole(pole_bot, size_i, size_j)

# # hand_fill_ships(pole_user, size_i, size_j, 4, 1)
# # hand_fill_ships(pole_user, size_i, size_j, 3, 2)
# # hand_fill_ships(pole_user, size_i, size_j, 2, 3)
# # hand_fill_ships(pole_user, size_i, size_j, 1, 4)

# # while True:
# #     for i in range(3):
#         # # print('pole_user:')
#         # show_pole(pole_user, size_i, size_j)
#         # # print()
#         # print('pole_bot:')
# #         # print("===========================================")
# # rand_fill_ships(pole_bot, 1, 4)
# # rand_fill_ships(pole_bot, 2, 3)
# # rand_fill_ships(pole_bot, 3, 2)

# # show_pole(pole_bot, size_i, size_j)
#         # user_figth(pole_bot, size_i, size_j, symbol_ship, symbol_damage, symbol_empty, symbol_miss)
#         # bot_figth(pole_user, size_i, size_j, symbol_ship, symbol_damage, symbol_empty, symbol_miss)
#         # if i == 2:
#         #     save_game(pole_user, 'pole_user.txt')
#         #     save_game(pole_bot, 'pole_bot.txt')


#     # if win(pole_user, pole_bot, symbol_damage):
#     #   break
#     # break

# # ship = [#]
# # [_]
# # [@]
# # [%]
# # ===================================================================

# # def indexes(lst):
# #     indexes_list = []
# #     for i in range(len(lst)):
# #         indexes_list.append(i)
# #     return indexes_list

# # with open ('part_1', 'r') as file:
# #     file_1 = file.read()
# #     list_1 = []
# #     tmp = ''
# #     for i in file_1:
# #         if i != '\n':
# #          tmp += i
# #         else:
# #             list_1.append(tmp)
# #             tmp= ''
# #     if tmp:
# #              list_1.append(tmp)
# #     for i in indexes(list_1):
# #         print(list_1[i], '-', i+1)
        
    
# # def user_choice(list_1):
# #     selected = []
# #     word = ''
# #     bad_words = ['jerk', 'darn', 'heck']


# #     while True:
# #         user_input = input('Select the part want to join or press 0 to exit:')
# #         if not user_input.isdigit():
# #             print('!')
# #         else:
# #             user_input = int(user_input) - 1
# #             if user_input == -1:
# #                 break
# #             selected.append(list_1[user_input])
            
# #     for i in selected:
# #         word += i
# #     print(word, end = '')
# #     if word in bad_words:
# #         print("\n!")
# #     return word

# # word = user_choice(list_1)
# # with open ('new.txt', 'w') as file:
# #   file.write(word)
# # VERSION 2 ================================================
# # import random

# # def fill_pole(pole, size_i, size_j):
# #     for i in range(size_i):
# #         pole.append([])
# #         for _ in range(size_j):
# #             pole[i].append('[_]')


# # def show_pole(pole, size_i, size_j):
# #     for i in range(size_i):
# #         for j in range(size_j):
# #             print(pole[i][j],' ', end='')
# #         print('')


# # def win(pole_user, pole_bot, symbol_damage):
# #     user_strike = 0
# #     bot_strike = 0
# #     total_ship_cells = 4+6+6+4

# #     for i in pole_bot:
# #         for j in i:
# #             if j == symbol_damage:
# #                 user_strike += 1

# #     for a in pole_user:
# #         for b in a:
# #             if b == symbol_damage:
# #                 bot_strike += 1
# #     if user_strike == total_ship_cells and bot_strike == total_ship_cells:
# #         print("Tie!")
# #         return True
# #     if user_strike == total_ship_cells:
# #         print("User won")
# #         return True
# #     if bot_strike == total_ship_cells:
# #         print("Bot won")
# #         return True

# #     return False


# # def hand_fill_ships(pole, size_i, size_j, deck_total, deck_lenght):
# #     deck_counter = 0

# #     while deck_counter < deck_total:
# #         show_pole(pole, size_i, size_j)
# #         user_ship_i = int(input(f"(user_ship_i) X,   {deck_lenght} deck(s), {deck_counter+1} out of {deck_total} :"))
# #         user_ship_j = int(input(f"(user_ship_j) Y,  {deck_lenght}, {deck_counter+1} deck(s) out of {deck_total} :"))
# #         if deck_lenght > 1:
# #             user_direction = input("H or V:").upper()
# #             if user_direction == 'H':
# #                 if user_ship_j + deck_lenght <= size_j:
# #                     for i in range(deck_lenght):
# #                         if pole[user_ship_i][user_ship_j+i] != '[_]':
# #                             break
# #                     else:
# #                         for i in range(deck_lenght):
# #                             pole[user_ship_i][user_ship_j+i] = '[#]'
# #                         deck_counter += 1
# #             elif user_direction == 'V':
# #                 if user_ship_i + deck_lenght <= size_i:
# #                     for k in range(deck_lenght):
# #                         if pole[user_ship_i+k][user_ship_j] != '[_]':
# #                             break
# #                     else:
# #                         for k in range(deck_lenght):
# #                             pole[user_ship_i+k][user_ship_j] = '[#]'
# #                         deck_counter += 1
# #             else:
# #                 print("!")
# #         else:
# #             if pole[user_ship_i][user_ship_j] == '[_]':
# #                 pole[user_ship_i][user_ship_j] = '[#]'
# #                 deck_counter += 1
# #             else:
# #                 print("!")


# # def rand_fill_ships(pole_bot, ship_number, ship_size):
# #     deck_counter = 0
# #     while deck_counter < ship_number:
# #         rand_i = random.randint(0, size_i - 1)
# #         rand_j = random.randint(0, size_j - 1)
# #         direction = random.choice(['H', 'V'])

# #         if ship_size == 1:
# #             if pole_bot[rand_i][rand_j] == '[_]':
# #                 pole_bot[rand_i][rand_j] = '[#]'
# #                 deck_counter += 1
# #         else:
# #             if direction == 'H' and rand_j + ship_size <= size_j:
# #                 for i in range(ship_size):
# #                     if pole_bot[rand_i][rand_j + i] != '[_]':
# #                         break
# #                 else:
# #                     for i in range(ship_size):
# #                         pole_bot[rand_i][rand_j + i] = '[#]'
# #                     deck_counter += 1
# #             elif direction == 'V' and rand_i + ship_size <= size_i:
# #                 for i in range(ship_size):
# #                     if pole_bot[rand_i + i][rand_j] != '[_]':
# #                         break
# #                 else:
# #                     for i in range(ship_size):
# #                         pole_bot[rand_i + i][rand_j] = '[#]'
# #                     deck_counter += 1


# # def save_game(pole, filename):
# #   if pole == pole_user: 
# #     user_save = input("If you want to save the save, press 'S', if no, press 'N':").lower()
# #     if user_save == 's':
# #         with open(filename, 'w') as file:
# #           for i in pole:
# #               for j in i:
# #                   file.write(j)  
# #               file.write('\n')        
# #         print("Game saved")

# #         with open(filename, 'r') as file:
# #             game_save = file.read()
# #             print("Bot game", '\n')
# #             print(game_save)

# #         load_game('pole_user.txt', pole_user)
# #         load_game('pole_bot.txt', pole_bot)
# #     elif user_save == 'n':
# #           pass
# #     else:
# #           print('!')
# #   else:
# #       with open(filename, 'w') as file:
# #             for i in pole:
# #                 for j in i:
# #                     file.write(j)  
# #                 file.write('\n')        

# #       with open(filename, 'r') as file:
# #               game_save = file.read()
# #               print(game_save)  


# # def load_game(filename, pole):
# #     if pole == pole_user:
# #         user_load = input("If you want to load your saved game, press 'L'; if not, press 'N': ").lower()
# #         if user_load == 'n':
# #             return None
# #         elif user_load != 'l':
# #             print("!")
# #             return load_game(filename, pole)

# #     file = open(filename, 'r')
# #     lines = file.readlines()
# #     file.close()

# #     pole = []

# #     for i in lines:
# #         row = []
# #         cell = ''
# #         for j in i:
# #             cell += j
# #             if j == ']': 
# #                 if j in ('[_]', '[#]', '[%]', '[@]'):
# #                     row.append(j)
# #                 j = '' 
# #         if len(row) > 0:
# #             pole.append(row)

# #     return pole


# # def user_figth(pole, size_i, size_j, symbol_ship, symbol_damage, symbol_empty, symbol_miss):
# #     user_stat = 0
# #     while True:
# #         user_i = input('user_i: ')
# #         user_j = input('user_j: ')
# #         if not user_i.isdigit() or not user_j.isdigit():
# #             print("!")
# #             continue
# #         user_i = int(user_i)
# #         user_j = int(user_j)

# #         if pole[user_i][user_j] == symbol_ship:
# #             pole[user_i][user_j] = symbol_damage
# #             user_stat += 1
# #             return user_stat
# #         if pole[user_i][user_j] == symbol_empty:
# #             pole[user_i][user_j] = symbol_miss
# #             user_stat += 1
# #             return user_stat
        

# # def bot_figth(pole, size_i, size_j, symbol_ship, symbol_damage, symbol_empty, symbol_miss):
# #     bot_stat = 0
# #     while True:
# #         rand_i = random.randint(0, size_i - 1)
# #         rand_j = random.randint(0, size_j - 1)
# #         if pole[rand_i][rand_j] == symbol_ship:
# #             pole[rand_i][rand_j] = symbol_damage
# #             bot_stat += 1
# #             return bot_stat
# #         if pole[rand_i][rand_j] == symbol_empty:
# #             pole[rand_i][rand_j] = symbol_miss
# #             bot_stat += 1
# #             return bot_stat
        

# # def statistics(user_total, bot_total):
# #     with open ('stat.txt', 'a') as file:
# #         file.write(f"user:{user_total}")
# #         file.write(f"bot:{bot_total}")
# #     print(f"Stats: {user_total}, {bot_total}")


# # # ==================================================
# # pole_user = []
# # pole_bot = []
# # size_i, size_j = 10, 10

# # symbol_ship = '[#]'
# # symbol_damage = '[%]'
# # symbol_empty = '[_]'
# # symbol_miss = '[@]'

# # fill_pole(pole_user, size_i, size_j)
# # fill_pole(pole_bot, size_i, size_j)

# # rand_fill_ships(pole_bot, 1, 4)
# # rand_fill_ships(pole_bot, 2, 3)
# # rand_fill_ships(pole_bot, 3, 2)
# # rand_fill_ships(pole_bot, 4, 1)

# # hand_fill_ships(pole_user, size_i, size_j, 1, 4)
# # hand_fill_ships(pole_user, size_i, size_j, 2, 3)
# # hand_fill_ships(pole_user, size_i, size_j, 3, 2)
# # hand_fill_ships(pole_user, size_i, size_j, 4, 1)

# # user_total = 0
# # bot_total = 0
# # while True:
# #     user_total += user_figth(pole_bot, size_i, size_j,
# #          symbol_ship, symbol_damage, symbol_empty, symbol_miss)
# #     bot_total += bot_figth(pole_user, size_i, size_j,
# #        symbol_ship, symbol_damage, symbol_empty, symbol_miss)
# #     if win(pole_user, pole_bot, symbol_damage):
# #         statistics(user_total, bot_total)
# #         break
# #=== 11.17.25 NEW DAY ===============================================    
# # try:
# #     num = int(input(': '))
# #     print(10/num)
# # except ValueError:
# #     print('no number')
# # except ZeroDivisionError:
# #     print('del 0')
# # finally:
# #     print('ok')

# # def sounds(user_text):
# #         user_text = input("Pls enter ur text here:")
# #         vowels = []
# #         for i in user_text:
# #                 if i in ['a', 'e', 'u', 'i', 'o', 'y']:
# #                  vowels.append(i)
# #         result = len(vowels)
# #         return result

# # # def calc(num1, operator, num2)# :
# #         t# ry:
# #                 # num1 = int(input("Pls enter ur 1st numbe# r:"))
# #                 # operator = input("Pls enter the operator a valid operators ('+', '-','/', '*', or ^(to raise to a po# wer):")
# #                 # num2 = int(input("Pls enter ur 2nd number or power to which u want to raise the n# umber:"))
# #                #  result = 0
# #                 if ope# rator == '+':
# #                         resul# t = num1 + num2
# #                 elif#  operator == '-':
# #                         r# esult = num1 - num2
# #                 # elif operator == '*':
# #                      #    result = num1 * num2
# #             #     elif operator == '/':
# #                  #        result = num1 / num2
# #         #         elif operator == '^':
# #               #           result = num1 ** num2
# #                #  print(f'The result is {result# }')
# #                 retur# n result
# #         except ValueError:
# #     #         print('Please enter a numb# er!')
# #         except ZeroDivisionError:
# #             print('Division by zero is not allowed!') 


import secrets


welcome_word = "Welcome to the random password generator. You can select the lenght and the type of charachers used. If you want to use only symbols for your password - press 'S', if you want to use only letters - press 'L', for numbers - 'N'. Press 'C' for the combination of all the above.\n"

print(welcome_word)


symbols = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = "0123456789"

try:
    user_lenght = int(input("Please select the lenght of your password:"))
    user_choice = (input("Please select one: symbols - 'S', letters - 'L', numbers - 'N', or combination of them all - 'C':")).lower()
    password = ''
    pass_char = ''
    if user_choice == 's':
      pass_char = symbols
    elif user_choice == 'l':
      pass_char = alphabet
    elif user_choice == 'n':
      pass_char = numbers
    elif user_choice == 'c':
      pass_char = symbols + alphabet + numbers
    
    for i in range(user_lenght):
        password += secrets.choice(pass_char)
        print(f"Your password is {password}")
except ValueError:
    print("Please enter a number")

