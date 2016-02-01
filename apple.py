__author__ = 'OR'
import random
from snake import CELLS


class Apple:
    def __init__(self):
        self.eaten = 0
        self.dropped = 0
        self.location = None

    def generate_apple(self, snake_body):
        cells_without_snake = list(CELLS)
        for cell in snake_body:
            cells_without_snake.remove(cell)
        if cells_without_snake:
            self.location = random.choice(cells_without_snake)
            self.dropped += 1

    def eat_apple(self):
        self.location = None
        self.eaten += 1
