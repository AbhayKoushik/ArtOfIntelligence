import random
import math 	
import turtle
import turtlegraphics as tg

def Utility_Value(board):
	if winnerH(board):
		return -1
	elif draw(board):
		return 0
	elif winnerM(board):
		return 1

goal=([0,1,2],[1,2,3],[4,5,6],[5,6,7],[8,9,10],[9,10,11],[12,13,14],[13,14,15],
       [0,4,8],[1,5,9],[2,6,10],[3,7,11],[4,8,12],[5,9,13],[6,10,14],[7,11,15],
       [0,5,10],[2,5,8],[1,6,11],[3,6,9],[4,9,14],[6,9,12],[5,10,15],[7,10,13])

winners=('H','-','M')
def init(board=[]):
	if len(board)==0:
		board=['-' for i in range(16)]
	else:
		board=board
	return board

def show(board):
	for a in [board[i:i+4] for i in range(0,len(board),4)]:
		print(a)

def actions(board):
		return [a for a,i in enumerate(board) if a<4 and i is '-' or a>=4 and i is '-' and board[a-4] is not '-']

def Terminal_test(board):
	if '-' not in [i for i in board]:
		return True
	if winner(board)!='-':
		return True
	return False
	
def winnerH(board):
	return winner(board)=='H'

def winnerM(board):
	return winner(board)=='M'

def draw(board):
	return Terminal_test(board)==True and winner(board) is '-'

def get_player_positions(board,player):
	return [i for i, j in enumerate(board) if j==player]

def winner(board):
	for	player in ('H','M'):
		positions=get_player_positions(board,player)
		for i in goal:
			win=True
			for p in i:
				if p not in positions:
					win=False
			if win:
				return player
	return '-'

def result(board,position,player):
	board[position]=player
	return board

def get_enemy(player):
	if player=='H':
		return 'M'
	return 'H'

def Minimax(board, player):      #Min_Value and Max_value functions of minimax have been integrated here.
	if Terminal_test(board):
  		return Utility_Value(board)
	else:
		best = 0
		for move in actions(board):
		    result(board, move, player)
		    val=Minimax(board,get_enemy(player))
		    result(board,move,'-')
		    if player == 'M':      #Max_Value
		    	if val > best:
		    		best = val
		    else:
		    	if val < best:     #Min_Value
		    		best = val
		return best  		

def alphabeta(board,player,alpha,beta):  #Min_Value and Max_value functions of alphabeta have been integrated here.
	if Terminal_test(board):
		return Utility_Value(board)
	for action in actions(board):
		board=result(board,action,player)
		v=alphabeta(board,get_enemy(player),alpha,beta)
		board=result(board,action,'-')
		# print(v)      #prints the utility values 
		if player=='M':           #Max_Value
			if v>alpha:
				alpha=v
			if alpha>=beta:
				return beta
		else:					  #Min_Value 
			if v<beta:
				beta=v

			if beta<=alpha:
				return alpha

	if player == 'M':
		return alpha
	else:
		return beta

def decideAB(board,player):      #This integrator module for deciding the move
	a=-2
	choices=[]
	for action in actions(board):
		board=result(board,action,player)
		v=alphabeta(board,get_enemy(player),-2,2)
		board=result(board,action,'-')
		if v>a:
			a=v
			choices=[action]
		elif v==a:
			choices.append(action)

	return random.choice(choices)

def decideMM(board,player):     #This integrator module for deciding the move
	a=-2
	choices=[]
	for action in actions(board):
		board=result(board,action,player)
		v=Minimax(board,get_enemy(player))
		board=result(board,action,'-')
		if v>a:
			a=v
			choices=[action]
		elif v==a:
			choices.append(action)

	return random.choice(choices)	

def moveIt(board,player):
	move=int(input("Next Move: "))-1
	if move in actions(board):
		board=result(board,move,player)
		tg.inMap(move,player)
		return
	else:
		print("Please choose from the available")
		moveIt(board,player) 

def decideDumb(board,player):
	return random.choice(actions(board))


def playMinimax(number):
	board=init()
	win=turtle.Screen()
	# show(board)
	tg.drawGrid()
	turtle.right(90)
	while not Terminal_test(board):
		player='M'
		print("wait...")
		print("machine M playing")
		if number==1:
			M_move=decideAB(board,player)
		elif number==2:
			M_move=decideDumb(board,player)	
		# print("M_move",M_move)
		board=result(board,M_move,player)
		print()
		show(board)
		print()	
		tg.inMap(M_move,player)
		if Terminal_test(board):
			break
		player=get_enemy(player)
		acts=actions(board)
		acts[:]=[x+1 for x in acts]
		print("available moves: ",acts)
		moveIt(board,player)
		show(board)
	print("WINNER is ",winner(board))
	print("")
	return 1
	# turtle.exitonclick()
	


