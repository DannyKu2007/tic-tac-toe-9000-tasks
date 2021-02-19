from game_engine import TicTacToeGame, TicTacToeTurn

first_player_id = str(input())
second_player_id = str(input())
game_id = "7139"
game = TicTacToeGame(game_id, first_player_id, second_player_id)
number_player = ""
player_id = ""
while game.get_game_info().winner_id == "" and len(game.get_game_info().sequence_of_turns) < 9:
    if game.get_game_info().sequence_of_turns == []:
        player_id = first_player_id
    else:
        if game.get_game_info().sequence_of_turns[-1].player_id==second_player_id:
            player_id = first_player_id
        else:
            if game.get_game_info().sequence_of_turns[-1].player_id==first_player_id:
                player_id = second_player_id
    x_coordinate, y_coordinate = map(int, input().split())
    turn = TicTacToeTurn(player_id,x_coordinate,y_coordinate)
    if game.is_turn_correct(turn) == True:
        game.do_turn(turn)
        print(game.get_game_info())
