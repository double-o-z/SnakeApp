__author__ = 'OR'
import random
import signal
import time

from snake import Snake

CELLS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
         (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
         (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


class Game:
    def __init__(self):
        self.snake = Snake()
        self.snake.body.append(random.choice(CELLS))
        signal.signal(signal.SIGALRM, self.raise_exception)

    def raise_exception(self, sig_num, stack_frame):
        raise KeyboardInterrupt

    def start_game(self):
        print("""
        'Welcome to the Snake Jungle v1.0'
        Choose a direction by it's letter:
        [A]LEFT, [W]UP, [S]DOWN, [D]RIGHT And Press Enter.
        The Game will begin in 2 seconds.
        """)
        time.sleep(2)
        message = ''
        while True:
            # self.cycle()
            self.draw_jungle()
            try:
                signal.alarm(3)
                self.snake.get_direction()
                signal.alarm(0)
            except KeyboardInterrupt:
                continue
            if self.snake.length >= len(CELLS):
                message = "Congratz! You've Won!!!"
                break
            elif self.snake.body[-1] in self.snake.body[:-1]:
                message = "Oops.. You ate yourself. Try again."
                break
            else:
                continue
        print(message)
        exit(0)

    def draw_jungle(self):
        print('\n{}'.format('='*20))
        print(' _ _ _ _ _')
        tile = '|{}'
        for idx, cell in enumerate(CELLS):
            content = '_'
            if cell in self.snake.body:
                content = 'S'
                if cell == self.snake.body[-1]:
                    content = 'O'
            if idx+1 in [5, 10, 15, 20, 25]:
                print_line += tile.format(content + '|')
                print(print_line)
            elif idx+1 in [1, 6, 11, 16, 21]:
                print_line = ''
                print_line += tile.format(content)
            else:
                print_line += tile.format(content)

        print('\n{}'.format('='*20))

Game().start_game()