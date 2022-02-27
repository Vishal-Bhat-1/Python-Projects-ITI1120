import math
def sum_odd_divisors(n):
    """
    Type: (int) -> int
    Description: Returns the sum of positive odd divisors
    Precondition: Must be a positive integer
    """
    if(n==0):
        return None
    else:
        count=0
        n2 = int(abs(n))
        for x in range(1,(n2+1),2):
            if ((n2%x)==0):
                count = count + x
        if(n2==2):
            return 1
        else:
            return count
        
print(sum_odd_divisors(9))
print(sum_odd_divisors(-9))
print(sum_odd_divisors(1))
print(sum_odd_divisors(2))
print(sum_odd_divisors(3))
print(sum_odd_divisors(7))
print(sum_odd_divisors(-2001))
print(sum_odd_divisors(12))

def series_sum():
    """
    Type: (none) -> int
    Description: function should return the sum of the following series 1000 + 1/12 +1/22 + 1/32 + 1/42 + ... + 1/n2 for the given integer n
    Precondition: Must be a non negative integer
    """
    n = int(input("Please enter a non-negative integer:"))
    if(n<0):
        return None
    else:
        count = 1000
        for y in range(n):
            if(y!=0):
                count = count + (1/(y**2))
        return count
print(series_sum())


def pell(n):
    """
    Type: (int) -> int
    Description: If n is negative, pell returns None. Else, pell returns the nth Pell number 
    Precondition: Must be a non-negative integer
    """
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n>1):
        y = 1
        z = 0
        for x in range(n-1):
              pell = z + (y*2)
              z=y
              y=pell
        return pell
print(pell(3))
print(pell(6))
print(pell(-45))
print("\n\n\n")
print(pell(1743))

def countMembers(s):
    """
    Type: (string) -> none
    Description: count how many times extraordinairy characters appear in a string 
    Precondition: Must be a string
    """
    s1 = "efghij"
    s2 = "FGHIJKLMNOPQRSTUVWX"
    count = 0
    for a in (s):
        for b in range(len(s1)-1):
            if(a==s1[b]):
                count = count + 1
        for c in range(len(s2)-1):
            if(a==s2[c]):
                count = count + 1
        if(a=="!"):
            count = count + 1
        if(a==","):
            count = count + 1
        if(a=="\\"):
            count = count + 1
        for g in range(2,6):
            if(a==str(g)):
                count = count + 1
    return count
        
print(countMembers("hi23F!,\\"))
print(countMembers("2aAb3?eE'_13"))
print(countMembers("one, Two"))
print(countMembers("1\'"))
print(countMembers("\\"))
print(countMembers("2\'"))
print(countMembers("one, Two"))


def casual_number(s):
    """
    Type: (string) -> int
    Description: Returns an integer representing a whole number without commas
    Precondition: Must be a string
    """
    s2=""
    count2=0
    for x in s:
        if x not in " ,0123456789-":
            return None
            break
        if x in "0123456789":
            s2=s2+x
            count2=0
        if(count2==1 and x not in "0123456789"):
            return None
            break
        if("-" in x or "," in x):
            count2=count2+1
        
    return int(s2)

print(casual_number("12,465"))
print(casual_number("999,999,999,876"))
print(casual_number("-1,000,001"))
print(casual_number("-,,,,"))
print(casual_number("--97,251"))
print(casual_number("-97251"))
print(casual_number("1,aba,251"))
print(casual_number("1,251"))

def alienNumbers(s):
    """
    Type: (string) -> int
    Description: Adds all the values for the symbols in a given phrase to calculate the number for alien linguistics
    Precondition: Must be a string
    """
    
    return ((1024*s.count('T')) + (598*s.count('y')) + (121*s.count('!')) + (42*s.count('a')) + (6*s.count('N')) + (1*s.count('U')))
print(alienNumbers("a!ya!U!NaU"))
print(alienNumbers("aaaUUU"))
print(alienNumbers(""))

def alienNumbersAgain(s):
    """
    Type: (string) -> int
    Description: Adds all the values for the symbols in a given phrase to calculate the number for alien linguistics
    Precondition: Must be a string
    """
    count=0
    for x in s:
        if x==('T'):
            count=count+1024
        if x==('y'):
            count=count+598
        if x==('!'):
            count=count+121
        if x==('a'):
            count=count+42
        if x==('N'):
            count=count+6
        if x==('U'):
            count=count+1
    return count
print(alienNumbersAgain("a!ya!U!NaU"))
print(alienNumbersAgain("aaaUUU"))
print(alienNumbersAgain(""))

def encrypt(s):
    """
    Type: (string) -> string
    Description: Writes an encrypted message by writing message backwrds , then start on either side, and bring the characters together
    Precondition: Must be a string
    """
    s1 = ""
    count = 0
    #print(int(math.floor((len(s)/2))))
    #print(s[-1])
    for x in range(int(math.floor((len(s)/2)))):
        #print("x: " + str(x))
        if(x==0):
            s1=s1+s[(len(s)-1)]+ s[0]
            #print (s1)
        for y in range(2):
            if (x!=0):    
                if(y==0):
                    s1=s1+s[(-1*x)-1]
                    #print (s1)
                if(y==1):
                    s1=s1+s[x]
                    #print (s1)
    if(len(s)%2==1):
        s1=s1+s[int(math.floor((len(s)/2)))]          
    return s1
print(encrypt(""))
print(encrypt("Hello, world"))
print(encrypt("1234"))
print(encrypt("12345"))
print(encrypt("1"))
print(encrypt("Secret Message"))
print(encrypt(",'4'r"))
print(encrypt("12"))
print(encrypt("123"))


def oPify(s):
    """
    Type: (string) -> string
    Description: returns a string with the letters o and p inserted between every pair of consecutive characters of s. If the first character in the pair is uppercase, it inserts an uppercase O. If however,
    it is lowercase, it inserts the lowercase o. If the second character is uppercase, it inserts an uppercase P. If however, it
    is lowercase, it inserts the lowercase p. If at least one of the character is not a letter in the alphabet, it does not insert
    anything between that pair. Finally, if s has one or less characters, the function returns the same string as s
    Precondition: Must be a string
    """
    s1 = ""
    count=0
    count2=0
    count3=0
    if(len(s)==1):
        s1=s
    else:
        for x in range(len(s)):
                for alphabet in range(97,123,1):
                    if(ord(s[x].lower())==alphabet):
                        count=count+1
                    if(x+1<len(s)):
                        if(ord(s[x+1].lower())==alphabet):
                            count2=count2+1
                            
                if(count==0):
                    s1 = s1+s[x]
                    if(count2!=0):
                        s1=s1+s[x+1]
                        count2=0
                else:
                    if(x==0):
                        s1=s1+s[x]
                    for y in range(2):
                        if (y==0 and x!=len(s)-1):
                            if(count!=0 and count2!=0):                           
                                if (s[x].lower()==s[x]):
                                    s1=s1+"o"
                                else:
                                    s1=s1+"O"
                        if(y==1):
                            if(x+1>=len(s)):
                                print("")
                            elif(s[x+1].lower()==s[x+1]):
                                if(count2!=0):
                                    s1=s1+"p"+s[x+1]
                                    count2=0
                            else:
                                if(count2!=0):
                                    s1=s1+"P"+s[x+1]
                                    count2=0
                    count=0
    return s1
print(oPify("aC234f5g"))
print(oPify("abCd22efg"))
print(oPify("abcdef22x"))
print(oPify("ooo"))
print(oPify("aB"))
print(oPify("aa"))
print(oPify("abCd22efg"))
print(oPify("aBCdef22x"))
print(oPify("x"))
print(oPify("123456"))
print(oPify("ax1"))
print(oPify("X"))

def nonrepetitive(s):
    """
    Type: (string) -> boolean
    Description: The function returns True if the inputted string is nonrepetitive and False otherwise
    Precondition: Must be a string
    """
    s1=""
    s2=""
    count=0
    for x in range(len(s)): #looping through each element in s
        for z in range(len(s)):
            for y in range((x+1)): #length of the substring :
                if(x+1+y+z<len(s)):
                    s1=s1+s[y+z]
                    s2=s2+s[x+1+y+z]
                    #print(s1,s2)
                else:
                    #print("jello")
                    count=count+1
            if(count>0):
                count=0
                s1=""
                s2=""

            elif(s1==s2):
                #print("here is s1" + s1)
                return False
                break
            else:
                #print("Went here")
                s1=""
                s2=""
    return True
print(nonrepetitive("borborygmus"))
print(nonrepetitive("abracadabra"))
print(nonrepetitive("abcab"))
print(nonrepetitive("12341341"))
print(nonrepetitive("44"))
print(nonrepetitive(""))
print(nonrepetitive("zrtzghtghtghtq"))
print(nonrepetitive("123234"))








    

                











    





    
