import heapq

# A* algorithm implementation
def astar(start, goal, grid, heuristic):
    # Dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue to store nodes being explored
    frontier = [(0, start)]
    
    # Dictionary to track the path taken to reach each node
    came_from = {}
    
    # Dictionary to store the cost of reaching each node from the start node
    cost_so_far = {start: 0}

    # Main A* loop
    while frontier:
        # Pop the node with the lowest f-value from the priority queue
        current_f, current_node = heapq.heappop(frontier)

        # If the goal is reached, reconstruct the path and return
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        # Explore neighbors of the current node
        for next_node in neighbors(current_node, rows, cols):
            # Calculate the new cost to reach the neighbor node
            new_g = cost_so_far[current_node] + 1  # Assuming uniform cost
            
            # Update cost if the new path to this node is cheaper
            if next_node not in cost_so_far or new_g < cost_so_far[next_node]:
                cost_so_far[next_node] = new_g
                
                # Calculate heuristic value for the neighbor node
                new_h = heuristic(next_node, goal)
                
                # Calculate the total estimated cost
                new_f = new_g + new_h
                
                # Add the neighbor node to the frontier
                heapq.heappush(frontier, (new_f, next_node))
                
                # Update the path information
                came_from[next_node] = current_node

    # If no path is found
    return None

# Manhattan distance heuristic function
def manhattan_distance(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

# Function to find valid neighbors of a node
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

# Starting state of the search
start_state = (0, 0)

# Goal state of the search
goal_state = (4, 4)

# Perform A* search to find the path
path = astar(start_state, goal_state, grid, manhattan_distance)

# Print the resulting path
print("Path:", path)
