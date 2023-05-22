from turtle import *

#I want to create a house

#drawing a square
speed(2)
width(8)
color("brown")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()                  #end of square

#drawing a door
forward(75)       #height of the door
color("blue")
begin_fill()
left(90)

forward(75)
right(90)

forward(50)
right(90)

forward(75)
right(90)
end_fill()     #end of door

penup() #drawig a roof    
goto(200, 200)
pendown()

color("gray")
begin_fill()
right(45)
forward(140)

left(90)
forward(140)
end_fill()   #end of roof
color("red")
begin_fill()
penup()    #drawing firts window
goto(25, 150)
pendown()
left(45)
forward(35)

left(90)
forward(35)

left(90)
forward(35)

left(90)
forward(35) 
end_fill()  #end firts window

penup()       #drawing second window
color("red")
begin_fill()
goto(175, 150)
pendown()
forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90) 
end_fill()    #end second window
 
exitonclick()