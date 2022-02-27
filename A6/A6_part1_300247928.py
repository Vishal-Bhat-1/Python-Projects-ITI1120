import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    pass
    file_name = None
    count=0
    while count==0:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name).read().splitlines()#removed .splitlines()
            count=count+1
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None
            count=0
    return f 

def lines(fp,d):
    for line in fp:
    #print (line)
        for y in line:
            #line=line.lower()
            d[y]=0
        
def alpha(d2,d):
    for x in d2: #O(n)
        if len(x)<2:
            d.pop(x)
        elif x.isalpha()==False:
            for y in x:
                if y in string.punctuation:
                    #print(y)
                    x2=x.replace(str(y),'')
                    d[x2]=d[x]
                    #print(str(d[x]))
                    #print("x: " + str(x))
            #if d[x].isalpha()==False:
            d.pop(x)
    #print(d)

def make_dict(d,fp,s,count):
    for z in d:
        #print("z: " + str(z))
        for line in fp:
            #line.strip(string.punctuation)
            lines=set(line)
            count=count+1
            #print("lines: " + str(lines))
            if z in lines:
                s.add(count)
        d[z]=s
        s=set()
        count=0
        
def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    d={}
    s=set()
    count=0
    fp = [x.lower().split(' ') for x in fp] #O(n)
    lines(fp,d)
    d2=d.copy()     
                
    make_dict(d,fp,s,count)

    alpha(d2,d)
    return d

    pass

def punc(query):
    for a in string.punctuation:
        query=query.replace(a,"")
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    #print(D)
    d=set()
    d2={}
    l2=[]
    l=[]
    s=""
    count=0
    punc(query)  
    #print(query,type(query))
    for x in query:
        count=count+1
        if x != " ":
            s=s+x
        else:
            l.append(s)
            s=""
        if count==len(query):
            l.append(s)        
    count2=0
    for x in l:
        #print(x)
        if x in D:
            count2=count2+1
        if str(x) in D:
            d2[x]=D[x]
            l2.append(D[x])
    if count2==0:
        print("Word '" + str(query) + "' not in the file")
        return ""
    else:
        c = list(set(l2[0]).intersection(*l2[1:]))
        c.sort()
        if len(c)>0:
            print("The one or more words you entered coexisted in the following lines of the file:\n")
            return c
        else:
            print("The one or more words you entered does not coexist in a same line of the file.")
            return ""
    pass
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
#query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
# YOUR CODE GOES HERE
#print("The one or more words you entered coexisted in the following lines of the file:\n",find_coexistance(d,query))
cue=0
while cue==0:
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if 'q' in query:
        c=2
        break
    print(find_coexistance(d,query))
    

