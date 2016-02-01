__author__ = 'OR'
import signal
import time
import sys

sys.path.append("/Users/or/dev/Snake")

from snake import Snake
from apple import Apple


class Game:
    def __init__(self, field_size, refresh_speed):
        self.field_size = field_size
        self.refresh_speed = refresh_speed
        self.cells = [(i, j) for i in list(xrange(self.field_size)) for j in list(xrange(self.field_size))]
        self.snake = Snake(self.cells)
        self.snake.create_snake()
        self.apple = Apple(self.cells)
        self.apple.generate_apple(self.snake.body)
        signal.signal(signal.SIGALRM, self.raise_exception)

    def raise_exception(self, sig_num, stack_frame):
        raise KeyboardInterrupt

    def start_game(self):
        self.game_start_print()
        time.sleep(2)
        message = ''
        while True:
            if self.snake.length >= len(self.cells):
                self.game_over_print("Good Game, You WIN.")
                exit(1)
            self.draw_jungle()
            try:
                signal.alarm(self.refresh_speed)
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


def prompt_field_size():
    try:
        signal.alarm(5)
        field_size = raw_input('Enter a number for the field size (1-20): ')
        if field_size:
            try:
                field_size = int(field_size)
            except Exception, e:
                print(e)
        else:
            field_size = 5
        signal.alarm(0)
        return field_size
    except KeyboardInterrupt:
        pass


def prompt_refresh_speed():
    try:
        signal.alarm(5)
        refresh_speed = raw_input('Enter a number for the refresh speed in seconds (1-3): ')
        if refresh_speed:
            try:
                refresh_speed = int(refresh_speed)
            except Exception, e:
                print(e)
        else:
            refresh_speed = 2
        signal.alarm(0)
        return refresh_speed
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    field_size = prompt_field_size()
    refresh_speed = prompt_refresh_speed()
    game = Game(field_size, refresh_speed)
    game.start_game()
