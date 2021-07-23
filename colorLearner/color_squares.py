from multiprocessing import Queue, Process
import queue
import pygame
from random import randint
from time import sleep
from typing import List, Tuple



class ColorSquares:

    def __init__(self, initial_squares: List[List[Tuple[int]]]):
        """
            Initial squares is a 2D list of (R, G, B) values to represent
            the color and position of the square to be displayed.
        """
        
        pygame.init()
        
        self.running = False
        self.squares = initial_squares
        self._width = 500
        self._height = 500
        self._communication_queue = Queue()

        self.render_thread = Process(target=self._render_loop, daemon=True)
        self.render_thread.start()

    def start(self):
        self._communication_queue.put(True)

        self.running = True

    def update_squares(self, squares):
        if not self.running:
            self.squares = squares
        else:
            self._communication_queue.put(squares)

    def _render_loop(self):
        self.running = self._communication_queue.get()
        self.screen = pygame.display.set_mode([self._width, self._height])
        if self.squares == []:
            self.squares = self._communication_queue.get()


        while True:
            if not self.running:
                continue

            square_height = self._height // len(self.squares)
            for row, square_row in enumerate(self.squares):
                square_width = self._width // len(square_row) 

                for column, square_color in enumerate(square_row):
                    left = square_width * column
                    top = square_height * row
                    square_position = (left, top, square_width, square_height)

                    pygame.draw.rect(self.screen, square_color, square_position)
            
            pygame.display.flip()

            kill_render = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    kill_render = True
        
            if kill_render:
                break

            # Silly loop so that VSCode stops
            # telling me the pygame window is not
            # responding due to a long
            # wait on the queue.
            while True:
                try:
                    self.squares = self._communication_queue.get(timeout=1)
                except queue.Empty:
                    break

        pygame.quit()

if __name__ == "__main__":
    squares_height = 10
    squares_depth = 10

    def generate_squares():
        squares = []
        for i in range(squares_height):
            squares.append([])
            for j in range(squares_depth):

                random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
                squares[-1].append(random_color)
        return squares

    square_display = LearnerSquares(generate_squares())
    square_display.start()

    while True:
        sleep(3)
        square_display.update_squares(generate_squares())
