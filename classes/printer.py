__author__ = 'or'
import os


class Printer:
    def __init__(self, snake, apple, refresh_speed, difficulty):
        self.os_name = os.name
        self.snake = snake
        self.apple = apple
        self.game_start_delay = 5
        self.refresh_speed = refresh_speed
        self.difficulty = difficulty
        self.message = None
        self.message_counter = 0

    def clear_screen(self):
        os.system('cls' if self.os_name == 'nt' else 'clear')

    def game_over_print(self, message):
        self.clear_screen()
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
        self.clear_screen()
        print("""
Welcome to the Snake Jungle v1.0



Enter a command by it's letter, then press the Enter Key:

Movement:
    [W]
[A]     [D]
    [S]


Gameplay Options:
    [-]Slower
    [+]Faster
    [Q]Quit



Press Enter To Begin!
""")

    def print_message(self):
        if self.message and self.message_counter > 0:
            print("\n\n{}".format(self.message))
            self.message_counter -= 1
            if self.message_counter == 0:
                self.message = None

    def display_message(self, message):
        self.message = message
        self.message_counter = self.refresh_speed * self.difficulty
