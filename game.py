__author__ = 'OR'
import random
import signal
import time
import sys

sys.path.append("/Users/or/dev/Snake")

from snake import Snake, CELLS


class Game:
    def __init__(self):
        self.snake = Snake()
        self.snake.create_snake(random.choice(CELLS))
        signal.signal(signal.SIGALRM, self.raise_exception)

    def raise_exception(self, sig_num, stack_frame):
        raise KeyboardInterrupt

    def start_game(self):
        message = \
            """
Welcome to the Snake Jungle v1.0
Enter a direction by it's letter, then press the Enter Key:
[A]LEFT, [W]UP, [S]DOWN, [D]RIGHT And Press Enter.
The Game will begin in 2 seconds.
"""
        print(message)
        time.sleep(2)
        message = ''
        while True:
            if self.snake.length >= len(CELLS):
                message = "Good Game, You WIN."
                print(message)
                score_int = 5 * len(self.snake.body)
                score = """
Score: {}
""".format(score_int)
                print(score)
                exit(1)
            self.draw_jungle()
            try:
                signal.alarm(2)
                self.snake.get_direction()
                signal.alarm(0)
            except KeyboardInterrupt:
                self.snake.grow_snake()
            if self.snake.body[-1] in self.snake.body[:-1]:
                message = \
                    """
Oops..
You ate yourself.
Game Over.
"""
                break
            else:
                continue
        print(message)
        score_int = 5 * len(self.snake.body)
        score = """
Score: {}
""".format(score_int)
        print(score)
        exit(0)

    def draw_jungle(self):
        seperator = '\n{}'.format('=' * 20)
        roof = ' _ _ _ _ _'
        print(seperator)
        print(roof)
        tile = '|{}'
        for idx, cell in enumerate(CELLS):
            content = '_'
            if cell in self.snake.body:
                content = 'S'
                if cell == self.snake.body[-1]:
                    content = 'O'
            if idx + 1 in [5, 10, 15, 20, 25]:
                print_line += tile.format(content + '|')
                print(print_line)
            elif idx + 1 in [1, 6, 11, 16, 21]:
                print_line = ''
                print_line += tile.format(content)
            else:
                print_line += tile.format(content)
        print(seperator)


Game().start_game()
