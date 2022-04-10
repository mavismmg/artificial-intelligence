from queue import PriorityQueue

class AStarAgent:
    def __init__(self, _maze):
        self._maze = _maze

    def h(self, cell1, cell2):
        x1, y1 = cell1
        x2, y2 = cell2

        return abs(x1 - x2) + abs(y1 - y2)

    def aStar(self):
        """f(n) = g(n) + h(n)"""
        start = (self._maze.rows, self._maze.cols)

        g_score = {cell:float('inf') for cell in self._maze.grid}
        g_score[start] = 0
        
        f_score = {cell:float('inf') for cell in self._maze.grid}
        f_score[start] = self.h(start, self._maze._goal)

        queue = PriorityQueue()
        queue.put((self.h(start, self._maze._goal), self.h(start, self._maze._goal), start))
        a_path = {}

        search_path = [start]

        while not queue.empty():
            curr_cell = queue.get()[2]
            search_path.append(curr_cell)

            if curr_cell == self._maze._goal:
                break

            for dict in 'ESNW':
                if self._maze.maze_map[curr_cell][dict] == True:
                    if dict == 'E':
                        child_cell = (curr_cell[0], curr_cell[1] + 1)

                    if dict == 'W':
                        child_cell = (curr_cell[0], curr_cell[1] - 1)

                    if dict == 'N':
                        child_cell = (curr_cell[0] - 1, curr_cell[1])
                    
                    if dict == 'S':
                        child_cell = (curr_cell[0] + 1, curr_cell[1])

                    temp_g_score = g_score[curr_cell] + 1
                    temp_f_score = temp_g_score + self.h(child_cell, self._maze._goal)

                    if temp_f_score < f_score[child_cell]:
                        g_score[child_cell] = temp_g_score
                        f_score[child_cell] = temp_f_score

                        queue.put((temp_f_score, self.h(child_cell, self._maze._goal), child_cell))
                        a_path[child_cell] = curr_cell
        
        fwd_path = {}
        cell = self._maze._goal

        while cell != start:
            fwd_path[a_path[cell]] = cell
            cell = a_path[cell]

        return search_path, a_path, fwd_path