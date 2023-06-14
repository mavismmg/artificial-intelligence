import pygame
import sys

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

def same_column(solution, col):
    return (col in solution)

def same_diagonal(solution, col):
    for i in range(len(solution)):
        delta_col = abs(col - solution[i]) 
        delta_row = abs(i - len(solution))
        if delta_col == delta_row:
            return True
    return False

def violate_constraints(solution, col, constraints):
    for constraint in constraints:
        res = constraint(solution, col)
        if res:
           return True
    return False 

def backtracking(n, constraints, solution=[]):
    if len(solution) == n:
        return solution
    for col in [int(i) for i in range(n)]:
        if not violate_constraints(solution, col, constraints):
            solution.append(col)
            res = backtracking(n, constraints, solution)
            if res:
                return res
            solution.pop(-1)

if __name__ == '__main__':

    constraints = [same_diagonal,same_column]
    n = 60

    res = backtracking(n,constraints)
    print(res)

    draw_chessboard(res)