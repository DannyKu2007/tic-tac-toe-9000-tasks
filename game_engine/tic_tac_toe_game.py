from copy import deepcopy
from typing import Callable, List, Optional
from game_engine import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    """Наследуемся от абстрактного класса и реализуем ручками все методы"""

    def __init__(
            self,
            game_id: str,
            first_player_id: str,
            second_player_id: str,
            # strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None
    ) -> None:
        self.game = TicTacToeGameInfo(
            game_id=game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=[],
            first_player_id=first_player_id,
            second_player_id=second_player_id,
            winner_id=""
        )

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.game.winner_id == "":
            if -1 < turn.x_coordinate < 3 and -1 < turn.y_coordinate < 3:
                if self.game.field[turn.x_coordinate][turn.y_coordinate] != "X" and \
                        self.game.field[turn.x_coordinate][turn.y_coordinate] != "O":
                    if turn.player_id != self.game.first_player_id and \
                            self.game.sequence_of_turns == []:
                        return False
                    if (turn.player_id == self.game.first_player_id and \
                            self.game.sequence_of_turns == []):
                        return True
                    else:
                        if turn.player_id == self.game.first_player_id and \
                                self.game.sequence_of_turns[-1].player_id == self.game.second_player_id:
                            return True
                        if turn.player_id == self.game.second_player_id and \
                                self.game.sequence_of_turns[-1].player_id == self.game.first_player_id:
                            return True
        return False

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) == True:
            if turn.player_id == self.game.first_player_id:
                self.game.field[turn.x_coordinate][turn.y_coordinate] = "X"
                self.game.sequence_of_turns.append(deepcopy(turn))
            if turn.player_id == self.game.second_player_id:
                self.game.field[turn.x_coordinate][turn.y_coordinate] = "O"
                self.game.sequence_of_turns.append(deepcopy(turn))
        row1 = ""
        row2 = ""
        for i in range(3):
            row1 += self.game.field[i][i]
            row2 += self.game.field[i][2 - i]
            if row1 == "XXX" or row2 == "XXX":
                self.game.winner_id = self.game.first_player_id
            if row1 == "OOO" or row2 == "OOO":
                self.game.winner_id = self.game.second_player_id
        for i in range(3):
            row1 = ""
            row2 = ""
            for j in range(3):
                row1 += self.game.field[j][i]
                row2 += self.game.field[i][j]
                if row1 == "XXX" or row2 == "XXX":
                    self.game.winner_id = self.game.first_player_id
                if row1 == "OOO" or row2 == "OOO":
                    self.game.winner_id = self.game.second_player_id
        return self.get_game_info()

    def get_game_info(self) -> TicTacToeGameInfo:
        return deepcopy(self.game)

    def state_game(self) -> bool:
        return self.game.winner_id != ""
