import heapq

def astar(start, goal, grid, heuristic):
    rows, cols = len(grid), len(grid[0])
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        current_f, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        for next_node in neighbors(current_node, rows, cols):
            new_g = cost_so_far[current_node] + 1  # Assuming uniform cost
            if next_node not in cost_so_far or new_g < cost_so_far[next_node]:
                cost_so_far[next_node] = new_g
                new_h = heuristic(next_node, goal)
                new_f = new_g + new_h
                heapq.heappush(frontier, (new_f, next_node))
                came_from[next_node] = current_node

    return None

# Example usage:
def manhattan_distance(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def neighbors(state, rows, cols):
    x, y = state
    possible_moves = [(x+dx, y+dy) for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]]
    return [(x, y) for x, y in possible_moves if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0]

# Define the grid
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start_state = (0, 0)
goal_state = (4, 4)

path = astar(start_state, goal_state, grid, manhattan_distance)
print("Path:", path)
