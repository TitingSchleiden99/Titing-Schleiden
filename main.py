
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
        #This is an octagon
        #Black and Blue are it's main colors
        #It is a pattern
        #It follows an arrow
