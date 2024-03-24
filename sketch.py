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
  distRed=findDistance(a,c)
  distBlue=findDistance(b,c)
 
  if distYellow==distRed and distRed==distBlue:
    text("equilateral",100,height-100)
  elif distRed==distYellow or distRed==distBlue or distBlue==distYellow:
    text("isoceles",100,height-100)
  else:
    text("scalene",100,height-100)
  
  noStroke()
  
  midPointXyellow=(a.x+b.x)/2
  midPointYyellow=(a.y+b.y)/2
  fill("black")
  rect(midPointXyellow,midPointYyellow,40,30)
  fill("yellow")
  text(distYellow,midPointXyellow,midPointYyellow)
  
  midPointXred=(a.x+c.x)/2
  midPointYred=(a.y+c.y)/2
  fill("black")
  rect(midPointXred,midPointYred,40,30)
  fill("red")
  text(distRed,midPointXred,midPointYred)


  
  midPointXblue=(b.x+c.x)/2
  midPointYblue=(b.y+c.y)/2
  fill("black")
  rect(midPointXblue,midPointYblue,40,30)
  fill("blue")
  text(distBlue,midPointXblue,midPointYblue)





def findDistance(a,b):
  d=round(sqrt((a.x-b.x)**2+(a.y-b.y)**2))
  print(d)
  return d 




