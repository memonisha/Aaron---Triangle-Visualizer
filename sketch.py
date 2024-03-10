from p5 import *


def setup():
  createCanvas(windowWidth, windowHeight)
  global a,b,c
  a=createMovableCircle(100,200,10)
  b=createMovableCircle(300,100,10)
  c=createMovableCircle(100,100,10)

  
def draw():
  global a,b,c
  background('black')
  drawTickAxes()
  noStroke()
  a.draw()
  b.draw()
  c.draw()
  strokeWeight(3)
  stroke("yellow")
  line(a.x,a.y,b.x,b.y)
  stroke("red")
  line(a.x,a.y,c.x,c.y)
  stroke("blue")
  line(b.x,b.y,c.x,c.y)




