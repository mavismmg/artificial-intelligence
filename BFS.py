from labirinto import Labirinto

import matplotlib.pyplot as plt

class AgentBFS:
  def __init__(self, env_) -> None:
    self.env_ = env_
    self.perceptions = env_.initial_persceptions()
    self.F = [[self.perceptions['position']]]
    
  def act(self) -> None:
    path = self.F.pop(0)
    action = {'move_to': path[-1]}
    ps = path
    for p in range(len(ps) - 1):
      plt.plot([ps[p][1] + 0.5, ps[p+1][1] + 0.5], [ps[p][0] + 0.5, ps[p+1][1] + 0.5], '-rs')
    plt.draw()
    plt.pause(0.1)
    plt.clf()
    self.perceptions = self.env_.change_env_state(action)
    if self.perceptions['position'].all() == self.perceptions['objective'].all():
      return path
    else:
      for neighbor in self.perceptions['neighbors']:
        cycle = False
        for node in path:
          if (node == neighbor).all():
            cycle = True
        if not cycle:
          self.F.append(path + [neighbor])
          
  def run(self) -> None:
    plt.ion()
    while self.F:
      plt.axes().invert_yaxis()
      plt.pcolormesh(self.env_.map)
      print(self.F)
      self.act()
      plt.draw()
      plt.pause(0.1)
      plt.clf()