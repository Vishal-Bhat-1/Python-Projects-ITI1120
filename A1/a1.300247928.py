
# Family name: Vida Dujmovic 
# Student number: 300247928 
# Course: IT1 1120 
# Assignment Number 1
# Date: Sept 27, 2021

import math
import turtle

########################
# Question 4
########################
def safe(n):
    """
   Type: (int -> boolean)
   Description: (Returns true or false whether n is a safe integer)
   Precondition: (Must be a non-negative integer that has at most 2 digits (range is 0-99))
    """
    return (bool(n%9!=0))and(bool(n%10!=9))and(bool(n//10!=9))#first boolean checks if it's divisible by 9, second boolean checks if second digit is 9, third boolean checks second digit
print(safe(27))
########################
# Question 5
########################

def quote_maker(quote, name, year):

    """
    Type:(string,string,number) -> string
    Description: Creates a string that concatenates the year, name, and quote given to make a complete sentence
    Precondition: (a string, string, and year must be given in that order) 
    """
    a = "'In " + str(year) + ", a person called " + str(name) + " said: " + quote + "'" #string concatenation
    return a
print(quote_maker("Early bird gets the worm", "Jacob", 2003))

########################
# Question 6
########################

def quote_displayer():
    """
Paramater Type: () -> string 
Description: Prompts for a quote, name, and year and then  print a sentence that concatenates it altogether by calling the previous function
Precondition: quote, name, year must be provided when prompted
"""
    quotePrompt = input("Give me a quote: ")
    namePrompt = input("Who said that?")
    yearPrompt = input("What year did she/he say that?")
    b =(quote_maker(quotePrompt,namePrompt,yearPrompt))
    return b
print(quote_displayer())

########################
# Question 7
########################

def rps_winner():

    """
Type: () -> string, boolean
Description: Displays the result of a rps game given the choices of player 1 and player 2
Precondition: User may only enter the words: rock, paper or scissors in lower case when prompted to make a choice
"""
    p1 = input("What choice did player 1 make? \n Type 1 of the following options: rock, paper or scissors:")
    print(p1)
    p2 = input("What choice did player 2 make? \n Type 1 of the following options: rock, paper or scissors")
    print(p2)
    winner = bool((not p1>p2 or (p1 == "scissors" and p2 == "paper")) and (not (p1 == "paper" and p2 == "scissors")))
    draw = bool(p1!=p2)
    print("Player 1 wins: ",winner)
    print("It is a tie. That is not", draw)

print(rps_winner())

########################
# Question 8
########################

def fun(x):
    """
Type: (number) -> number
Description: Solves the equation 104y=x+3
Precondition: Must be a positive number

"""
    
    y = (math.log(x+3,10))/4
    return y
print(fun(7.2))

########################
# Question 9
########################

def ascii_name_plaque(name):
    """
Type: (string) -> None
Description: Prints a name plaque after name is inputted
Precondition: Must be a string
"""
    name = "   __" + name + "__   "  
    n = len(name)
    stars = "*" * n
    print(stars, "\n" + name, "\n" + stars)
    
print(ascii_name_plaque("Vishal"))

########################
# Question 10
########################


s=turtle.Screen() 
t=turtle.Turtle()

def my_fun_drawing():
    """
Type: () -> None
Description: Draws a train similiar to the one provided with EQUAL complexity using turtle
Precondition: None
"""

    ### Positioning
    t.penup()
    t.goto(-300,-125)
    t.right(90)

    t.fillcolor('Red')
    t.begin_fill()
    t.right(90)
    t.backward(100)
    t.pendown()
    t.backward(175)
    t.right(90)
    t.backward(100)
    t.right(90)
    t.backward(175)
    t.right(90)
    t.backward(100)
    t.right(90)
    t.end_fill()


    t.penup()
    t.right(180)
    t.forward(20)
    t.pendown()

    t.fillcolor('Grey')
    t.begin_fill()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.end_fill()

    t.fillcolor('Black')
    t.begin_fill()
    t.left(180)
    t.forward(40)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(40)
    t.end_fill()
    t.right(90)
    t.forward(40)

    t.right(90)
    t.forward(50)
    t.left(90)

    t.fillcolor('Grey')
    t.begin_fill()
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.end_fill()

    t.fillcolor('Grey')
    t.begin_fill()
    t.forward(10)
    t.right(45)
    t.forward(64)
    t.left(135)
    t.forward(45)
    t.end_fill()

    
    
    t.penup()
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.pendown()
    t.fillcolor('Black')
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.fillcolor('Cyan')
    t.begin_fill()
    t.penup()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.pendown()
    t.circle(15)
    t.end_fill()

    #Stick between wheels
    t.fillcolor('Grey')
    t.begin_fill()
    t.forward(75)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(5)
    t.end_fill()

    #Wheel 2
    t.left(90)
    t.forward(75)
    t.penup()
    t.right(90)
    t.forward(5)
    t.left(90)
    t.fillcolor('Black')
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.fillcolor('Cyan')
    t.begin_fill()
    t.penup()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.pendown()
    t.circle(15)
    t.end_fill()
    
    t.penup()
    t.goto(-50,-125)
    t.pendown()

    t.fillcolor('Grey')
    t.begin_fill()
    t.setheading(90)
    t.circle(20,180)
    t.end_fill()

    t.fillcolor('Grey')
    t.begin_fill()
    t.penup()
    t.goto(-100,-125)
    t.pendown()
    t.setheading(90)
    t.circle(20,180)
    t.end_fill()


    ### Second car
    t.penup()
    t.setpos(-25,-225)
    t.pendown()
    t.fillcolor('Orange')
    t.begin_fill()
    t.left(180)
    t.forward(200)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(120)
    t.right(180)
    t.end_fill()
    
    t.penup()
    t.forward(60)
    t.pendown()

    t.penup()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.fillcolor('Black')
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.fillcolor('Cyan')
    t.begin_fill()
    t.penup()
    t.left(90)
    t.forward(8)
    t.right(90)
    t.pendown()
    t.circle(23)
    t.end_fill()
    
    # Window
    t.penup()
    t.setpos(-5,-70)
    t.pendown()
    t.forward(80)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(60)


    t.penup()
    t.setpos(-20,-30)
    t.pendown()
    t.fillcolor('Black')
    t.begin_fill()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(130)
    t.right(90)
    t.forward(10)
    t.end_fill()

    #Train 3
    t.penup()
    t.setpos(95,-210)
    t.left(90)
    t.pendown()
    t.fillcolor('Black')
    t.begin_fill()
    t.forward(35)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.forward(10)
    t.end_fill()

    t.penup()
    t.setpos(130,-225)
    t.pendown()
    t.fillcolor('Magenta')
    t.begin_fill()
    t.left(180)
    t.forward(300)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(120)
    t.right(180)
    t.end_fill()

    t.penup()
    t.setpos(130,-175)
    t.pendown()
    t.left(90)
    
    t.fillcolor('Brown')
    t.begin_fill()
    t.right(90)
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    t.fillcolor('Brown')
    t.begin_fill()
    t.forward(12) # width/planks = 120/10 = 12
    t.right(90)
    t.forward(50)#225-175=50
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(12)
    t.end_fill()

    #Wheel 1:
    t.penup()
    t.setpos(95,-210)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(60)
    t.pendown()
    t.fillcolor('Black')
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.fillcolor('Cyan')
    t.begin_fill()
    t.penup()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.pendown()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.forward(75)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.fillcolor('Black')
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.fillcolor('Cyan')
    t.begin_fill()
    t.penup()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.pendown()
    t.circle(15)
    t.end_fill()

    #Windows:

    t.penup()
    t.setpos(135,-55)
    t.left(90)
    t.pendown()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(40)

    t.right(90)
    t.penup()
    t.forward(60)
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(40)

    t.penup()
    t.setpos(135,70)
    t.pendown()
    t.fillcolor('Black')
    t.begin_fill()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(130)
    t.right(90)
    t.forward(10)
    t.end_fill()
    
my_fun_drawing() 


########################
# Question 11
########################
def alogical(n):
    """
Type: (number) -> number
Description: Returns the min number of times that a number needs to be divided by 2 in order to get a number equal to or smaller than 1
Precondition: n must be bigger than or equal to 1

"""
    logic = math.ceil(math.log(n,2))
    return logic
print(alogical(7))

########################
# Question 12
########################

def cad_cashier(price,payment):
    """
Type: (float, float) -> float
Description: Returns a real number with 2 decimal places equal to the change the customer is owed in Canadian dollars.
Precondition: the price and payment must be two real non negative numbers with a max of 2 decimal places
"""
    change = payment-price
    roundUp = round((change%0.05)*20,0) * ((1-(((change)%0.05)*20))/20)
    roundDown = round(round((1-((change%0.05)*20)),0),0) * (change%0.05)
    roundedChange = round((change+roundUp-roundDown),2)
    return roundedChange
print(cad_cashier(2.62,2.79))
########################
# Question 13
########################

def min_CAD_coins(price,payment):
    """
Type: (number,number) -> int
Description: Returns 5 numbers that represent the smallest number of coins that equal the change. 
Precondition: The price and payment must be two real non negative numbers with a max of 2 decimal places
"""
    change = cad_cashier(price,payment)
    t = round(change//2)
    l = round((change%2)//1)
    q = round(((change%2)%1)//0.25)
    d = round((((change%2)%1)%0.25)//0.1)
    n = round(((((change%2)%1)%0.25)%0.1)//0.05)
    return (t,l,q,d,n)
    
print(min_CAD_coins(3.27,4,73))
