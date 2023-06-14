import pygame
import sys
import numpy as np
from copy import copy

def draw_chessboard(queen_positions):
    queen_positions = [(i,queen_positions[i]) for i in range(len(queen_positions))]
    BLACK = (107,142,35)
    WHITE = (255,248,220)
    RED = 	(0,0,0)
    WIDTH = 480
    HEIGHT = 480
    CELL_SIZE = WIDTH // len(queen_positions)
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chessboard')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for row in range(len(queen_positions)):
            for col in range(len(queen_positions)):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if (row, col) in queen_positions:
                    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
        pygame.display.flip()

def get_conflicts(solution):
    conflicts = 0
    for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            delta_col = abs(solution[i]-solution[j]) 
            delta_row = abs(i-j)
            if delta_col==delta_row:
                conflicts+=1
    return conflicts

def local_search(n, f, itermax=1000, solution=[]):
    conflicts = []
    if not solution:
        for i in range(n):
            r = np.random.randint(n)
            while r in solution:
                r = np.random.randint(n)
            solution.append(r) 

    iter = 0
    while iter < itermax:
        print(f(solution))
        i = np.random.randint(n)
        j = np.random.randint(n)
        neighbor = copy(solution)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        if f(neighbor) <= f(solution):
            solution = neighbor 
            conflicts.append(f(neighbor))
        iter += 1
    print(f(solution))
    return solution, conflicts

if __name__ == '__main__':
    n = 10
    res, conflicts = local_search(n,get_conflicts)
    draw_chessboard(res)