#gameoflife.py
import random
import copy
from Tkinter import *

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

def boardToScreen(w,board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[j][i] == 1:
				w.create_rectangle(25*(i+1), 25*(j+1), 25*(i+2), 25*(j+2), fill="blue")
			else:
				w.create_rectangle(25*(i+1), 25*(j+1), 25*(i+2), 25*(j+2), fill="gray")


def printBoard(board):
	for row in board:
		print row
	print

n = 5


b = initBoard(n)
printBoard(b)




master = Tk()
w = Canvas(master, width=250, height=250)
w.pack()

boardToScreen(w, b)
# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
# w.create_rectangle(50, 25, 150, 75, fill="blue")


mainloop()