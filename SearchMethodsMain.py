from pyamaze import maze, COLOR, agent, textLabel
from AstarAgent import AStarAgent
from DFS import AgentDFS
from BFS import AgentBFS
from Greedy import AgentGreedy
from LowerCost import AgentLowerCost
from labirinto import Labirinto

def main():
    _maze = maze(75, 75)
    _maze.CreateMaze(loopPercent=100, theme=COLOR.dark)

    path_agent = agent(_maze, footprints=True, filled=True, goal=(_maze.rows, _maze.cols),
                   color=COLOR.red)

    search_agent = agent(_maze, shape='square', footprints=True, color=COLOR.yellow, filled=True)
    fwd_agent = agent(_maze, footprints=True, color=COLOR.blue)

    solution = AStarAgent(_maze)
    search_path, a_path, fwd_path = solution.aStar()

    _maze.tracePath({search_agent:search_path})
    _maze.tracePath({path_agent:a_path})
    _maze.tracePath({fwd_agent:fwd_path})

    textLabel(_maze, 'Path Lenght', len(fwd_path) + 1)
    textLabel(_maze, 'Search Lenght', len(search_path))

    print(_maze.maze_map)
    print(_maze.grid)

    _maze.run()
    
    # DFS
    nlin = 10
    ncol = 10
    
    l1 = Labirinto(nlin, ncol, 0.25, [0, 0], [nlin-1, ncol-1])
    ag = AgentDFS(l1)
    ag.run()
    
    # BFS
    ag2 = AgentBFS(l1)
    ag2.run()
    
    # Greedy
    ag3  = AgentGreedy(l1)
    path_greedy = ag3.act()
    print(path_greedy)
    
    # LowerCost
    ag4 = AgentLowerCost(l1)
    path_lowercost = ag4.act()
    print(path_lowercost)
    
if __name__ == '__main__':
    main()