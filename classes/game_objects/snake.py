__author__ = 'OR'
import random

DIRECTIONS = {
    'A': {
        'Direction': 'Left',
        'X-Axis': -1,
        'Y-Axis': 0,
    },
    'W': {
        'Direction': 'Up',
        'X-Axis': 0,
        'Y-Axis': -1,
    },
    'S': {
        'Direction': 'Down',
        'X-Axis': 0,
        'Y-Axis': 1,
    },
    'D': {
        'Direction': 'Right',
        'X-Axis': 1,
        'Y-Axis': 0,
    }
}


class Snake:
    def __init__(self, field_size, cells, apple):
        self.user_input = None
        self.cells = cells
        self.field_size = field_size
        self.apple = apple
        self.length = 0
        self.apples = 0
        self.current_direction = None
        self.current_head = None
        self.body = []

    def move_snake(self):
        self.current_head = self.body[-1]
        self.current_direction = DIRECTIONS.get(self.user_input)
        self.current_head = (self.current_head[0] + self.current_direction['Y-Axis'],
                             self.current_head[1] + self.current_direction['X-Axis'])
        if self.current_head not in self.cells:
            clean_screen = "\n" * 100
            print(clean_screen)
            print("\n\nBumped the wall. Game Over.\n")
            score_int = 5 * len(self.body)
            score = """
Score: {}
""".format(score_int)
            print(score)
            exit(1)
        self.body.append(self.current_head)
        if self.current_head in self.body[:-1]:
            message = "You ate yourself. Game Over."
            self.game_over_print(message)
            exit(1)
        elif self.current_head == self.apple.location:
            self.apple.eat_apple()
            self.length += 1
            self.apple.generate_apple(self.body)
        else:
            del self.body[0]

    def create_snake(self):
        self.body.append(random.choice(self.cells))
        self.length += 1
        self.current_head = self.body[0]
        self.current_direction = self.get_initial_direction()
        self.user_input = self.current_direction

    def get_initial_direction(self):
        directions_without_wall = dict(DIRECTIONS)
        if self.current_head[0] == 0:
            # remove [W]Up
            del directions_without_wall['W']
        if self.current_head[1] == 0:
            # remove [A]Left
            del directions_without_wall['A']
        if self.current_head[0] + 1 == self.field_size:
            # remove [S]Down
            del directions_without_wall['S']
        if self.current_head[1] + 1 == self.field_size:
            # remove [D]Right
            del directions_without_wall['D']

        return random.choice(directions_without_wall.keys())

    def game_over_print(self, message):
        clean_screen = "\n" * 100
        print(clean_screen)
        print("\n\n")
        print(message)
        score_int = 5 * len(self.body)
        score_int += 50 * self.apple.eaten
        score = """
Score: {}\n\n
""".format(score_int)
        print(score)

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

