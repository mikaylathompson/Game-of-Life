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

def countLiving(board):
	count = 0
	for row in board:
		for cell in row:
			count += cell
	return count

def boardToScreen(w,board, s):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[j][i] == 1:
				w.create_rectangle(s*(i+1), s*(j+1), s*(i+2), s*(j+2), fill="blue")
			else:
				w.create_rectangle(s*(i+1), s*(j+1), s*(i+2), s*(j+2), fill="gray")

def printBoard(board):
	for row in board:
		print row
	print

n = 30
blockSize = 20
delay = 100

b = initBoard(n)
# font = ("Aller Display",30)
# font = ("Digital dream Fat",30)


master = Tk()
w = Canvas(master, width=n*blockSize+120, height=n*blockSize+50)
w.pack()

for i in range(1001):
	w.delete(ALL)
	boardToScreen(w, b, blockSize)
	w.create_text(blockSize*(n+2.7)+15, n*blockSize/3, text=str(i), font=("ONRAMP",40), fill="red")
	w.create_text(blockSize*(n+2.7)+15, n*blockSize/3 - 40, text="Time:", font=("ONRAMP",25), fill="red")
	w.create_text(blockSize*(n+2.7)+15, 2*n*blockSize/3, text=str(countLiving(b)), font=("ONRAMP",40), fill="red")
	w.create_text(blockSize*(n+2.7)+15, 2*n*blockSize/3 - 40, text="Alive:", font=("ONRAMP",25), fill="red")
	b = tic(b)
	w.after(delay)
	w.update()

mainloop()