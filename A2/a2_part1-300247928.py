
#Part 1:

import math
import random

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
    return ("")
    
def elementary_school_quiz(flag,n):
    
    """
    Type: (int,int) -> int
    Description: Helps elementary school students practice either exponentiation or logarithm by generating a quiz (num of questions decided by user) and then returning how many questions were answered correctly
    Precondition: flag (first param) must be 0 or 1 and n (second param) must be either 0,1 or 2
    """
        
    if(flag==0):
        count=0
        for i in range(n):
            question = 2**(random.randint(1,10))
            answer = int(input("Question " + str(i+1) + ":\n 2 to what is " + str(question) + " i.e. what is the result of log_2 (" + str(question)+ ")?"))
            if(answer==math.log(question,2)):
                count+=1
        return count

    if(flag==1):
        count2=0
        for x in range(n):
            question = random.randint(1,10)
            answer = int(input("Question " + str(x+1) + ":\n What is the result of 2^" + str(question) + "?"))
            if(answer==(2**question)):
                count2+=1
        return count2
    
#print(elementary_school_quiz(1,2))

def high_school_quiz(a,b,c):
    """
    Type: (real number,real number,real number) -> string
    Description: Finds the real or complex solution to a quadratic or linear equation and determines if the equation is satisfied for all numbers x if a nd b are equal to 0
    Precondition: Must be real numbers
    """
    discriminant = b**2-4*a*c
    if(a==0):
        if(b==0):
            if(c==0):
                print("The quadratic equation " + str(b) + "x + " + str(c) + " = 0 is satisfied for all numbers x")
            else:
                print("The quadratic equation " + str(b) + "x + " + str(c) + " = 0 is satisfied for no number x")
        else:
            linSolution = -c/b
            print("The linear equation " + str(b) + "x + " + str(c) + " = 0 has the following root/solution: " + str(linSolution))
    elif(discriminant > 0):
        solution1 = (-b+((discriminant)**0.5))/(2*a)
        solution2 = (-b-((discriminant)**0.5))/(2*a)
        print("The quadratic equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 has the following real roots: " + str(solution1) + " and " + str(solution2))
    elif(discriminant == 0):
        solution = -b/(2*a)
        print("The quadratic equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 has only one solution, a real root: \n" + str(solution))
    else:
        real = -b/(2*a)
        imaginary = ((-discriminant)**0.5)/(2*a)

        print("The quadratic equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 has the following 2 complex roots: " + str(real) + " + i " + str(imaginary) + " and " + str(real) + " - i " + str(imaginary))
    return " "

#print(high_school_quiz(0,0,0))       
    
print(ascii_name_plaque("Welcome to my math quiz-generator"))
userName = input("What is your name?")
school = int(input("Hi " + str(userName) + " Are you in _? Enter\n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?"))
if(school == 1):
    print(ascii_name_plaque(userName + ", welcome to my math quiz-generator for elementary school students."))
    flag = int(input(userName + " what would you like to practice? \nEnter 0 for inverse of exponentiation\n1 for exponentiation"))
    if(flag != 0 and flag != 1):
        print("Invalid choice. Only 0 or 1 is accepted.\nGood bye " + userName + "!")
    else:
        n = int(input("How many practice questions would you like to do? Enter 0, 1, or 2:"))
        if(n != 0 and n != 1 and n!= 2):
            print("Only 0,1 or 2 are valid choices for the number of questions.\nGood bye " + userName + "!")
        elif(n==0):
            print("Zero questions. OK. Good bye\nGood bye " + userName + "!")
        else:
            print(userName + ", here is your " + str(n) + " questions:")
            result = elementary_school_quiz(flag,n)        
            if(result==n):
                    print("Congratulations " + userName +"! You'll probably get an A tomorrow.\nGood bye " + userName + "!")
            elif(result==(n/2)):
                    print("You did ok " + userName + ", but I know you can do better. \nGoodbye " + userName + "!")
            else:
                    print("I think you need some more practice " + userName + ".\nGoodbye " + userName + "!")
    
elif(school == 2):
    print(ascii_name_plaque("quadratic equation, a·x^2 + b·x + c= 0, solver for " + userName))
    flag=True
    while flag:
        question=input(userName + ", would you like a quadratic equation solved?")
        if ((question.lower())!="yes"):
            flag=False
            print("Goodbye  " + userName + "!")
        else:
            print("Good choice!")
            a = int(input("Enter a number the coefficient a: "))
            b = int(input("Enter a number the coefficient b: "))
            c = int(input("Enter a number the coefficient c: "))
            print(high_school_quiz(a,b,c))
else:
    print(userName + " you are not a target audience for this software.\nGood bye " + userName + "!")






    
