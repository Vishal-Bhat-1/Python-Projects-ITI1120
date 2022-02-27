import math
def min_enclosing_rectangle(radius, x, y):
    """
    Type: (number,number,number) -> number
    Description: Returns the x and y coordinates of the bottom left corner of the smallest possible rectangle to enclose a circle, given the radius and coordinates of the center provided 
    Precondition: Radius must be non-negative real number, x and y must be real numbers
    """
    if(radius>=0):
        recX = x-radius
        recY = y-radius
        return recX, recY
#print(min_enclosing_rectangle(50, 1000, 2000))

def vote_percentage(results):
    """
    Type: (string) -> float
    Description: Returns percentage of yes among yes and no votes and ignores the abstained votes
    Precondition: The string results has at least one yes or no and the only words present are yes, no and/or abstained
    """
    count=0
    count2=0
    for char in results:
        if char in 'yY':
            count = count+1
        if char in 'oO':
            count2 = count2+1
    return count/(count2+count)
#print(vote_percentage("('yes yes yes yes yes abstained abstained yes yes yes yes')"))

def vote():
    """
    Type: (string) -> string
    Description: Asks user to enter all yes-s and no-s and abstained-s votes. The function then prints the outcome of the vote (If all the votes are yes, then the proposal passes "unanimously", if at least 2/3 of the votes are yes,then the proposal passes with "super majority", if at least 1/2 of the votes are yes, then the proposal passes by "simplemajority", and otherwise it fails.)
    Precondition: The string results has at least one yes or no and the only words present are yes, no and/or abstained
    """
    vote = input("Enter the yes, no, abstained votes one by one and then press enter:")
    if (vote_percentage(vote)==1):
        print("proposal passes unanimously")
    elif (vote_percentage(vote)>=(2/3)):
        print("proposal passes with super majority")
    elif (vote_percentage(vote)>=(1/2)):
        print("proposal passes with simple majority")
    else:
        print("proposal fails")
    return " "
vote()

def l2lo(w):
    """
    Type: (number) -> int, number
    Description: Returns a pair of numbers (l,o) such that w = l + o/16 and l is an integer and o is a non-negative number smaller than 16 
    Precondition: w is a non-negative number, l is an integer and o is a non-negative number less than 16 
    """
    o = (w-math.floor(w))*16
    l = w-(o/16)
    if(o==l):
        o=5
    return l,o
#print(l2lo(9.25))
