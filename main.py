
import turtle as t 

t.speed(30)

pattern=1

for i in range (100):
    for color in ["black","blue"]:
        t.color(color)
        t.forward(pattern)
        t.right(90)
        t.left(45)
        pattern+=1