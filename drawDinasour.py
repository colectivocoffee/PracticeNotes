import turtle

with open("mystery.txt") as tturn:
                
    turtleScreen = turtle.Screen()
    turtleScreen.setworldcoordinates(-300, -300, 400, 400)    
    run = turtle.Turtle()
    run.pencolor("brown")
    
    turnList = []    
    
    for eachTurn in tturn:
        
        turn = eachTurn.split()

        if turn == ["UP"]:
            run.up()
            turnList.append(eachTurn)
        elif turn == ["DOWN"]:
            run.down()
            turnList.append(eachTurn)
        else:
            xy = tuple(int(x) for x in turn)
            run.goto(xy)   
            turnList.append(tuple(int(x) for x in turn)) # turn strings to tuple
            
    
    print(turnList)
    turtleScreen.exitonclick()

    
    