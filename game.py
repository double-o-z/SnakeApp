__author__ = 'OR'
import signal
import time
import sys

sys.path.append("/Users/or/dev/Snake")

from classes.game_objects.snake import Snake, DIRECTIONS
from classes.game_objects.apple import Apple
from classes.printer import Printer
from classes.decorators import with_alarm


class Game:
    def __init__(self):
        self.difficulties = '12345'
        self.difficulty = 5
        self.refresh_speed = 1.25
        self.refresh_speed_interval = 0.25
        self.slowest_refresh_rate = (len(self.difficulties) + 1) * self.refresh_speed_interval
        self.fastest_refresh_rate = self.refresh_speed_interval
        self.signal = signal
        self.signal.signal(signal.SIGALRM, self.raise_exception)
        self.field_size = 4
        self.user_input = None
        self.prompt_difficulty()
        self.cells = [(i, j) for i in list(xrange(self.field_size)) for j in list(xrange(self.field_size))]
        self.apple = Apple(self.cells)
        self.snake = Snake(self.field_size, self.cells, self.apple)
        self.printer = Printer(self.snake, self.apple, self.refresh_speed, self.difficulty)

    def raise_exception(self, sig_num, stack_frame):
        raise KeyboardInterrupt

    def prompt_difficulty(self):
        self.signal.setitimer(self.signal.ITIMER_REAL, 5)
        try:
            self.user_input = raw_input(
                "Choose Game Difficulty By Number: [1]Easy, [2]Normal, [3]Hard, [4]Veteran, [5]Expert: ")
            if self.user_input:
                if self.user_input in self.difficulties:
                    self.difficulty = int(self.user_input)
                    self.field_size = int(self.user_input) * 4
                    self.refresh_speed = float(self.refresh_speed_interval) * (len(self.difficulties) + 1 - int(self.user_input))
            self.signal.setitimer(self.signal.ITIMER_REAL, 0)
        except KeyboardInterrupt:
            pass

    def start_game(self):
        while True:
            self.game_status()
            self.draw_jungle()
            try:
                with_alarm(self.get_input, self.signal, self.refresh_speed)()
            except KeyboardInterrupt:
                self.snake.move_snake()

    def game_status(self):
        if self.snake.length >= len(self.cells):
            self.printer.game_over_print("Good Game, You WIN.")
            exit(1)

    def draw_jungle(self):
        self.printer.clear_screen()
        roof = ' {} '.format(' '.join('_' * self.field_size))
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
        self.printer.print_message()

    def get_input(self):
        user_input = raw_input()
        if user_input:
            if user_input[-1].upper():
                self.user_input = user_input[-1].upper()
                if self.user_input in DIRECTIONS.keys():
                    self.snake.user_input = self.user_input
                    self.snake.move_snake()
                if self.user_input == 'Q':
                    self.end_game()
                elif self.user_input in ['-', '+']:
                    self.change_refresh_speed()
                    self.snake.move_snake()
        return user_input

    def init_field(self):
        self.snake.create_snake()
        self.apple.generate_apple(self.snake.body)
        self.printer.game_start_print()
        with_alarm(self.player_ready, self.signal, 60)()

    def player_ready(self):
        user_input = raw_input()
        if user_input == "":
            return

    def end_game(self):
        print("Game Over")
        exit(1)

    def change_refresh_speed(self):
        if self.user_input == '-':
            if self.refresh_speed < self.slowest_refresh_rate:
                self.refresh_speed += self.refresh_speed_interval
                self.printer.refresh_speed += self.refresh_speed
                self.printer.display_message("Speed Decreased. Current Refresh Rate: {} Seconds.".
                                             format(self.refresh_speed))
            else:
                self.printer.display_message("Slowest Speed. Current Refresh Rate: {} Seconds.".
                                             format(self.refresh_speed))
        elif self.user_input == '+':
            if self.refresh_speed > self.fastest_refresh_rate:
                self.refresh_speed -= self.refresh_speed_interval
                self.printer.refresh_speed += self.refresh_speed
                self.printer.display_message("Speed Increased. Current Refresh Rate: {} Seconds.".
                                             format(self.refresh_speed))
            else:
                self.printer.display_message("Fastest Speed. Current Refresh Rate: {} Seconds.".
                                             format(self.refresh_speed))


if __name__ == "__main__":
    game = Game()
    game.init_field()
    game.start_game()
