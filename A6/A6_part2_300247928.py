class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle(Point): #inherits all the attributes of Point
    def __init__(self,get_bottom_left, get_top_right, get_color):
        ''' Type: (Rectangle,Point,Point,str) -> None
        Description: initialize bottom_left, top_right, and color of object
        Preconditions: input (Rectangle,Point,Point,str) in this order
        '''
        self.bottom_left_point = get_bottom_left
        self.top_right = get_top_right
        self.color = get_color
        self.x=0
        self.y=0
        #print(str(bottom_left_point.y), str(top_right.y))
        #print(str(self.bottom_left_point),type(self.bottom_left_point),str(int(self.bottom_left_point)))
        #Point.__init__(self, xcoord=self.bottom_left_point.x, ycoord=self.bottom_left_point.y)
        #bottom_left_point.x=self.x+bottom_left_point.x
        #bottom_left_point.y=self.y+bottom_left_point.y
        #Point.__init__(self, xcoord=self.top_right.x, ycoord=self.top_right.y)
    def __repr__(self):
        '''(Rectangle)->str
        Returns string concatenation of (x, y)
        Preconditions: Input rectangle'''
        return 'Rectangle('+str(self.bottom_left_point)+','+str(self.top_right)+','+self.color+')' #add ' ' to color

    def __str__(self):
        '''(Point)->str
        Returns cleaner string version of Point(x, y).
        Preconditions: INput rectangle'''
        #return "I am a " + self.color + "rectangle with bottom left corner at ('+str(self.bottom_left_point) + " + "and top right corner at " + '+str(self.top_right)+',"
        return "I am a " + self.color + " rectangle with bottom left corner at " + (str(self.bottom_left_point)) + " and top right corner at " + (str(self.top_right))

    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns bottom left coordinate of rectangle
        Preconditions: INput rectangle'''
        return self.bottom_left_point


    def get_top_right(self):
        '''(Rectangle)->Point
        Returns top right coordinate of rectangle
        Preconditions: Input rectangle'''
        return self.top_right
    
    def get_color(self):
        '''(Rectangle)->str
        Returns color of rectangle
        Preconditions: Input rectangle'''
        return self.color

    def reset_color(self,newcolor):
        '''(Rectangle)->none
        Resets color
        Preconditions: Input rectangle'''
        self.color=newcolor
        #return self.color
        
    def get_perimeter(self):
        '''(Rectangle)->Number
        Returns perimeter of rectangle
        Preconditions: Input rectangle'''
        perimeter = 2*(self.top_right.x-self.bottom_left_point.x) + 2*(self.top_right.y-self.bottom_left_point.y)
        return perimeter

    def get_area(self):
        '''(Rectangle)->Number
        Returns area of rectangle
        Preconditions: Input rectangle'''
        area = (self.top_right.x-self.bottom_left_point.x) * (self.top_right.y-self.bottom_left_point.y)
        return area      

    def move(self,dx,dy):
        '''(Rectangle,number,number) -> None
        Moves rectangle by (dx,dy)
        Preconditions: Input rectangle'''
        super().move(dx, dy)
        self.bottom_left_point.x=self.x+self.bottom_left_point.x
        self.bottom_left_point.y=self.y+self.bottom_left_point.y
        self.top_right.x=self.x+self.top_right.x
        self.top_right.y=self.y+self.top_right.y
        
    def intersects(self,r2):
        '''(Rectangle,Rectangle) -> bool
        Returns True if the rectangle intersects with the given rectangle, otherwise returns false
        Preconditions: Input rectangle and rectangle you are intersecting it with'''
        if (self.top_right.y < r2.bottom_left_point.y or r2.top_right.y < self.bottom_left_point.y):
            return False;
        
        elif (self.top_right.x < r2.bottom_left_point.x or r2.top_right.x < self.bottom_left_point.x):
            return False;
        
        return True;

    def contains(self,x,y):
        '''(Rectangle,number,number) ->bool
        Returns True if the given point is inside of rectangle and false if not
        Preconditions: Input rectangle and x and y coordinates of the point'''
        if (self.top_right.x>=x and x>=self.bottom_left_point.x and self.top_right.y>=y and y >= self.bottom_left_point.y):
            return True
        else:
            return False
    
    
class Canvas: #inherits all attributes of Rectangles
    def __init__(self):
        '''Type:(Canvas) -> None
        creates a canvas list (compilation of rectangles)
        Preconditions: Input canvas'''
        self.canvas = []

    def add_one_rectangle(self, r1):
        '''Type:(Canvas,Rectangle) -> None
        Adds one rectangle to the canvas list
        Preconditions: must input a canvas and rectangle object'''
        self.canvas.append(r1)

    def count_same_color(self, color):
        '''(Canvas,str) ->int
        Returns the number of rectangles with the given color in the canvas list of rectangles
        Preconditions: must input canvas and type in a color with no spaces,caps, or other symbols and must be singular'''
        
        count=0
        for x in self.canvas:
            if x.color==color:
                count=count+1
        return count

    def total_perimeter(self):
        '''(Canvas) -> number
        Returns the sum of the perimeters of all the rectangles
        Preconditions: INput Canvas
        '''
        count=0
        for x in self.canvas:
            count=count+x.get_perimeter()
        return count

    def min_enclosing_rectangle(self):
        '''(Canvas) -> Rectangle
        Returns minimum enclosing rectangle that contains all the rectangles in the canvas
        Preconditions: Input Canvas'''
        bottomleftx = []
        bottomlefty = []
        toprightx = []
        toprighty = []
        for a in self.canvas:
            bottomleftx.append((a.get_bottom_left().x)) 
            bottomlefty.append(a.get_bottom_left().y)
            toprightx.append((a.get_top_right().x))
            toprighty.append((a.get_top_right().y))
        mbottomleftx = min(bottomleftx)
        mbottomlefty = min(bottomlefty)
        mtoprightx = max(toprightx)
        mtoprighty = max(toprighty)
        
        return Rectangle(Point(mbottomleftx, mbottomlefty), Point(mtoprightx, mtoprighty), 'blue')

    def common_point(self):
        '''(Canvas) ->bool
        Returns True if a point that intersects all rectangles in the canvas exists and False if not
        Preconditions: Input canvas'''
        for x in self.canvas:
            for y in self.canvas:
                if x.intersects(y)==False:
                    return False
        return True

    def __len__(self):
        '''(Canvas) ->int
        Returns the number of rectangles stored in canvas list
        Preconditions: input Canvas'''
        return len(self.canvas)

    def __str__(self):
        '''(Rectangle) ->str
        Returns string version of Canvas list
        Preconditions: input Canvas'''
        return str(self.canvas)

    def __repr__(self):
        '''(Canvas) ->str
        Returns clean,concatenated version of stringed canvas list
        Preconditions: input Canvas'''
        return "Canvas(" + str(self.canvas) + ")"


    
