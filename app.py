from flask import Flask, request, abort

from game_app import TicTacToeApp, TicTacToeGameNotFoundException

from game_engine import TicTacToeTurn


app = Flask(__name__)
t_app = TicTacToeApp()
t_app.start_game('1', '2')
users=[]
games=[]

@app.route('/')
def hello_world():
    return list(t_app._games.keys())[0]

@app.route('/game_info', methods=['GET'])
def get_game_info():
    game_id = request.args.get('game_id')
    if game_id:
        try:
            game_info = t_app.get_game_by_id(game_id).to_json()
        except TicTacToeGameNotFoundException:
            abort(404)
        return game_info
    abort(400)

@app.route('/do_turn', methods=['POST'])
def do_turn():
    turn = TicTacToeTurn.from_dict(request.json["turn"])
    #turn = TicTacToeTurn(request.json["turn"]["player_id"], request.json["turn"]["x_coordinate"], request.json["turn"]["y_coordinate"])
    game_id = request.args.get('game_id')
    if game_id:
        try:
            game = t_app.do_turn(turn, game_id).to_json()
        except TicTacToeGameNotFoundException:
            abort(404)
        return game
    abort(400)

@app.route('/registration', methods=['POST'])
def registration():
    user_id = request.json["user_id"]
    if user_id not in users:
        if user_id != 'draw' and user_id != 'Draw' and user_id != 'DRAW' and user_id != '' and ' ' not in user_id :
            users.append(user_id)
            return user_id
    else:
        abort(404)


@app.route('/start_game', methods=['POST'])
def start_game():
    first_player_id = request.json["first_player_id"]
    second_player_id = request.json["second_player_id"]
    new_game = t_app.start_game(first_player_id, second_player_id).to_json()
    games.append(new_game)
    return new_game