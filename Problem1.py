import random
import oxo_data 

class Game:
    def __init__(self):
        self.board = self.new_game()

    def new_game(self):
        return list(" " * 9)

    def save_game(self):
        oxo_data.saveGame(self.board)

    @classmethod
    def restore_game(cls):
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                return cls.from_board(game)
            else:
                return cls()
        except IOError:
            return cls()

    @classmethod
    def from_board(cls, board):
        game_instance = cls()
        game_instance.board = board
        return game_instance

    def _generate_move(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _is_winning_move(self):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def user_move(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self._is_winning_move():
            return 'X'
        else:
            return ""

    def computer_move(self):
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._is_winning_move():
            return 'O'
        else:
            return ""

    def play(self):
        result = ""
        while not result:
            print(self.board)
            try:
                user_cell = self._generate_move()  
                result = self.user_move(user_cell)
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()

            if not result:
                continue
            elif result == 'D':
                print("It's a draw")
            else:
                print("Winner is:", result)
            print(self.board)

if __name__ == "__main__":
    game_instance = Game.restore_game()  
    game_instance.play()
