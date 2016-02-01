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
    def __init__(self, field_size, cells):
        self.cells = cells
        self.field_size = field_size
        self.length = 0
        self.apples = 0
        self.current_direction = None
        self.current_head = None
        self.body = []
        self.user_input = None

    def get_direction(self):
        user_input = raw_input().upper()
        if user_input:
            self.user_input = user_input
            if self.user_input in DIRECTIONS.keys():
                self.grow_snake()
            elif self.user_input == 'Q':
                print("Game Over")
                exit(1)
        return

    def grow_snake(self):
        self.current_head = self.body[-1]
        self.current_direction = DIRECTIONS.get(self.user_input)
        self.current_head = (self.current_head[0] + self.current_direction['Y-Axis'],
                             self.current_head[1] + self.current_direction['X-Axis'])
        if self.current_head not in self.cells:
            seperator = '\n{}'.format('=' * 20)
            print(seperator)
            print("\n\nBumped the wall. Game Over.\n")
            score_int = 5 * len(self.body)
            score = """
Score: {}
""".format(score_int)
            print(score)
            print(seperator)
            exit(1)
        self.body.append(self.current_head)
        self.length += 1

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
