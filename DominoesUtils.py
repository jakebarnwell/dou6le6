import random

dominoes = []
for i in range(7):
    for j in range(i+1):
        dominoes.append([j, i])

def extract_game(game_data):
    game_dict = {
        'name'                : game_data[0],
        'is_private'          : game_data[1],
        'has_started'         : game_data[2],
        'players_list'        : game_data[3],
        'players_dominoes'    : game_data[4],
        'current_player'      : game_data[5],
        'last_move_timestamp' : game_data[6],
        'is_over'             : game_data[7],
        'left_dominoes'       : game_data[8],
        'right_dominoes'      : game_data[9],
        'starting_domino'     : game_data[10],
        'num_of_each_domino'  : game_data[11]
    }
    return game_dict

def encode_game(game_dict):
    game_data = [game_dict['name'],
                 game_dict['is_private'],
                 game_dict['has_started'],
                 game_dict['players_list'],
                 game_dict['players_dominoes'],
                 game_dict['current_player'],
                 game_dict['last_move_timestamp'],
                 game_dict['is_over'],
                 game_dict['left_dominoes'],
                 game_dict['right_dominoes'],
                 game_dict['starting_domino'],
                 game_dict['num_of_each_domino']
                ]
    return game_data

def not_passable(rand_dominoes):
    if rand_dominoes == dominoes:
        return False
    
    for i in range(4):
        player_hand = rand_dominoes[7*i:7*(i+1)]
        count_doubles = 0
        for domino in player_hand:
            count_doubles += (domino[0] == domino[1]) # 1 if double, 0 if not
        if count_doubles >= 5:
            return False
    return True

def randomize_dominoes():
    rand_dominoes = dominoes[:]
    while not_passable(rand_dominoes):
        rand_dominoes = random.shuffle(rand_dominoes)
    return rand_dominoes

def join_game(game_dict, user_id):
    players = game_dict['players_list'] 
    players.append(user_id)
    game_dict['players_list'] = players
    return game_dict

def initialize_game(game_dict):
    rand_dominoes = randomize_dominoes()
    players_hands = []
    for i in range(4):
        player_hands.append(rand_dominoes[7*i:7*i+7])
    ## Initialize Game
    game_dict['players_dominoes'] = players_hands
    return game_dict


def play_domino(game, user_id, direction, domino):

    if domino == "PASS":
	pass
    else:
        if direction == “L”:
            if len(game[“left_dominos”]) >0:
                l_domino_num = str(game[“left_dominos”][-1][-1])
            else:
                l_domino_num = str(game[“starting_domino”][-1])

            if domino[0] == l_domino_num:
                game[“left_dominos”].append([int(domino[0]), int(domino[1])])
            else:
                game[“left_dominos”].append([int(domino[1]), int(domino[0])])

        elif direction == “R”:
            if len(game[“right_dominos”]) >0:
                r_domino_num = str(game[“right_dominos”][-1][-1])
            else:
                r_domino_num = str(game[“starting_domino”][-1])

            if domino[0] == r_domino_num:
                game[“right_dominos”].append([int(domino[0]), int(domino[1])])
            else:
                game[“right_dominos”].append([int(domino[1]), int(domino[0])])

    game[“current_player”] = (game[“current_player”] + 1) % 4 +1

    return game
            
