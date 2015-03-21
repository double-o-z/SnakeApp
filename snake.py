__author__ = 'OR'
import random

DIRECTIONS = 'AWSD'


class Snake():
    def __init__(self):
        self.length = 1
        self.apples = 0
        self.current_direction = DIRECTIONS[random.randint(0, 3)]
        self.body = []
        self.user_input = ''

    def get_direction(self):
        print('Insert Move: ')
        self.user_input = raw_input().upper()
        if self.user_input:
            if self.user_input in DIRECTIONS:
                if self.user_input == 'A':
                    print('You Move Left')
                elif self.user_input == 'W':
                    print('You Move UP')
                elif self.user_input == 'S':
                    print('You Move Down')
                elif self.user_input == 'D':
                    print('You Move Right')
        return