from copy import deepcopy
from typing import List
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
        self.game_id=game_id
        self.field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.sequence_of_turns: List[TicTacToeTurn] = []
        self.first_player_id=first_player_id
        self.second_player_id=second_player_id
        self.winner_id=""

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.winner_id == "":
            if -1 < turn.x_coordinate < 3 and -1 < turn.y_coordinate < 3:
                if self.field[turn.x_coordinate][turn.y_coordinate] != "X" and \
                        self.field[turn.x_coordinate][turn.y_coordinate] != "O":
                    if turn.player_id != self.first_player_id and \
                            self.sequence_of_turns == []:
                        return False
                    if (turn.player_id == self.first_player_id and \
                            self.sequence_of_turns == []):
                        return True
                    if turn.player_id == self.first_player_id and \
                            self.sequence_of_turns[-1].player_id == self.second_player_id:
                        return True
                    if turn.player_id == self.second_player_id and \
                            self.sequence_of_turns[-1].player_id == self.first_player_id:
                        return True
        return False

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn):
            if turn.player_id == self.first_player_id:
                self.field[turn.x_coordinate][turn.y_coordinate] = "X"
                self.sequence_of_turns.append(deepcopy(turn))
            if turn.player_id == self.second_player_id:
                self.field[turn.x_coordinate][turn.y_coordinate] = "O"
                self.sequence_of_turns.append(deepcopy(turn))
            draw = True

            for i in range(3):
                row1 = []
                row2 = []

                for j in range(3):
                    row1.append(self.field[i][j])
                    row2.append(self.field[j][i])

                if row1 == ["X"] * 3 or row2 == ["X"] * 3:
                    self.winner_id = self.first_player_id
                    return self.get_game_info()

                if row1 == ["O"] * 3 or row2 == ["O"] * 3:
                    self.winner_id = self.second_player_id
                    return self.get_game_info()

                if ("X" not in row1) or ("X" not in row2) or ("O" not in row1) or ("O" not in row2):
                    draw = False

            row1 = []
            row2 = []

            for i in range(3):
                row1.append(self.field[i][i])
                row2.append(self.field[i][2 - i])

            if row1 == ["X"] * 3 or row2 == ["X"] * 3:
                self.winner_id = self.first_player_id
                return self.get_game_info()

            if row1 == ["O"] * 3 or row2 == ["O"] * 3:
                self.winner_id = self.second_player_id
                return self.get_game_info()

            if ("X" not in row1) or ("X" not in row2) or ("O" not in row1) or ("O" not in row2):
                draw = False

            if draw:
                self.winner_id = "Draw"
        return self.get_game_info()

    def get_game_info(self) -> TicTacToeGameInfo:
        game = TicTacToeGameInfo(
            game_id=self.game_id,
            field=deepcopy(self.field),
            sequence_of_turns=deepcopy(self.sequence_of_turns),
            first_player_id=self.first_player_id,
            second_player_id=self.second_player_id,
            winner_id=self.winner_id
        )
        return game
