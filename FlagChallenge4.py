# 900 * 1200 
# 500 * 500
import turtle
turtle.register_shape("rectangle", ((0,0),(0,120),(90,120),(90,0),(0,0)))
turtle.fillcolor("red")
turtle.begin_fill()
turtle.shape("rectangle")
turtle.end_fill()
turtle.done()