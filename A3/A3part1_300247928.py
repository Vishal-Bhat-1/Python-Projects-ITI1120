
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

def split_tester(N, d):
        """
        Type: (string,string) -> string
        Description: Prints a yes or no depending on if the inputted number can split into an increasing size
        Precondition: Must be a string
        """
        n = int(N)
        d = int(d)
        if(n%d==0):
            pair=0
            pair2 = 0
            count=0
            for x in range(d,len(N)+d,d):
                for y in range(d):
                    pair = pair + int(N[(x-1-y)])*(10**y)
                    print (pair)
                    
                if(pair2<pair or pair2==0):
                    if(x==(len(N))):
                        print("The sequence is increasing")
                else:
                    print("no")
                    break
                pair2 = pair
                pair = 0
    # Your code for split_tester function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
        pass

# you can add more function definitions here if you like       


            
# main
# Your code for the welcome message goes here, instead of name="Vida"
flag=True
print(ascii_name_plaque("Welcome to my increasing-splits tester"))
name=input("What is your name?")

while flag:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    else:
        #print(ascii_name_plaque("Welcome to my increasing-splits tester"))
        print("Good choice!")
        split_tester("543654765", "3")
        print(split_tester("12311234","4"))

                
        
    #YOUR CODE GOES HERE. The next line should be elif or else.


        
#finally your code goes here too.

