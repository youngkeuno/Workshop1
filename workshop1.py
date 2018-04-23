from graphics import *
win = GraphWin("Hey", 500, 400)

new_point = win.getMouse()
x = new_point.getX()
y = new_point.getY()
print("X-coordinate is: ")
print(x)
print("Y -coordinate is: ")
print(y)

pnt= Point(x,y)
circle= Circle(pnt, 20)
circle.draw(win)

new_point2 = win.getMouse()
a = new_point2.getX()
b = new_point2.getY()
print("X-coordinate is: ")
print(a)
print("Y -coordinate is: ")
print(b)

pnt1= Point(a-30,b-30)
pnt2= Point(a+30, b+30)
rctngle= Rectangle(pnt1, pnt2)
rctngle.draw(win)

new_point3 = win.getMouse()
c = new_point3.getX()
d = new_point3.getY()

pnt3= Point(c-30,d-30)
pnt4= Point(c+30, d+30)
rctngle2= Rectangle(pnt3, pnt4)
rctngle2.draw(win)

new_point4 = win.getMouse()
e = new_point4.getX()
f = new_point4.getY()


if e<250 and f<250:
 rctngle2.move(-70,-70)
else:
 rctngle2.move(70,70)
 



input("press a key to continue")
