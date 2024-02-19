from math import *
from turtle import *
bgcolor("lightblue")
width(7)
speed(3)
#ვხატავთ მიწას
color("green")
penup()
goto(-1000,0)
pendown()
begin_fill()
forward(2000)
right(90)
forward(500)
right(90)
forward(2000)
right(90)
forward(500)
end_fill()
right(90)
penup()
goto(0,0)
pendown()
#step 1 - drawing a square

color("blue")
forward(160)
left(90)


forward(160)
left(90)

forward(160)
left(90)

forward(160)
left(90)



penup()

goto(160,160)

pendown()
begin_fill()

left(120)
forward(sqrt(71 * 71+ 142 *142))
left(120)
forward(sqrt(71 * 71+ 142 *142))
end_fill()
penup()
goto(-200,0)
pendown()
left(120)
forward(160)
left(90)
forward(160)
left(90)
forward(160)
left(90)
forward(160)
left(90)
penup()
goto(-40,160)
pendown()
begin_fill()
left(120)
forward(sqrt(71 * 71+ 142 *142))
left(120)
forward(sqrt(71 * 71+ 142 *142))
end_fill()
penup()
goto(200,0)
pendown()
left(120)
forward(160)
left(90)
forward(160)
left(90)
forward(160)
left(90)
forward(160)
penup()
goto(360,160)
pendown()
#მესამე სახლის სახურავი
begin_fill()
left(210)
forward(sqrt(71* 71 + 142 * 142))
left(120)
forward(sqrt(71* 71 + 142 * 142))
end_fill()
#ხეები
penup()
goto(-50,-250)
pendown()
begin_fill()
left(210)
color("#4D2D18")
forward(100)
left(90)
forward(25)
left(90)
forward(100)
left(90)
forward(25)
end_fill()
penup()
goto(-62.5,-150)
pendown()
color("darkgreen")
begin_fill()
circle(50)
end_fill()
penup()
goto(-380,180)
pendown()
color("yellow")
begin_fill()
circle(100)
end_fill()











exitonclick()