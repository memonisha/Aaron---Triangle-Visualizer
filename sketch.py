from p5 import *


def setup():
  createCanvas(windowWidth, windowHeight)
  global a,b,c
  a=createMovableCircle(100,200,15)
  b=createMovableCircle(300,100,15)
  c=createMovableCircle(100,100,15)

#(200,300) ---green
#(500,400)
  
def draw():
  global a,b,c
  background('black')
  drawTickAxes()
  noStroke()
  textSize(20)
  fill('green')
  a.draw()
  text(f"({a.x},{a.y})",width-150,height-50)
  fill('blue')
  b.draw()
  text(f"({b.x},{b.y})",width-150,height-100)
  fill('orange')
  c.draw()
  text(f"({c.x},{c.y})",width-150,height-150)
  strokeWeight(3)
  stroke("yellow")
  line(a.x,a.y,b.x,b.y)
  stroke("red")
  line(a.x,a.y,c.x,c.y)
  stroke("blue")
  line(b.x,b.y,c.x,c.y)


  #finding distances
  distYellow=findDistance(a,b)
  distRed=findDistance(a,b)
  distBlue=findDistance(a,b)

def findDistance(a,b):
  d=round(sqrt((a.x-b.x)**2+(a.y-b.y)**2))
  print(d)
  return d 




