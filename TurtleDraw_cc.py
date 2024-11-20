import turtle
import math

TEXTFILENAME = 'turtle-draw.txt'

def close_window():
    turtle.bye()

print('')
print('Turtle Draw - cpc')
print('')

screen = turtle.Screen()
screen.setup(width=450, height=450)

cpc = turtle.Turtle()
cpc.speed(10)
cpc.penup()

total_distance = 0
last_position = None

print('Reading a text file.')
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
        cpc.goto(x, y)
        
        if cpc.isdown():
            if last_position:
                distance = math.sqrt((x - last_position[0])**2 + (y - last_position[1])**2)
                total_distance += distance
                
        cpc.pendown()
        last_position = (x, y)
        
    if (len(parts) == 1):
        cpc.penup()
    
    line = turtleDrawTextfile.readline()
    
cpc.goto(175, -175)
cpc.write("Total distance marked: {:.2f}".format(total_distance), align="right")    

turtle.onkey(close_window, "\n")
turtle.listen()
turtle.mainloop()

print('')
print('\nEnd')
print('')