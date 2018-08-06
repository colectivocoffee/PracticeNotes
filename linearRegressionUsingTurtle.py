'''
Interpret the data file labdata.txt such that each line contains a an x,y coordinate pair. 
Write a function called plotRegression that reads the data from this file and uses a turtle to plot those points and a best fit line according to the following formulas:

y=y¯+m(x−x¯)

m=∑xiyi−nx¯y¯∑x2i−nx¯2

where x¯ is the mean of the x-values, y¯ is the mean of the y- values and n is the number of points. 
If you are not familiar with the mathematical ∑ it is the sum operation. For example ∑xi means to add up all the x values.

Your program should analyze the points and correctly scale the window using setworldcoordinates so that that each point can be plotted. 
Then you should draw the best fit line, in a different color, through the points.

'''


import turtle

xCoord = []
yCoord = []
xiyi = []
xiSquare = []
goFromLinearX = 0 # x values are not being set yet
goFromLinearY = 0 # y values are not being set yet
goToLinearX = 200 # sets where the line is going to
goToLinearY = 0 # y is subject to x
m = 0
meanX = 0
meanY = 0

with open("labdata.txt") as coord:
        
    for eachCoord in coord: 
        
        # To get x coord
        xCoordInt = int(eachCoord.split()[0])
        xCoord.append(xCoordInt)
        
        # To get y coord
        yCoordInt = int(eachCoord.split()[1])
        yCoord.append(yCoordInt)        
    
        # To get xiyiList
        xiyi.append(xCoordInt * yCoordInt)
        
        xiSquare.append(xCoordInt**2)
        
    sumX = sum(xCoord)
    sumY = sum(yCoord)
    
    meanX = float(sum(xCoord)) / max(len(xCoord),1)
    meanY = float(sum(yCoord)) / max(len(yCoord),1)
    
    print(meanX)
    print(meanY)
    
      
    m = (sum(xiyi) - (len(xCoord)*meanX*meanY)) / (sum(xiSquare) - len(xCoord)*(meanX**2))
    print(m)
    
    goFromLinearY = meanY + m*(goFromLinearX - meanX)
    goToLinearY = meanY + m*(goToLinearX - meanX)
    
    print("y", goToLinearY)
    
    
def stampPoints():

    eachPoint = turtle.Turtle()
    eachPoint.up()
    
    for i in range(len(xCoord)):
        eachPoint.setpos(xCoord[i], yCoord[i])
        eachPoint.shape("circle")
        eachPoint.shapesize(0.3,0.3,0.3)
        eachPoint.write((xCoord[i], yCoord[i]))
        eachPoint.stamp()
    


def drawLinearRegression():
    turtleScreen = turtle.Screen()
    turtleScreen.setworldcoordinates(0, 0, 200, 200) #(origin, lowerleftx, lowerlefty, upper right x, upper right y)
    line = turtle.Turtle()
    line.pencolor("brown")
    line.penup()
    line.setposition(goFromLinearX,goFromLinearY)
    line.pendown()
    line.goto(goToLinearX,goToLinearY)
    line.penup()
    stampPoints()
    turtleScreen.exitonclick()

    
      
drawLinearRegression()  
 
    