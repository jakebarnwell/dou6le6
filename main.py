from flask import Flask
from FirebaseWrapper import *
import DominoesUtils as Utils

## Firebase Settings
firebase_url = 'https://dou6le6.firebaseio.com/'
firebase_db = '/dou6le6'

## Set up Firebase Wrapper
fb = FirebaseWrapper(firebase_url, firebase_db)

app = Flask(__name__)

@app.route('/game/<game_id>')
def initialize(game_id):
    fb_game_key = 'game_' + str(game_id)
    fb_get_response = fb.get_data(fb_game_key)
    python_game = Utils.extract_game(fb_get_response)
    
    game = Utils.initialize_game(python_game)
    
    fb_post_game = Utils.encode_game(game)
    fb_post_response = fb.write_data(fb_game_key, fb_post_game)
    return fb_post_response

if __name__ == '__main__':
    app.run()