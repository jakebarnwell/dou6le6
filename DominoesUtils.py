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
        'pin'                 : game_data[3],
        'players_info'        : game_data[4],
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
                 game_dict['pin'],
                 game_dict['players_info'],
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
        player = rand_dominoes[7*i:7*(i+1)]
        count_doubles = 0
        for double in player:
            
    
    

def randomize_dominoes():
    rand_dominoes = dominoes[:]
    while not_passable(rand_dominoes):
        rand_dominoes = random.shuffle(rand_dominoes)
    return rand_dominoes

def initialize_game(game_dict):
    ## Initialize Game
    return game_dict