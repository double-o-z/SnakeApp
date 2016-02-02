__author__ = 'OR'
import signal
import time
import sys

sys.path.append("/Users/or/dev/Snake")

from snake import Snake
from apple import Apple


class Game:
    def __init__(self):
        self.signal = signal
        self.signal.signal(signal.SIGALRM, self.raise_exception)
        self.field_size = 4
        self.refresh_speed = 1.25
        self.user_input = None
        self.prompt_difficulty()
        self.cells = [(i, j) for i in list(xrange(self.field_size)) for j in list(xrange(self.field_size))]
        self.apple = Apple(self.cells)
        self.snake = Snake(self.field_size, self.cells, self.apple)
        self.snake.create_snake()
        self.apple.generate_apple(self.snake.body)

    def raise_exception(self, sig_num, stack_frame):
        raise KeyboardInterrupt

    def prompt_difficulty(self):
        self.signal.setitimer(self.signal.ITIMER_REAL, 5)
        try:
            self.user_input = raw_input(
                "Choose Game Difficulty By Number: [1]Easy, [2]Normal, [3]Hard, [4]Veteran, [5]Expert: ")
            if self.user_input:
                if self.user_input in '12345':
                    self.field_size = int(self.user_input) * 4  # 4 - 20
                    self.refresh_speed = float(0.25) * (6 - int(self.user_input))
            self.signal.setitimer(self.signal.ITIMER_REAL, 0)
        except KeyboardInterrupt:
            pass

    def start_game(self):
        game_start_delay = 5
        self.game_start_print(game_start_delay)
        time.sleep(game_start_delay)
        message = ''
        while True:
            if self.snake.length >= len(self.cells):
                self.game_over_print("Good Game, You WIN.")
                exit(1)
            self.draw_jungle()
            try:
                # self.signal.alarm(self.refresh_speed)
                self.signal.setitimer(self.signal.ITIMER_REAL, self.refresh_speed)
                self.snake.get_direction()
                self.signal.setitimer(self.signal.ITIMER_REAL, 0)
            except KeyboardInterrupt:
                self.snake.move_snake()

    def draw_jungle(self):
        clean_screen_top = "\n" * 100
        clean_screen_bottom = "\n" * 30
        print(clean_screen_top)
        seperator = '\n{}'.format('=' * 20)
        roof = ' {} '.format(' '.join('_' * self.field_size))
        print(seperator)
        print(roof)
        tile = '|{}'
        for idx, cell in enumerate(self.cells):
            content = '_'
            if cell in self.snake.body:
                content = 'o'
                if cell == self.snake.body[-1]:
                    content = 's'
            if cell == self.apple.location:
                content = '*'
            if (idx + 1) % self.field_size == 0:
                print_line += tile.format(content + '|')
                print(print_line)
            elif (idx + 1) % self.field_size == 1:
                print_line = ''
                print_line += tile.format(content)
            else:
                print_line += tile.format(content)
        print(seperator)
        print(clean_screen_bottom)

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
        clean_screen_bottom = "\n" * 30
        print(clean_screen_bottom)

    def game_start_print(self, game_start_delay):
        clean_screen = "\n" * 100
        print(clean_screen)
        message = \
            """
Welcome to the Snake Jungle v1.0
Enter a direction by it's letter, then press the Enter Key:
[A]LEFT, [W]UP, [S]DOWN, [D]RIGHT And Press Enter.
The Game will begin in {} seconds.
""".format(str(game_start_delay))
        print(message)
        clean_screen_bottom = "\n" * 30
        print(clean_screen_bottom)


if __name__ == "__main__":
    game = Game()
    # game.prompt_difficulty()
    game.start_game()
