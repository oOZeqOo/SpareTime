
# Templated off of Tech with Tim's A* algorithm video.
# added Dijkstra's Algorithm and Visuals and color options

import pygame
import math
import tkinter as tk
from tkinter import messagebox, simpledialog
from queue import PriorityQueue
import InputDialog
import os

main_x = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (main_x, main_x)

WIDTH = 800
WIN = pygame.display.set_mode( (WIDTH, WIDTH) )
pygame.display.set_caption("Path Finding Algorithms")

# Colors
RED = (255, 0, 0)
LIGHT_RED = (254, 150, 150)
START_COLOR = GREEN = (0, 220, 0)
END_COLOR = BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
LIGHT_BLUE = (0, 255 ,255)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
DARK_TURQUIOSE = (25, 196, 179)

DRAW_LINES = True
CHANGE_COLORS = True

class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
		self.count = 0
		self.size = 2
		self.colorCount = 0

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == LIGHT_RED

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == START_COLOR

	def is_end(self):
		return self.color == END_COLOR

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = START_COLOR

	def make_end(self):
		self.color = END_COLOR

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = LIGHT_RED

	def make_barrier(self):
		self.color = BLACK

	def make_path(self):
		self.color = LIGHT_BLUE

	def draw(self, win):
		global CHANGE_COLORS

		if self.count % 10 == 0 and self.size < (self.width // 2) and self.color != WHITE: # Make the non-WHITE squares more visually pleasing
			self.size += 1

		if self.color != WHITE:
			self.count += 1
			pygame.draw.rect(win, self.color, (self.x + (self.width // 2) - self.size, self.y + (self.width // 2) - self.size, self.size * 2, self.size * 2) )
		else:
			pygame.draw.rect(win, self.color, (self.x , self.y , self.width, self.width) )

		#Change colors of checked Spots
		if CHANGE_COLORS and self.count % 2 == 0:
			if self.color != LIGHT_RED and self.color[0] == 255 and self.color[1] < 254 : 
				self.color = (self.color[0], self.color[1] + 1, self.color[2])

			#elif self.color != LIGHT_RED and self.color != WHITE and self.color[1] >= 254 and self.color[0] >= 1:
				#self.color = (self.color[0] - 1, 0, self.color[2])

		#elif CHANGE_COLORS and self.color != LIGHT_RED and self.color != WHITE  and self.color[1] > 150 and self.colorCount % 1.0 == 0:
		#	self.color = (self.color[0] , self.color[1]  - self.colorCount, 0)



	def update_neightbors(self, grid):
		self.neighbors = []

		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # Down
			self.neighbors.append(grid[self.row + 1][self.col])
		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # Up
			self.neighbors.append(grid[self.row - 1][self.col])
		if self.col < self.total_rows - 1 and not grid[self.row ][self.col + 1].is_barrier(): # Right
			self.neighbors.append(grid[self.row ][self.col + 1])
		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # Left
			self.neighbors.append(grid[ self.row ][self.col - 1])
	
	def __lt__(self, other):
		return False

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()


def dijkstra_algorithm(draw, grid, start, end):
	count = 0
	visited = PriorityQueue()
	visited.put( (0, count, start) )
	came_from = {}

	dist = {spot: float("inf") for row in grid for spot in row}
	dist[start] = 0

	open_set_hash = {start}

	while not visited.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = visited.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			return True

		for neighbor in current.neighbors:
			temp_g_score = dist[current] + 1

			if temp_g_score < dist[neighbor]:
				came_from[neighbor] = current
				dist[neighbor] = temp_g_score
				if neighbor not in open_set_hash:
					count += 1
					visited.put((dist[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()
		draw()

		if current != start:
			current.make_closed()

		end.make_end()
		start.make_start()

	return False

def astar_algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put( (0, count, start) )
	came_from = {}

	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0

	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)

			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()
		draw()

		if current != start:
			current.make_closed()

		end.make_end()
		start.make_start()

	return False




def make_grid(rows, width):
	grid = []
	gap = width // rows

	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid
	
def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (WIDTH, i * gap) )
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width) )

def draw(win, grid, rows, width):
	global draw_lines
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	if DRAW_LINES: 
		draw_grid(win, rows, width)
	pygame.display.update()

def get_clicked_position(pos, rows, width):
	gap = width // rows
	y, x = pos
	
	row = y // gap
	col = x // gap

	return row, col

def main(win, width, draw_lines=True):
	global DRAW_LINES, CHANGE_COLORS
	DRAW_LINES = draw_lines
	ROWS = 50
	grid = make_grid(ROWS, width)

	win.fill(WHITE)
	pygame.display.update()
	
	algorithm = InputDialog.getInput(main_x, WIDTH)


	start = None
	end = None

	run = True 
	
	while run:
		draw(win, grid, ROWS, width)
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_position(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()
				elif not end and spot != start:
					end = spot
					end.make_end()
				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_position(pos, ROWS, width)
				spot = grid[row][col]
				if spot == start:
					start = None
					spot.reset()
				elif spot == end:
					end = None
					spot.reset()
				elif spot != end and spot != start:
					spot.reset()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neightbors(grid)
					CHANGE_COLORS = True
					if algorithm == "A* Algorithm":
						astar_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
					if algorithm == "Dijkstras Algorithm":	
						dijkstra_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
					CHANGE_COLORS = False
					start.make_start()

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)
					algorithm = InputDialog.getInput(main_x, WIDTH)

	pygame.quit()

main(WIN, WIDTH, False )