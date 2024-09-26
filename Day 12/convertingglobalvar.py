#modifying global variable

var = 1
def funct():
    global var
    var+=2
    print(var)

#OR

def func():
    print(f"Value of variable is {var}")
    return var+1
var = func()
print(f"value of variable outside function is after increaing{var}")
funct()