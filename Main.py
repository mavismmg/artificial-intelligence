from pyamaze import maze, COLOR, agent, textLabel
from AstarAgent import AStarAgent

def main():
    _maze = maze(25, 25)
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

if __name__ == '__main__':
    main()