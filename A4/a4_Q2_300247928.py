
raw_input = input("Please input a list of numbers separated by space: ").strip().split()
float_input = [float(x) for x in raw_input] #int automatically strips strings of whitespace
def two_length_run(float_input):
    '''(list)->int
    Description: Returns true if list has atleast one run and false otherwise
    Preconditions: raw_input must be a list of integers seperated by spaces
    '''
    y=None
    for x in float_input:
        if (x==y):
            return True
        y=x
    return False
print(two_length_run(float_input))
    
