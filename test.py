
#comment
#adding two strings

def sum (a,b):
    add = a+b
    print (add)
    return(add)

def view (num):
    for x in range(num):
        sum(x,x+1)
view(10)
