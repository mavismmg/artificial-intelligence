from nqueen_backtracking import draw_chessboard
from nqueen_backtracking import backtracking
from nqueen_backtracking import same_diagonal
from nqueen_backtracking import same_column

from nqueen_local_search import local_search
from nqueen_local_search import get_conflicts

def main():
  # Local search
  n = 10
  res, conflicts = local_search(n, get_conflicts)
  draw_chessboard(res)
  
  # With backtracking
  constraints = [same_diagonal, same_column]
  n = 60
  res = backtracking(n, constraints=constraints)
  print(res)
  draw_chessboard(res)

if __name__ == "__main__":
  main()