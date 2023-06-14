import numpy as np

from matplotlib import pyplot as plt

class Labirinto:
  def __init__(self, rows: int, cols: int, p_obstacle: float, input_: np.array, output_: np.array) -> None:
    self.map = np.zeros((rows, cols))
    self.input_ = np.array(input_)
    self.output_ = np.array(output_)
    # add obstacles
    for row in range(rows):
      for col in range(cols):
        if np.random.random() < p_obstacle:
          self.map[row][col] = 1
    
    self.map[input_[0]][output_[1]] = 0.8
    self.map[output_[0]][input_[1]] = 0.2
          
  def get_neighbors(self, position: int) -> None:
    n_rows, n_cols = self.map.shape
    nbs = []
    nbs.append(position + np.array([1, 0])) # north
    nbs.append(position - np.array([1, 0])) # south
    nbs.append(position + np.array([0, 1])) # east
    nbs.append(position - np.array([0, 1])) # west
    neighbors = []
    for nb in nbs:
      if ((nb[0] >= 0) and (nb[0] < n_rows) and (nb[1] >= 0) and (nb[1] < n_cols)):
        if (self.map[nb[0]][nb[1]] == 0):
          neighbors.append(nb)  
    return neighbors
  
  def visualize_map(self) -> None:
    plt.axes().invert_yaxis()
    plt.pcolormesh(self.map)
    plt.plot(self.input_[1] + 0.5, self.input_[0] + 0.5, 'rs')
    plt.show()
    print(self.map)
    
  def visualize_route(self, paths: np.array) -> None:
    plt.axes().invert_yaxis()
    plt.pcolormesh(self.map)
    for path in range(len(paths) - 1):
      plt.plot([paths[path][1] + 0.5, paths[path+1][1] + 0.5], [paths[path][0] + 0.5, paths[path+1][1] + 0.5], '-rs')
    plt.show()
    
  def initial_persceptions(self):
    return {'position': self.input_,
            'objective': self.output_,
            'neighbors': self.get_neighbors(self.input_)}
  
  def change_env_state(self, action: bool) -> None:
    position = action['move_to']
    return {'position': position,
            'objective': self.output_,
            'neighbors': self.get_neighbors(position)}
