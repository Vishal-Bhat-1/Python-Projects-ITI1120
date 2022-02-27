raw_input = input("Please input a list of numbers separated by space: ").strip().split()
float_input = [float(x) for x in raw_input] #int automatically strips strings of whitespace
def longest_run(float_input):
    '''(list)->int
    Description: Returns lenght of longest run
    Preconditions: raw_input must be a list of integers seperated by spaces
    '''
    count=0
    y=None
    for x in float_input:
        if (x==y):
            count=count+1
        y=x
    return count
print(longest_run(float_input))
