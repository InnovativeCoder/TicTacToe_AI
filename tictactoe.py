
from numpy import random

states = []
V = []
totalStates = 0

board = [0,0,0,0,0,0,0,0,0]

tiles = [0,1,2]

def initBoard():
	for i in range(0,9):
		board[i] = 0

def create_all_states(board,player):
	won = hasWinner(board)
	if won == 1 or won == -1:
		return
	for i in range(0,9):
		if board[i] == 0:
			board[i] = player
			if board[:] not in states:
				states.append(board[:])
				V.append(determineValue(board,player))

			create_all_states(board,switchPlayer(player))
			board[i] = 0


def switchPlayer(player):
	if player == 1:
		return 2
	else:
		return 1

def determineValue(_board, player):
  won = hasWinner(_board)
  
  # win
  if 1 == won:
    if 1 == player:
      return 1.0
    else:
      return 0.0
  # draw
  elif -1 == won:
    return 0.0
  else:
    return 0.5

def printBoard(board):
	size = len(board)
	for index in range(0,size):
		if board[index] == 1:
			print ('X'),
		elif board[index] == 2:
			print ('O'),
		else:
			print ('_'),

		if ((index+1)%3) == 0:
			print

def hasWinner(board):

	for player in range(1,3):
		tile = tiles[player]

		#check Horizontal
		for i in range(0,3):
			i = i*3
			if (board[i] == tile) and \
			   (board[i+1] == tile) and \
			   (board[i+2] == tile):
				return 1
		# check Vertical
		for i in range(0,3):
			if (board[i] == tile) and \
				(board[i+3] == tile) and \
				 (board[i+6] ==tile):
					return 1
		if(board[0] == tile) and \
			(board[4] == tile ) and \
			(board[8] == tile):
			return 1
		if (board[6] == tile) and \
			(board[4] == tile) and \
			(board[2] == tile):
			return 1

	for i in range(0,9):
		if board[i] == 0:
			return 0
		#Draw match
	return -1

def updateBoard(_board, player, index):
  if _board[index] == 0:
    _board[index] = player
    return True
  
  return False

def updateEstimateValueOfS(sPrime, s):
  V[s] = V[s] + alpha*(V[sPrime] - V[s])

def getListOfBlankTiles(board):
	blanks = []
	for i in range(0,9):
		if board[i] == 0:
			blanks.append(i)
	return blanks

def greedyMove():
	maxValue = 0
	maxIndex = 0
	nextMoves = getListOfBlankTiles(board)
	boardIndex = nextMoves.pop()
	board[boardIndex] = 1
	maxIndex = states.index(board)
	maxValue = V[maxIndex]
	board[boardIndex] = 0

	for i in nextMoves:
		board[i] = 1
		idx = states.index(board)
		if V[idx] > maxValue:
			boardIndex = i
			maxIndex = idx
			maxValue = V[idx]
		board[i] = 0
	return boardIndex,maxIndex

alpha = 0.1
create_all_states(board,1)
create_all_states(board,2)
totalStates = len(states)
print ("Total States: %d" %(totalStates) )

numPlayer1Won = 0
numPlayer2Won = 0
numDraws = 0
prevIndex = 0          # previous state index
maxIndex = 0 

player = 1
while(1):
	initBoard()
	player = random.randint(1,3)

	print ("Player 1 = Computer")
	print ("Player 2 = You!")

	printBoard(board)

	while(True):

		nextMoves = getListOfBlankTiles(board)
		countNextMoves = len(nextMoves)
		exploring = False

		print("Player %d's move : " %(player))

		if player == 2:

			userPlay = int(raw_input("Enter move [1-9]: "))
			userPlay = userPlay -1

		else:
			ex = random.randint(1,100)/(100.0)
			if ex<= 0.1:
				userPlay = nextMoves[random.randint(0,countNextMoves-1)]
				exploring = True
				print ("exploring")
			else:
				userPlay,maxIndex = greedyMove()
				print ("greedy")
				print ("V(s) = %f changed to" %(V[prevIndex])),
				updateEstimateValueOfS(maxIndex, prevIndex)
				print ("V(s) = %f" %(V[prevIndex]))
				prevIndex = maxIndex
		if True == updateBoard(board, player, userPlay):
			if exploring:
			  prevIndex = states.index(board)
		else:
			print("Invalid Move")
			continue	
    
		printBoard(board)
	    
		won = hasWinner(board)
		if 1 == won:              #won == 1
		  if 1 == player:
		    numPlayer1Won = numPlayer1Won + 1
		  else:
		    maxIndex = states.index(board)
		    print ("V(s) = %f changed to" %(V[prevIndex])),
		    updateEstimateValueOfS(maxIndex, prevIndex)
		    print ("V(s) = %f" %(V[prevIndex]))
		    numPlayer2Won = numPlayer2Won + 1
		  print ("Player %d has won!" %(player))
		  print
		  break
	    
		if -1 == won:           #won == -1
			numDraws = numDraws + 1
			#maxIndex = states.index(board)
			#print "V(s) = %f changed to" %(V[prevIndex]),
			#updateEstimateValueOfS(maxIndex, prevIndex)
			#print "V(s) = %f" %(V[prevIndex])
			print ("It's a draw!")
			print
			break
	    
		player = switchPlayer(player)
		print

	if raw_input("Play Again[y]: ") != "y":
		break

print
print ("-----")
print ("Game Stats: ")
print ("Player 1 # of Wins  : %d" %(numPlayer1Won))
print ("Player 2 # of Wins  : %d" %(numPlayer2Won))
print ("         # of Draws : %d" %(numDraws))

