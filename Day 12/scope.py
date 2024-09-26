##### scope #####

#global scope 
b= 3

def var():
    #Local scope
    a=2
    print(a)
    print(b)

#print(a)    not accessible
print(b)
var()