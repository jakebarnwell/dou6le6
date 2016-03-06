from FirebaseWrapper import *
import json

firebase_url = 'https://dou6le6.firebaseio.com/'
firebase_db = '/dou6le6'

fb = FirebaseWrapper(firebase_url, firebase_db)

def conv_to_python(game_data):
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

def conv_to_firebase(game_data):
    python_list = 

def initialize_game(game_id):
    game_key = 'game_' + str(game_id)
    unicode_response = fb.get_data(game_key)
    game_data = json.loads(unicode_response)
    game_dict = conv_to_python(game_data)
    return game_dict

game = initialize_game('1029143930')
print(game)