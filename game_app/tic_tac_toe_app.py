from typing import Dict
from uuid import uuid4
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


class TicTacToeGameNotFoundException(Exception):
    """game not found :)"""


class TicTacToeApp:
    def __init__(self):
        """пока не знаю, мб что-то ещё тут будет :)
        в обоих случаях айдишник - ключ, значение - угадайте, что)"""
        self._games: Dict[str, TicTacToeGame] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        game_id = uuid4().hex
        game = TicTacToeGame(game_id, first_player_id, second_player_id)
        self._games[game_id] = game
        return game.get_game_info()

    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        game = self._games.get(game_id)
        if game:
            return game.get_game_info()
        raise TicTacToeGameNotFoundException(f"no game with id={game_id}")

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        game = self._games.get(game_id)
        if game:
            return game.do_turn(turn)
        raise TicTacToeGameNotFoundException(f"no game with id={game_id}")
