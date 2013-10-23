import urllib2
response = urllib2.urlopen("http://bus.artuvic.com/account.json?id=1").read()

print response


##def parse(jsonstr):
##    """This function takes in a Json string and prints out the formatted version of the string"""
##    #indent=
##    if jsonstr[0]!='{':
##        print error
##    else:

def keyvalue(strng, indent):
    if strng[0] == '{':
        strng = strng[1:len(strng)-1]
        
    #print strng
    index=strng.index(':')
    key=strng[:index]
    value = strng[index+ 1:]
        
    
    strtype=Whatis(value)
    print strtype
    if strtype==0:
        
        if value.find(',', 0, len(value)) > 0:
            rest = value[value.index(',')+ 1:]
            value=value[:value.index(',')]
            print indent + key+("=>")+value
            if (value[-1] == '}' or value[-1] == ']') and rest[0] != '{':
                keyvalue(rest, indent[:-4])
            elif rest[0] == '{':
                print "-----"
                keyvalue(rest, indent)
            else:
                keyvalue(rest, indent)
        
    elif strtype==1:
        print indent+ key
        keyvalue(value, indent + "    ")
    elif strtype==2:
        print indent + key
        value = value[1:len(value)-1]
        keyvalue(value, indent + "    ")
        

def Whatis(strng):
    if strng[0]=='[':
        return 2
    elif strng[0]=='{':
        return 1
    else:
        return 0 
    
def print_pair(strng):
    index=strng.index(':')
    key=strng[:index]
    value = strng[index+ 1:]
    print key+("=>")+value

    
keyvalue(response,"")    
    
