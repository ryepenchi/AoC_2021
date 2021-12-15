from itertools import chain
'''
regards to 
http://www.redblobgames.com/pathfinding/a-star/implementation.html
and
https://github.com/melkir/A-Star-Python
'''
class SquareGrid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.walls = []
	
	def in_bounds(self, id):
		(x, y) = id
		return 0 <= x < self.width and 0 <= y < self.height
	
	def passable(self, id):
		return id not in self.walls
	
	def neighbors(self, id):
		(x, y) = id
		results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
		if (x + y) % 2 == 0: results.reverse() # aesthetics
		results = filter(self.in_bounds, results)
		results = filter(self.passable, results)
		return results


class GridWithWeights(SquareGrid):
	def __init__(self, width, height):
		super().__init__(width, height)
		self.weights = {}
	
	def cost(self, from_node, to_node):
		return self.weights.get(to_node, 1) # 1 as default value

import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
	current = goal
	path = []
	while current != start:
		path.append(current)
		current = came_from[current]
	path.append(start) # optional
	path.reverse() # optional
	return path


# own stuff
chitons = []
with open("input15.txt") as file:
    for line in file:
        line = [int(x) for x in line.strip()]
        iterations = [line]
        for i in range(4):
            iterations.append([x+1 if x<9 else 1 for x in iterations[-1]])
        chitons.append(list(chain(*iterations)))

lines_per_block = len(chitons)
for i in range(4):
    new_lines = []
    for line in chitons[-lines_per_block:]:
        new_lines.append([x+1 if x<9 else 1 for x in line])
    chitons += new_lines


WIDTH = len(chitons[0])
HEIGHT = len(chitons)
# creating weighed grid graph
chiton_grid = GridWithWeights(WIDTH, HEIGHT)
for y in range(HEIGHT):
    for x in range(WIDTH):
        chiton_grid.weights[(x,y)] = chitons[y][x]

START = (0,0)
GOAL = (WIDTH - 1, HEIGHT - 1)

came_from, cost_so_far = a_star_search(chiton_grid, START, GOAL)
print(cost_so_far[GOAL])
# print(reconstruct_path(came_from, START, GOAL))