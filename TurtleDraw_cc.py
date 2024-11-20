TEXTFILENAME = 'turtle-draw.txt'

import turtle

print('')
print('Turtle Draw - cpc')
print('')

cpc = turtle.Turtle()
cpc.speed(10)


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
        
        cpc.pendown()
        cpc.goto(x,y)
    
    
    line = turtleDrawTextfile.readline()
    
turtle.done()
print('\nEnd')

