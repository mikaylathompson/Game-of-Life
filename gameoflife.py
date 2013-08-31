#gameoflife.py
import random
import copy
from Tkinter import *

def initBoard(n):  #Build a random board of 1s and 0s of size n x n
	board = []
	for i in range(n):
		board.append([random.randint(0,1) for x in xrange(n)])
	return board

def countNeighbors(board, row, col):	# count how many neighbors a
	n = len(board)						# particular cell has
	count = 0
	irange = []
	if 0 < row < n-1:					#These find range to iterate over
		irange = [-1, 0, 1]				#(does it wrap around?)
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
	for i in irange:					#And this actually adds the neighbors
		for j in jrange:				#scores together
			count += board[row + i][col + j]
	count -= board[row][col]			#Don't count yourself
	return count

def tic(t1):							# One timestep
	n = len(t1)
	t0 = copy.deepcopy(t1)				# Make a copy to count from
	for row in range(n):				# and edit the original with
		for col in range(n):			# updated scores
			nbrs = countNeighbors(t0, row, col)
			if t0[row][col] == 0:		#Only changes are when dead cell
				if nbrs == 3:			#has three neighbors or
					t1[row][col] = 1 
			else:						#living cell has >3, <2 neighbors
				if nbrs < 2 or nbrs > 3:
					t1[row][col] = 0
	return t1

def countLiving(board):					#Iterates through board to count
	count = 0 							#how many cells are alive
	for row in board:
		for cell in row:
			count += cell
	return count

def boardToScreen(w,board, s): 			#Draws board on screen by drawing n^2
	for i in range(len(board)): 		#squares of size s and coloring them
		for j in range(len(board)):		#by whether or not they're alive
			if board[j][i] == 1:
				w.create_rectangle(s*(i+1), s*(j+1), s*(i+2), s*(j+2), fill="blue")
			else:
				w.create_rectangle(s*(i+1), s*(j+1), s*(i+2), s*(j+2), fill="gray")

#### SETTINGS ####
n = 30				# n = size of board
blockSize = 20		# blockSize = size of each square on display
delay = 100 		# delay = time between frames in display

# Set up canvas
master = Tk()
w = Canvas(master, width=n*blockSize+120, height=n*blockSize+50)
w.pack()

# Initialize a random board
b = initBoard(n)

# Loop through time.  
# For each step, clear screen, draw squares, and label with time and # alive.
# Calculate the new board, delay, update screen.
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