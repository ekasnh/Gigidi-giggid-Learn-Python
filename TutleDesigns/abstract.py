import turtle

tu = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
tu.pencolor("red")
tu.left(900)
tu.backward(100)
tu.speed(10)
tu.shape('turtle')

def tree(i):
  if i<1:
    return
  else:
    tu.forward(i)
    tu.color("orange")
    tu.circle(20)
    tu.color("brown")
    tu.left(300)
    tree(3*i/4)
    tu.left(300)
    tu.backward(i)
    
tree(100)     
turtle.done()
