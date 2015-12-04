#Author: Remel Kabir
#Math 308

import cmath


#Problem No.1
def quadratic_maximum(b,c):
    return c-((b**2)/-4)


#Problem No.2
def is_prime(x):
    n = 2
    if x == n: 
        print("True")
    elif x<n:
        print("False")
    else:    
        while x>n:
            if x % n == 0:
                print("Flase")
                break
            n = n + 1
        else:
            print("True")


#Problem No.3
def newtons_method(f, df, x0, n):
    if(n<1): 
        print("The value must be greater than 1 in order to find the root")
        return
    counter=0 
    while(counter != n): 
        x = x0 - f(x0)/df(x0) 
        x0= x 
        counter = counter + 1 
    return x 

