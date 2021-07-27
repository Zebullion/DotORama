#Made by JWolf
#import turtle
from turtle import Turtle,Screen
from random import randint


#define main function 
def main():
  #declare imports as variables
  t=Turtle()
  s = Screen()
#set bg color and tweak turtle
  t._tracer(0)
  s.bgcolor('Black')
  t.speed(0)
  t.penup()

  colors: list = ['hotpink','orange','cyan']

  for dot in range(1000):
    x =  randint(-100,100)
    y = randint(-100,100)
    t.goto(x,y)
    size = randint(1,10)

    if x<-50:
      t.dot(size,colors[0])
    elif x>=-50 and x<0:
      t.dot(size,colors[1])
    elif x>=0 and x<=50:
      t.dot(size,colors[2])
    elif x>=50:
      t.dot(size,colors[0])

    if y>75:
      t.dot(size,'green')


  s.mainloop()





main()