

raw_input = input("Please input a list of numbers separated by space: ").strip().split()
int_input = [int(x) for x in raw_input] #int automatically strips strings of whitespace
n = int(input("Please input an integer"))
def number_divisible(int_input,n):
    '''(list,int)->int
    Description: Returns the number of integers in the list divisible by n
    Preconditions: raw_input must be a list of integers seperated by spaces, n must be an integer
    '''
    count=0
    for x in int_input:
        if x%n==0:
            count=count+1
    return count
print("The number of elements divisible by " + str(n) + " is " + str(number_divisible(int_input, n)))

    
