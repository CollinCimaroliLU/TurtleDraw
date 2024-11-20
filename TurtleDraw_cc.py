TEXTFILENAME = 'turtle-draw.txt'

import turtle

print('')
print('Turtle Draw - cpc')
print('')

screen = turtle.Screen()
screen.setup(width=450, height=450)

cpc = turtle.Turtle()
cpc.speed(10)
cpc.penup()

print('Reading a text file line by line.')
print('')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')
    
    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        
        cpc.color(color)
        cpc.goto(x,y)
        cpc.pendown()
        
    if (len(parts)  == 1):
        cpc.penup()
    
    line = turtleDrawTextfile.readline()
    
turtle.done()
turtleDrawTextfile.close()


print('\nEnd')

