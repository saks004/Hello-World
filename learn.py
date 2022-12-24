import os
#check length of the list
mylist=[(1,2),(3,4),(5,6),(7,8)]
length = len(mylist)
print("The number of items in mylist is:" + str(length))

#print the items and store in a new list
mynewlist=[]
for x,y in mylist:
    print(x)
    print(y)
    mynewlist.append(x)
    mynewlist.append(y)
print (mynewlist)

#check for odd or even
for num in mynewlist:
    mod= num%2
    if mod==0:
        print("The number is Even",num )
    else:
        print("The number is Odd", num) 



# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#Recursive function to find the factorial of an interger
def factorial_recursive(x):
    if x<2:
        return (1)
    else:
        return (x * factorial_recursive(x-1))

num= 6
print('The factorial of number', num,'is', factorial_recursive (num))


#Iterative function to find the factorial of an interger

def factorial_iterative(x):
    if x<0:
        return ("Enter a positive interger")
    elif x<2:
        return(1)
    else:
        f = 1
        for i in range(1, x+1):
            f= f*i
        return(f)
n= 7  
print('The factorial of number',n, 'is', factorial_iterative(n)  )


print("sample list",list(range(2,3)))


#Prime function to generate list of prime numbers

def primes():
    terms= int(input("Prime numbers upto: "))
    for i in range(2,terms+1):
        divisor=0
        for j in range(2,i):
            if i%j ==0:
                divisor= divisor+1
        if divisor ==0 or i==2:
            print(i)
primes()


























# get_primes 
# a number divisible by 1 and itself
# a function to return list of prime number
# a function that accepts end limit number (get prime 100)