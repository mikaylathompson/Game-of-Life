#gameoflife.py
import random
import copy
import pygame

def initBoard(n):
	board = []
	for i in range(n):
		board.append([random.randint(0,1) for x in xrange(n)])
	return board

def countNeighbors(board, row, col):
	n = len(board)
	count = 0
	irange = []
	if 0 < row < n-1:
		irange = [-1, 0, 1]
	elif row == 0:
		irange = [n - 1, 0, 1]
	else:
		irange = [-1, 0, -row]

	if 0 < col < n-1:
		jrange = [-1, 0, 1]
	elif col == 0:
		jrange = [n - 1, 0, 1]
	else:
		jrange = [-1, 0, -col]

	for i in irange:
		for j in jrange:
			if not (i == 0 and j == 0):
				count += board[row + i][col + j]
	return count

def doCounts(t1):
	n = len(t1)
	t0 = copy.deepcopy(t1)
	for row in range(n):
		for col in range(n):
			nbrs = countNeighbors(t1, row, col)
			t0[row][col] = nbrs
	return t0


def tic(t1):
	n = len(t1)
	t0 = copy.deepcopy(t1)
	for row in range(n):
		for col in range(n):
			nbrs = countNeighbors(t0, row, col)
			if t0[row][col] == 0:
				if nbrs == 3:
					t1[row][col] = 1
			else:
				if nbrs < 2 or nbrs > 3:
					t1[row][col] = 0
	return t1


def printBoard(board):
	for row in board:
		print row
	print

n = 5


b = initBoard(n)
printBoard(tic(b))


pygame.init() 

#create the screen
window = pygame.display.set_mode((640, 480)) 

#draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
pygame.draw.line(window, (255, 255, 255), (0, 0), (30, 50))

#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print event 