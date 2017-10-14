import turtlegraphics as tg
import MiniMax as mm
import math
import turtle
		
if __name__=="__main__":
	print("\tHere's an intelligent game! \n\tYou can never beat the intelligent machine\n")

	print("The rules are fairly simple")
	print("\n\t# Its similar to tic-tac-toe")
	print("\t# You need to make three blue coins in a row")
	print("\t# You can only incrementally append your blue coin to the columns")
	print("\nTo make it easier, available moves are shown before you make a move")
	print("Same rules apply to the machine")
	print("")
	print("The strategies with which you can challenge a machine are: ")
	print("\n")
	print("\t1: Using AlphaBeta, a quicker variant of MiniMax strategy")
	print("")
	print("\t2: Play against a dumb machine")
	print("")
	print("       -1: Exit")
	n=int(input("Enter your option: "))
	if n!=1 and n!=2 and n!=3 and n!=-1:
		print("Enter correct option")
		n=int(input("Enter option: "))
	win=turtle.Screen()
	print("Click on the cancel window if not wanting to play")
	while(n!=-1):
		if n==1:
			a=mm.playMinimax(1)
			if a==1:
				break
		elif n==2:
			a=mm.playMinimax(2)
			if a==1:
				break		
		n=int(input("Enter option: "))
	print("Game over")

