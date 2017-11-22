import turtle as t

wt=t.Screen()
t1=t.Turtle()
queryList=[]
queryListDone=0
conditionList=[]    
conditionListDone=0

t1.penup()
t1.goto(-300, 800)
t1.pendown()
t1.color("blue")
t1.write("Please be patient until your clicked button turns yellow",font=("Arial", 21,"normal"))
t1.penup()

from threading import Thread
from time import sleep

def threaded_function(arg,t1):
    for i in range(arg):
        print("running thread")
        sleep(1)

def drawBigButton(word):
    t1.color("green")
    t1.begin_fill()
    t1.pendown()
    t1.forward(100)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.penup()
    t1.end_fill()
    t1.color("red")
    t1.write(word,font=("Arial", 15,"normal"))
    
def clickedBigButton(word):
    t1.color("yellow")
    t1.begin_fill()
    t1.pendown()
    t1.forward(100)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.penup() 
    t1.end_fill()
    t1.color("red")
    t1.write(word,font=("Arial", 15,"normal"))
        
def drawButton(letter):
    t1.color("green")
    t1.begin_fill()
    for i in range(4):
        t1.pendown()
        t1.forward(50)
        t1.right(90)
        t1.penup()
    t1.end_fill()
    t1.color("red")
    t1.write(letter,font=("Arial", 15,"normal"))
    
def clickedButton(letter):
    t1.color("yellow")
    t1.begin_fill()
    for i in range(4):
        t1.pendown()
        t1.forward(50)
        t1.right(90)
        t1.penup()
    t1.end_fill()
    t1.write(letter,font=("Arial", 15,"normal"))
    
def buttons():
    #t1.goto(0,0)
    #drawButton()
    t1.color("black")
    t1.goto(-400,600)
    t1.write("Query variables",font=("Arial", 20, "normal"))
    t1.goto(200,600)
    t1.write("Conditional variables",font=("Arial", 20, "normal"))
    
    # Column 1
    t1.goto(-400,500)
    drawButton("A")
             
    t1.goto(-400,500-1*75)
    drawButton("B")
               
    t1.goto(-400,500-2*75)
    drawButton("C")
    
    t1.goto(-400,500-3*75)
    drawButton("D")
               
    t1.goto(-400,500-4*75)
    drawButton("F")
    
    t1.goto(-400,500-5*75)
    drawButton("G")
    
    t1.goto(-400,500-6*75)
    drawButton("H")
    
    t1.goto(-400,500-7*75)
    drawButton("L")
    
    t1.goto(-400,500-8*75)
    drawButton("N")
    
    t1.goto(-400,500-9*75)
    drawButton("O")
               
    t1.goto(-400,500-10*75)
    drawButton("P")
    
    t1.goto(-400,500-11*75)
    drawButton("R")
    
    t1.goto(-400,500-12*75)
    drawButton("T")
    
    t1.goto(-400,500-13*75)
    drawButton("X")
    
    t1.goto(-400,500-14*75)
    drawButton("Y")
    
    # Column 2
    t1.goto(-200,500)
    drawButton("~A")
               
    t1.goto(-200,500-1*75)
    drawButton("~B")
               
    t1.goto(-200,500-2*75)
    drawButton("~C")
    
    t1.goto(-200,500-3*75)
    drawButton("~D")
               
    t1.goto(-200,500-4*75)
    drawButton("~F")
    
    t1.goto(-200,500-5*75)
    drawButton("~G")
    
    t1.goto(-200,500-6*75)
    drawButton("~H")
    
    t1.goto(-200,500-7*75)
    drawButton("~L")
    
    t1.goto(-200,500-8*75)
    drawButton("~N")
    
    t1.goto(-200,500-9*75)
    drawButton("~O")
               
    t1.goto(-200,500-10*75)
    drawButton("~P")
    
    t1.goto(-200,500-11*75)
    drawButton("~R")
    
    t1.goto(-200,500-12*75)
    drawButton("~T")
    
    t1.goto(-200,500-13*75)
    drawButton("~X")
    
    t1.goto(-200,500-14*75)
    drawButton("~Y")

    # Column 3
    t1.goto(200,500)
    drawButton("A")
               
    t1.goto(200,500-1*75)
    drawButton("B")
               
    t1.goto(200,500-2*75)
    drawButton("C")
    
    t1.goto(200,500-3*75)
    drawButton("D")
               
    t1.goto(200,500-4*75)
    drawButton("F")
    
    t1.goto(200,500-5*75)
    drawButton("G")
    
    t1.goto(200,500-6*75)
    drawButton("H")
    
    t1.goto(200,500-7*75)
    drawButton("L")
    
    t1.goto(200,500-8*75)
    drawButton("N")
    
    t1.goto(200,500-9*75)
    drawButton("O")
               
    t1.goto(200,500-10*75)
    drawButton("P")
    
    t1.goto(200,500-11*75)
    drawButton("R")
    
    t1.goto(200,500-12*75)
    drawButton("T")
    
    t1.goto(200,500-13*75)
    drawButton("X")
    
    t1.goto(200,500-14*75)
    drawButton("Y")
    
    # Column 4
    t1.goto(400,500)
    drawButton("~A")
               
    t1.goto(400,500-1*75)
    drawButton("~B")
               
    t1.goto(400,500-2*75)
    drawButton("~C")
    
    t1.goto(400,500-3*75)
    drawButton("~D")
               
    t1.goto(400,500-4*75)
    drawButton("~F")
    
    t1.goto(400,500-5*75)
    drawButton("~G")
    
    t1.goto(400,500-6*75)
    drawButton("~H")
    
    t1.goto(400,500-7*75)
    drawButton("~L")
    
    t1.goto(400,500-8*75)
    drawButton("~N")
    
    t1.goto(400,500-9*75)
    drawButton("~O")
               
    t1.goto(400,500-10*75)
    drawButton("~P")
    
    t1.goto(400,500-11*75)
    drawButton("~R")
    
    t1.goto(400,500-12*75)
    drawButton("~T")
    
    t1.goto(400,500-13*75)
    drawButton("~X")
    
    t1.goto(400,500-14*75)
    drawButton("~Y")
  
def drawResults():
    t1.color("Black")
    t1.goto(-700,-700)
    t1.write("Generated query P("+str(queryList)+"|"+str(conditionList)+")",font=("Arial", 20,"normal"))
    t1.goto(-700,-800)
    t1.write("Answer = Answer",font=("Arial", 20 ,"normal"))    
    
def drawButtons():
    t1.penup()
    buttons()
    t1.goto(-400,700)
    drawBigButton("Done")
    t1.goto(200,700)
    drawBigButton("Done")
 
def clickQuery(x,y):
    print("InQuery")    
    t1.penup()
    t1.goto(x,y)
    if x<-300 and x>-400:
        if y<700 and y>650:
            t1.goto(-400,700)
            clickedBigButton("Done")
            global queryListDone
            queryListDone=1
                
    if x<-350 and x>-400:
        if y<500 and y>450:
            if "A" not in queryList and "~A" not in queryList:
                t1.goto(-400,500)
                clickedButton("A")
                queryList.append("A")
        if y<500-1*75 and y>450-1*75:
            if "B" not in queryList and "~B" not in queryList:
                t1.goto(-400,500-1*75)
                clickedButton("B")
                queryList.append("B")
        if y<500-2*75 and y>450-2*75:
            if "C" not in queryList and "~C" not in queryList:
                t1.goto(-400,500-2*75)
                clickedButton("C")
                queryList.append("C")
        if y<500-3*75 and y>450-3*75:
            if "D" not in queryList and "~D" not in queryList:
                t1.goto(-400,500-3*75)
                clickedButton("D")
                queryList.append("D")
        if y<500-4*75 and y>450-4*75:
            if "F" not in queryList and "~F" not in queryList:
                t1.goto(-400,500-4*75)
                clickedButton("F")
                queryList.append("F")
        if y<500-5*75 and y>450-5*75:
            if "G" not in queryList and "~G" not in queryList:
                t1.goto(-400,500-5*75)
                clickedButton("G")
                queryList.append("G")
        if y<500-6*75 and y>450-6*75:
            if "H" not in queryList and "~H" not in queryList:
                t1.goto(-400,500-6*75)
                clickedButton("H")
                queryList.append("H")
        if y<500-7*75 and y>450-7*75:
            if "L" not in queryList and "~L" not in queryList:
                t1.goto(-400,500-7*75)
                clickedButton("L")
                queryList.append("L")
        if y<500-8*75 and y>450-8*75:
            if "N" not in queryList and "~N" not in queryList:
                t1.goto(-400,500-8*75)
                clickedButton("N")
                queryList.append("N")
        if y<500-9*75 and y>450-9*75:
            if "O" not in queryList and "~O" not in queryList:
                t1.goto(-400,500-9*75)
                clickedButton("O")
                queryList.append("O")
        if y<500-10*75 and y>450-10*75:
            if "P" not in queryList and "~P" not in queryList:
                t1.goto(-400,500-10*75)
                clickedButton("P")
                queryList.append("P")
        if y<500-11*75 and y>450-11*75:
            if "R" not in queryList and "~R" not in queryList:
                t1.goto(-400,500-11*75)
                clickedButton("R")
                queryList.append("R")        
        if y<500-12*75 and y>450-12*75:
            if "T" not in queryList and "~T" not in queryList:
                t1.goto(-400,500-12*75)
                clickedButton("T")
                queryList.append("T")
        if y<500-13*75 and y>450-13*75:
            if "X" not in queryList and "~X" not in queryList:
                t1.goto(-400,500-13*75)
                clickedButton("X")
                queryList.append("X")
        if y<500-14*75 and y>450-14*75:
            if "Y" not in queryList and "~Y" not in queryList:
                queryList.append("Y")
                t1.goto(-400,500-14*75)
                clickedButton("Y")
                
    if x<-150 and x>-200:
        if y<500 and y>450:
            if "A" not in queryList and "~A" not in queryList:
                t1.goto(-200,500)
                clickedButton("~A")
                queryList.append("~A")
        if y<500-1*75 and y>450-1*75:
            if "B" not in queryList and "~B" not in queryList:
                t1.goto(-200,500-1*75)
                clickedButton("~B")
                queryList.append("~B")
        if y<500-2*75 and y>450-2*75:
            if "C" not in queryList and "~C" not in queryList:
                t1.goto(-200,500-2*75)
                clickedButton("~C")
                queryList.append("~C")
        if y<500-3*75 and y>450-3*75:
            if "D" not in queryList and "~D" not in queryList:
                t1.goto(-200,500-3*75)
                clickedButton("~D")
                queryList.append("~D")
        if y<500-4*75 and y>450-4*75:
            if "F" not in queryList and "~F" not in queryList:
                t1.goto(-200,500-4*75)
                clickedButton("~F")
                queryList.append("~F")
        if y<500-5*75 and y>450-5*75:
            if "G" not in queryList and "~G" not in queryList:
                t1.goto(-200,500-5*75)
                clickedButton("~G")
                queryList.append("~G")
        if y<500-6*75 and y>450-6*75:
            if "H" not in queryList and "~H" not in queryList:
                t1.goto(-200,500-6*75)
                clickedButton("~H")
                queryList.append("~H")
        if y<500-7*75 and y>450-7*75:
            if "L" not in queryList and "~L" not in queryList:
                t1.goto(-200,500-7*75)
                clickedButton("~L")
                queryList.append("~L")
        if y<500-8*75 and y>450-8*75:
            if "N" not in queryList and "~N" not in queryList:
                t1.goto(-200,500-8*75)
                clickedButton("~N")
                queryList.append("~N")
        if y<500-9*75 and y>450-9*75:
            if "O" not in queryList and "~O" not in queryList:
                t1.goto(-200,500-9*75)
                clickedButton("~O")
                queryList.append("~O")
        if y<500-10*75 and y>450-10*75:
            if "P" not in queryList and "~P" not in queryList:
                t1.goto(-200,500-10*75)
                clickedButton("~P")
                queryList.append("~P")
        if y<500-11*75 and y>450-11*75:
            if "R" not in queryList and "~R" not in queryList:
                t1.goto(-200,500-11*75)
                clickedButton("~R")
                queryList.append("~R")        
        if y<500-12*75 and y>450-12*75:
            if "T" not in queryList and "~T" not in queryList:
                t1.goto(-200,500-12*75)
                clickedButton("~T")
                queryList.append("~T")
        if y<500-13*75 and y>450-13*75:
            if "X" not in queryList and "~X" not in queryList:
                t1.goto(-200,500-13*75)
                clickedButton("~X")
                queryList.append("~X")
        if y<500-14*75 and y>450-14*75:
            if "Y" not in queryList and "~Y" not in queryList:
                queryList.append("~Y")
                t1.goto(-200,500-14*75)
                clickedButton("~Y")
                    
    thread = Thread(target = threaded_function, args = (1,t1))
    thread.start()
    thread.join()
    return

def clickConditional(x,y):
    print("InConditional")    
    t1.goto(x,y)
    if x<300 and x>200:
        if y<700 and y>650:
            t1.goto(200,700)
            clickedBigButton("Done")
            global conditionListDone
            conditionListDone=1
    
    if x<250 and x>200:
        if y<500 and y>450:
            if "A" not in conditionList and "~A" not in conditionList:
                t1.goto(200,500)
                clickedButton("A")
                conditionList.append("A")
        if y<500-1*75 and y>450-1*75:
            if "B" not in conditionList and "~B" not in conditionList:
                t1.goto(200,500-1*75)
                clickedButton("B")
                conditionList.append("B")
        if y<500-2*75 and y>450-2*75:
            if "C" not in conditionList and "~C" not in conditionList:
                t1.goto(200,500-2*75)
                clickedButton("C")
                conditionList.append("C")
        if y<500-3*75 and y>450-3*75:
            if "D" not in conditionList and "~D" not in conditionList:
                t1.goto(200,500-3*75)
                clickedButton("D")
                conditionList.append("D")
        if y<500-4*75 and y>450-4*75:
            if "F" not in conditionList and "~F" not in conditionList:
                t1.goto(200,500-4*75)
                clickedButton("F")
                conditionList.append("F")
        if y<500-5*75 and y>450-5*75:
            if "G" not in conditionList and "~G" not in conditionList:
                t1.goto(200,500-5*75)
                clickedButton("G")
                conditionList.append("G")
        if y<500-6*75 and y>450-6*75:
            if "H" not in conditionList and "~H" not in conditionList:
                t1.goto(200,500-6*75)
                clickedButton("H")
                conditionList.append("H")
        if y<500-7*75 and y>450-7*75:
            if "L" not in conditionList and "~L" not in conditionList:
                t1.goto(200,500-7*75)
                clickedButton("L")
                conditionList.append("L")
        if y<500-8*75 and y>450-8*75:
            if "N" not in conditionList and "~N" not in conditionList:
                t1.goto(200,500-8*75)
                clickedButton("N")
                conditionList.append("N")
        if y<500-9*75 and y>450-9*75:
            if "O" not in conditionList and "~O" not in conditionList:
                t1.goto(200,500-9*75)
                clickedButton("O")
                conditionList.append("O")
        if y<500-10*75 and y>450-10*75:
            if "P" not in conditionList and "~P" not in conditionList:
                t1.goto(200,500-10*75)
                clickedButton("P")
                conditionList.append("P")
        if y<500-11*75 and y>450-11*75:
            if "R" not in conditionList and "~R" not in conditionList:
                t1.goto(200,500-11*75)
                clickedButton("R")
                conditionList.append("R")        
        if y<500-12*75 and y>450-12*75:
            if "T" not in conditionList and "~T" not in conditionList:
                t1.goto(200,500-12*75)
                clickedButton("T")
                conditionList.append("T")
        if y<500-13*75 and y>450-13*75:
            if "X" not in conditionList and "~X" not in conditionList:
                t1.goto(200,500-13*75)
                clickedButton("X")
                conditionList.append("X")
        if y<500-14*75 and y>450-14*75:
            if "Y" not in conditionList and "~Y" not in conditionList:
                conditionList.append("Y")
                t1.goto(200,500-14*75)
                clickedButton("Y")

    if x<450 and x>400:
        if y<500 and y>450:
            if "A" not in conditionList and "~A" not in conditionList:
                t1.goto(400,500)
                clickedButton("~A")
                conditionList.append("~A")
        if y<500-1*75 and y>450-1*75:
            if "B" not in conditionList and "~B" not in conditionList:
                t1.goto(400,500-1*75)
                clickedButton("~B")
                conditionList.append("~B")
        if y<500-2*75 and y>450-2*75:
            if "C" not in conditionList and "~C" not in conditionList:
                t1.goto(400,500-2*75)
                clickedButton("~C")
                conditionList.append("~C")
        if y<500-3*75 and y>450-3*75:
            if "D" not in conditionList and "~D" not in conditionList:
                t1.goto(400,500-3*75)
                clickedButton("~D")
                conditionList.append("~D")
        if y<500-4*75 and y>450-4*75:
            if "F" not in conditionList and "~F" not in conditionList:
                t1.goto(400,500-4*75)
                clickedButton("~F")
                conditionList.append("~F")
        if y<500-5*75 and y>450-5*75:
            if "G" not in conditionList and "~G" not in conditionList:
                t1.goto(400,500-5*75)
                clickedButton("~G")
                conditionList.append("~G")
        if y<500-6*75 and y>450-6*75:
            if "H" not in conditionList and "~H" not in conditionList:
                t1.goto(400,500-6*75)
                clickedButton("~H")
                conditionList.append("~H")
        if y<500-7*75 and y>450-7*75:
            if "L" not in conditionList and "~L" not in conditionList:
                t1.goto(400,500-7*75)
                clickedButton("~L")
                conditionList.append("~L")
        if y<500-8*75 and y>450-8*75:
            if "N" not in conditionList and "~N" not in conditionList:
                t1.goto(400,500-8*75)
                clickedButton("~N")
                conditionList.append("~N")
        if y<500-9*75 and y>450-9*75:
            if "O" not in conditionList and "~O" not in conditionList:
                t1.goto(400,500-9*75)
                clickedButton("~O")
                conditionList.append("~O")
        if y<500-10*75 and y>450-10*75:
            if "P" not in conditionList and "~P" not in conditionList:
                t1.goto(400,500-10*75)
                clickedButton("~P")
                conditionList.append("~P")
        if y<500-11*75 and y>450-11*75:
            if "R" not in conditionList and "~R" not in conditionList:
                t1.goto(400,500-11*75)
                clickedButton("~R")
                conditionList.append("~R")        
        if y<500-12*75 and y>450-12*75:
            if "T" not in conditionList and "~T" not in conditionList:
                t1.goto(400,500-12*75)
                clickedButton("~T")
                conditionList.append("~T")
        if y<500-13*75 and y>450-13*75:
            if "X" not in conditionList and "~X" not in conditionList:
                t1.goto(400,500-13*75)
                clickedButton("~X")
                conditionList.append("~X")
        if y<500-14*75 and y>450-14*75:
            if "Y" not in conditionList and "~Y" not in conditionList:
                conditionList.append("~Y")
                t1.goto(400,500-14*75)
                clickedButton("~Y")
                
    thread = Thread(target = threaded_function, args = (1,t1))
    thread.start()
    thread.join()
    return

def main():
    drawButtons()
    print("DrawingDone")
    t1.pendown()
    print(len(queryList))
    while len(queryList)<10 and queryListDone!=1:
        wt.onclick(clickQuery,btn=1)
        t1.penup()
        t1.goto(0,0)
    
    print("thread queryList finished...exiting")    
    print(queryList)
    while len(conditionList)<10 and conditionListDone!=1:
        wt.onclick(clickConditional,btn=1)
        t1.penup()
        t1.goto(0,0)
    print("thread queryList finished...exiting")    
    print(conditionList)
    drawResults()
    t.mainloop()
main()
        
