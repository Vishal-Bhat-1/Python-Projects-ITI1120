>>> c=Canvas()
>>> len(c)
0
>>> r1=Rectangle(Point(1,1), Point(2,2), "blue")
>>> r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
>>> r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
>>> c.add_one_rectangle(r1)
>>> c.add_one_rectangle(r2)
>>> c.add_one_rectangle(r3)
>>> c.add_one_rectangle( Rectangle(Point(0,0),Point(100,100),"orange") )
>>> len(c)
4
>>> c
Canvas([Rectangle(Point(1,1),Point(2,2),blue), Rectangle(Point(2,2.5),Point(3,3),blue), Rectangle(Point(1.5,0),Point(1.7,3),red), Rectangle(Point(0,0),Point(100,100),orange)])
>>> c.count_same_color("blue")
2
>>> c.count_same_color("red")
1
>>> c.count_same_color("purple")
0
>>> 

>>> c=Canvas()
>>> r1=Rectangle(Point(1,1), Point(2,2), "blue")
>>> r2=Rectangle(Point(1,1), Point(4,4), "blue")
>>> r3=Rectangle(Point(-2,-2), Point(-1,-1), "blue")
>>> c.add_one_rectangle(r1)
>>> c.add_one_rectangle(r2)
>>> c.add_one_rectangle(r3)
>>> c.total_perimeter()
20
>>> c.count_same_color("red")
0
>>> c.count_same_color("blue")
3
>>>


>>> r1=Rectangle(Point(1,1), Point(2,2), "blue")
>>> r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
>>> r1.intersects(r3)
True
>>>

>>> r1=Rectangle(Point(1,1), Point(2,2), "blue")
>>> r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
>>> r1.intersects(r2)
False
>>>

>>> r.contains(1.5,1)
True

>>> r1=Rectangle(Point(), Point(1,1), "red")
>>> r1.get_color()
'red'
>>> r1
Rectangle(Point(0,0),Point(1,1),red)
>>> print(r1)
I am a redrectangle with bottom left corner at Point(0,0)and top right corner at Point(1,1)

>>> print(c)
[Rectangle(Point(1,1),Point(2,2),blue), Rectangle(Point(2,2.5),Point(3,3),blue), Rectangle(Point(1.5,0),Point(1.7,3),red), Rectangle(Point(0,0),Point(100,100),orange)]
>>>

>>> r1=Rectangle(Point(), Point(1,1), "red")
>>> r1.move(2,3)
>>> r1
Rectangle(Point(2,3),Point(3,4),red)

>>> c=Canvas()
>>> r1=Rectangle(Point(1,1), Point(2,2), "blue")
>>> r2=Rectangle(Point(1,1), Point(4,4), "blue")
>>> r3=Rectangle(Point(-2,-2), Point(-1,-1), "blue")
>>> r4=Rectangle(Point(0,-100),Point(1,100), "yellow")
>>> c.add_one_rectangle(r1)
>>> c.add_one_rectangle(r2)
>>> c.add_one_rectangle(r3)
>>> c.add_one_rectangle(r4)
>>> c.min_enclosing_rectangle()
Rectangle(Point(-2,-100),Point(4,100),blue)

>>> c=Canvas()
>>> r1=Rectangle(Point(1,1), Point(2,2), "blue")
>>> r2=Rectangle(Point(1.5,1.5), Point(4,4), "blue")
>>> r3=Rectangle(Point(-2,-2), Point(2,1.5), "blue")
>>> r4=Rectangle(Point(0,-100),Point(1.5,100), "yellow")
>>> c.add_one_rectangle(r1)
>>> c.add_one_rectangle(r2)
>>> c.add_one_rectangle(r3)
>>> c.add_one_rectangle(r4)
>>> c.common_point()
True

>>> c=Canvas()
>>> r1=Rectangle(Point(-2,-2), Point(-1,2), "blue")
>>> r2=Rectangle(Point(-2,-2), Point(2,-1), "blue")
>>> r3=Rectangle(Point(1,-2), Point(2,2), "blue")
>>> r4=Rectangle(Point(-2,1), Point(2,2), "blue")
>>> c.add_one_rectangle(r1)
>>> c.add_one_rectangle(r2)
>>> c.add_one_rectangle(r3)
>>> c.add_one_rectangle(r4)
>>> c.common_point()
False
