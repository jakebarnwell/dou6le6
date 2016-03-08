from flask import Flask
from FirebaseWrapper import *
import DominoesUtils as Utils

## Firebase Settings
firebase_url = 'https://dou6le6.firebaseio.com/'
firebase_db = '/dou6le6'

## Set up Firebase Wrapper
fb = FirebaseWrapper(firebase_url, firebase_db)

app = Flask(__name__)

@app.route('/')
def app_status():
    html_str = "<html><head><title>DB Info</title></head><body>"
    fb_users_key = "USERS"
    fb_get_response = fb.get_data(fb_users_key)
    html_str += "<h1>Users</h1>"
    html_str += str(fb_get_response)
    html_str += "<br> <br>"
    html_str += "<h1>Games</h1>"
    fb_get_response = fb.get_data("PUBLIC_GAMES")    
    html_str += str(fb_get_response)
    html_str += "</body></html>"
    return html_str

@app.route('/game/join/<int:game_id>/<int:user_id>')
def join(game_id, user_id):
    fb_game_key = 'game_' + str(game_id)
    fb_get_response = fb.get_data(fb_game_key)
    python_game = Utils.extract_game(fb_get_response)

    game = Utils.join_game(python_game, user_id)    
    
    if len(game['players_list']) == 4:
        game['has_started'] = True
	game = Utils.initialize_game(game)
    
    fb_post_game = Utils.encode_game(game)
    fb_post_response = fb.write_data(fb_game_key, fb_post_game)
    return fb_post_response

@app.route('/game/<game_id>')
def initialize(game_id):
    fb_game_key = 'game_' + str(game_id)
    fb_get_response = fb.get_data(fb_game_key)
    python_game = Utils.extract_game(fb_get_response)
    
    game = Utils.initialize_game(python_game)
    
    fb_post_game = Utils.encode_game(game)
    fb_post_response = fb.write_data(fb_game_key, fb_post_game)
    return fb_post_response

@app.route('/game/<game_id>/<user_id>/play/<direction>/<domino>')
def play_domino(game_id, user_id, direction, domino):
    fb_game_key = 'game_' + str(game_id)
    fb_get_response = fb.get_data(fb_game_key)
    python_game = Utils.extract_game(fb_get_response)
    
    game = Utils.play_domino(python_game, str(user_id), str(direction), str(domino))

    fb_post_game = Utils.encode_game(game)
    fb_post_response = fb.write_data(fb_game_key, fb_post_game)
    return fb_post_response

@app.route('/game/isGameOver/<game_id>/')
def is_game_over(game_id):
    fb_game_key = 'game_' + str(game_id)
    fb_get_response = fb.get_data(fb_game_key)
    python_game = Utils.extract_game(fb_get_response)

    game = Utils.is_game_over(python_game)

    fb_post_game = Utils.encode_game(game)
    fb_post_response = fb.write_data(fb_game_key, fb_post_game)
    return fb_post_response


if __name__ == '__main__':
    app.run()
