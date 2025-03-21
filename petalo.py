from turtle import *
import colorsys

# Agregar el texto en la cabecera
header_text = "Para vos"  
color("white")
penup()
goto(-180, 250)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))
penup()

# Configurar velocidad y fondo
speed(20)
bgcolor("black")
h = 0

# Dibujar el tallo verde del girasol
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()
penup()

# Dibujar los pétalos del girasol
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Dibujar el centro marrón del girasol
penup()
goto(-20, 0)
pendown()
color("brown")
begin_fill()
circle(44)
end_fill()

done()

