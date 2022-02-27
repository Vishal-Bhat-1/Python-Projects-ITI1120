import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    # YOUR CODE GOES HERE
    a=-1
    friendList = []
    for x in range(1,len(friends)):
        if a == friends[x][:(friends[x].find(" "))] or x==1:
            friendList.append(int(friends[x][(1+friends[x].find(" ")):]))
        else:
            for y in range(len(network)):
                if int(a) in network[y][1]:
                    friendList.insert(0,network[y][0])
            friendList.sort()
            combineTuple = (int(a),friendList[:])
            network.append(combineTuple)  
            friendList.clear()
            friendList.append(int(friends[x][(1+friends[x].find(" ")):]))
        a = friends[x][:(friends[x].find(" "))]
        if x+1==len(friends):
            for y in range(len(network)):
                if int(a) in network[y][1]:
                    friendList.insert(0,network[y][0])
            friendList.sort()
            combineTuple = (int(a),friendList[:])
            network.append(combineTuple)
            friendList.clear()
            e=""
            g=""
            c=[]
            d=[]
            for z in range(len(network)):
                d.append(network[z][0]) #e was d
                c.append(network[z][1]) #g was c
            c.sort()
            for b in c: #each friend in network
                #print("b: " + str(b) + "  d.count(b): " + str(d.count(b)))
                for m in b:
                    if d.count(m)==0: #if a friend has not been assigned a userID
                        #print("Heyyyyy" + b + str(network[y][1]))
                        for y in range(len(network)):
                            if int(m) in network[y][1]:
                                friendList.append(network[y][0])
                                #print("network[y][0]: " + str(network[y][0]))
                        friendList.sort()
                        combineTuple = (int(m),friendList[:])
                        network.append(combineTuple)
                        friendList.clear()
                        #d=d+b
                        d.append(m)
                        
    #print("Network: " + str(network) + "  length of network: " + str(len(network)))
        
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2


    O(n1 + n2 + log n) were n is the the total number of users in the network, n1 is the number of friends of user1 and n2 is
    the number of friends of user2. In other words, n1 =len(user1), n2 =len(user2) and n =len(network).
    Note that on a typical network O(n1+n2+log n) is much better than O(n) since a network like Facebook has n roughly 2
    billion and the average number of friends per user is 338. Thus the number of operations an O(n) solution would do, would
    be in the order of a billion, roughly. While the number of operations an O(num_friends_user1 + num_friends_user2 + log n)
    solution would do, would be in the order of, O(338 + 338 + 21), thousand, roughly
    Thus O(n) solutions will not be accepted for the bonus
    '''
    common=[]
    
    # YOUR CODE GOES HERE
    
    a=0
    c=len(network)-1 #could also be friends[0]
    mid=0
    mid2=0 #must be declared outside loop so value saves
    
    #Time complexity of below loop: O(2log(n)) using binary search -> O(log(n)) 
    while a <= c:
        mid = (a + c) // 2
        if user1 < int(network[mid][0]):
            c = mid - 1
        elif user1 == int(network[mid][0]):
            c=-1
        else:
            a = mid + 1
    a=0
    c=len(network)-1
    while a <= c:
        mid2 = (a + c) // 2
        if user2 < int(network[mid2][0]):
            c = mid2 - 1
        elif user2 == int(network[mid2][0]):
            a=1
            c=0
        else:
            a = mid2 + 1

    d=0
    e=0
    
    #Time Complexity of below loop: O(n1+n2)
    while d < len(network[mid][1]) and e < len(network[mid2][1]):
        if network[mid][1][d] < network[mid2][1][e]:
            d = d+1
        elif network[mid2][1][e] < network[mid][1][d]:
            e = e+1
        else:
            common.append(network[mid2][1][e])
            e = e+1
            d = d+1
    #Final Time complexity of function: O(n1+n2+logn) (ignoring constants)
    return common
    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    pass
    top=0
    recommend = None
    
    for x in range(len(network)):
        common = getCommonFriends(user, network[x][0], network)
        if len(common)>top and (user not in network[x][1]) and user!=network[x][0]:
            top=len(common)
            recommend = int(network[x][0])
         
    return recommend

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    pass
    count=0
    for x in range(len(network)):
        if len(network[x][1])>=k:
            count+=1
    return count
            
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    pass
    count=0
    for x in range(len(network)):
        if len(network[x][1])>count:
            count=len(network[x][1])
    return count

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    mostFriends = maximum_num_friends(network)
    for x in range(len(network)):
        if len(network[x][1])==mostFriends:
            max_friends.append(network[x][0])
    return    max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    #people_with_most_friends(create_network("net1.txt"))
    count=0
    counter=0
    for x in range(len(network)):
        counter+=1
        count=count+len(network[x][1])
    return count/counter
    pass

def userID(network):
    userID=[]
    for x in range(len(network)):
        userID.append(network[x][0])
    return userID    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    for y in range(len(network)):
        #print(network[y][1])
        if len(network[y][1])==len(userID(network))-1:
            return True
        
    return False

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    # YOUR CODE GOES HERE

    flag=True
    while(flag==True):
        try:
            prompt = int(input("Enter an integer for a user ID:"))
            if prompt in userID(network):
                flag==False
                return prompt
        except:
            print("That was not an integer. Please try again.")
        else:
            print("That user ID does not exist. Try again.")
    
##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
