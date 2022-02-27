# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''

     
     dealer=[]
     other=[]
     
     
     
     for x in range(50):
         if(x<26):
             dealer.append(deck[x])
         else:
             other.append(deck[x]) 
     


     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢'])
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    l.sort()
    count=-1
    count2=0
    no_pairs=l[:]
    for x in range(len(l)):
        count=count+1
        if (x!=len(l)-1 and l[x][0] == l[x+1][0]):
            if (count2==0 and (x<len(l)-3 and l[x+1][0]==l[x+2][0]==l[x+3][0]) ):
                count2=count2+1
                no_pairs.remove(l[x])
                no_pairs.remove(l[x+1])
                no_pairs.remove(l[x+2])
                no_pairs.remove(l[x+3])
            elif(count2==0):
                count2=count2+1
                no_pairs.remove(l[x])
                no_pairs.remove(l[x+1])
            
        else:
            count2=0
        
        
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    random.shuffle(no_pairs)
    return no_pairs
    

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    output=""
    for a in deck:
        output = output + a + " "
    print ("\n" + output + "\n")
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     choice = int(input("I have " + str(n) + " cards. If 1 stands for my first card and " + str(n) + " for my last card, which of my cards would you like?\nGive me an integer between 1 and " + str(n) + ":"))
     while (choice<1 or choice>n):
         choice = int(input("Invalid number. Please enter integer between 1 and " + str(n) + ":"))
         #choice = int(input("I have " + str(n) + " cards. If 1 stands for my first card and " + str(n) + " for my last card, which of my cards would you like?\nGive me an integer between 1 and " + str(n) + ":"))


     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     return choice
def play_game():
     '''()->None
     This function plays the game'''
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)
     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")
     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     ordinal="th"
     flag=False
     while(flag==False):
         print("***********************************************************\nYour turn.\nYour current deck of cards is:")
         print_deck(human)
         myCardInd = get_valid_input(len(dealer))
         myCard = dealer[myCardInd-1]
         if(myCardInd==1):
             ordinal = "st"
         elif(myCardInd==2):
             ordinal = "nd"
         elif(myCardInd==3):
             ordinal = "rd"
         else:
             ordinal = "th"
         print("You asked for my " + str(myCardInd) + ordinal + " card. \nHere it is. It is " + myCard)
         dealer.remove(myCard)
         human.append(myCard)
         print("With " + myCard + " added, your current deck of cards is: ")
         print_deck(human)
         human=remove_pairs(human)
         print("And after discarding pairs and shuffling, your deck is: ")
         print_deck(human)
         wait_for_player()
         print("***********************************************************\nMy turn.")
         yourCardInd = random.randint(1, len(human))
         yourCard = human[yourCardInd-1]
         human.remove(yourCard)
         dealer.append(yourCard)
         dealer=remove_pairs(dealer)
         if(yourCardInd==1):
             ordinal = "st"
         elif(yourCardInd==2):
             ordinal = "nd"
         elif(yourCardInd==3):
             ordinal = "rd"
         else:
             ordinal = "th"
         print("I took your " + str(yourCardInd) + ordinal + " card.")
         wait_for_player()
         if not dealer: #Using python's implicit feature: any list is true except empty ones
             print("***********************************************************")
             print("Ups. I do not have any more cards\nYou lost! I, Robot, win")
             flag=True #when cards are finished
         elif not human:
             print("***********************************************************")
             print("Ups. You do not have any more cards\nCongratulations! You, Human, win")
             flag=True #when cards are finished
         

# main
play_game()
