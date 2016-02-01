__author__ = 'OR'
import signal
import time
import sys

sys.path.append("/Users/or/dev/Snake")

from snake import Snake, CELLS
from apple import Apple


class Game:
    def __init__(self):
        self.snake = Snake()
        self.snake.create_snake()
        self.apple = Apple()
        self.apple.generate_apple(self.snake.body)
        signal.signal(signal.SIGALRM, self.raise_exception)

    def raise_exception(self, sig_num, stack_frame):
        raise KeyboardInterrupt

    def start_game(self):
        self.game_start_print()
        time.sleep(2)
        message = ''
        while True:
            if self.snake.length >= len(CELLS):
                self.game_over_print("Good Game, You WIN.")
                exit(1)
            self.draw_jungle()
            try:
                signal.alarm(2)
                self.snake.get_direction()
                signal.alarm(0)
            except KeyboardInterrupt:
                self.snake.grow_snake()
            if self.snake.current_head in self.snake.body[:-1]:
                message = "You ate yourself. Game Over."
                self.game_over_print(message)
                exit(1)
            elif self.snake.current_head == self.apple.location:
                self.apple.eat_apple()
                self.apple.generate_apple(self.snake.body)
            else:
                continue

    def draw_jungle(self):
        clean_screen = "\n" * 100
        print(clean_screen)
        seperator = '\n{}'.format('=' * 20)
        roof = ' _ _ _ _ _'
        print(seperator)
        print(roof)
        tile = '|{}'
        for idx, cell in enumerate(CELLS):
            content = '_'
            if cell in self.snake.body:
                content = 'o'
                if cell == self.snake.body[-1]:
                    content = 's'
            if cell == self.apple.location:
                content = '*'
            if idx + 1 in [5, 10, 15, 20, 25]:
                print_line += tile.format(content + '|')
                print(print_line)
            elif idx + 1 in [1, 6, 11, 16, 21]:
                print_line = ''
                print_line += tile.format(content)
            else:
                print_line += tile.format(content)
        print(seperator)

    def game_over_print(self, message):
        clean_screen = "\n" * 100
        print(clean_screen)
        seperator = '\n{}'.format('=' * 20)
        print(seperator)
        print("\n\n")
        print(message)
        score_int = 5 * len(self.snake.body)
        score_int += 50 * self.apple.eaten
        score = """
Score: {}\n\n
""".format(score_int)
        print(score)
        print(seperator)

    def game_start_print(self):
        clean_screen = "\n" * 100
        print(clean_screen)
        message = \
            """
Welcome to the Snake Jungle v1.0
Enter a direction by it's letter, then press the Enter Key:
[A]LEFT, [W]UP, [S]DOWN, [D]RIGHT And Press Enter.
The Game will begin in 2 seconds.
"""
        print(message)


if __name__ == "__main__":
    game = Game()
    game.start_game()
