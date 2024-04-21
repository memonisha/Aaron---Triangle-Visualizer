from p5 import *


def setup():
  createCanvas(windowWidth, windowHeight)
  global a,b,c
  a=createMovableCircle(100,200,15)   #green -a
  b=createMovableCircle(300,100,15)  #blue-b
  c=createMovableCircle(100,100,15) #orange-c

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

  global distYellow, distRed, distBlue
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

  angles()
  #orange dot-angleC
  #blue dot-angle B
  #green dot-angleA
  fill("white")
  text(angleA,a.x,a.y)
  text(angleB,b.x,b.y)
  text(angleC,c.x,c.y)

  if angleA==90 or angleB==90 or angleC==90:
    text("right-angled",100,height-50)
  elif angleA>90 or angleB>90 or angleC>90:
    text("obtuse-angled",100,height-50)
  else:
    text("acute-angled",100,height-50)



def findDistance(a,b):
  d=round(sqrt((a.x-b.x)**2+(a.y-b.y)**2))
  return d 

def angles():
  global angleA,angleB,angleC,distYellow,distRed,distBlue
  c=distYellow
  b=distRed
  a=distBlue
  a2=a**2
  b2=b**2
  c2=c**2
  angleA=round(acos((c2+b2-a2)/(2*b*c)))
  angleB=round(acos((c2+a2-b2)/(2*a*c)))
  angleC=180-(angleA+angleB)
  print(angleA,angleB,angleC)
  


'''
https://jamboard.google.com/d/1Q2CvHRx-JLAaCz_HiE8SIMdO-L3ZbqPLYAKhwuKWHng/viewer?mtt=a3cev6v5p6uj&f=3

'''

