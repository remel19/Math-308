#Remel kabir
#Math 308

#Problem No.1

def tribonacci(m):
    if (m<1):
        print("The input value must be bigger than 1")
    TS = [] # # initializing an empty list
    t = 0 

    TS.append(t) # initializing the tribonacci sequence 
    TS.append(t) # initializing the tribonacci sequence 
    TS.append(t+1) # initializing the tribonacci sequence 
    while (t<m):
        t = TS[-1]+TS[-2]+TS[-3] # getting the next value and so on
        TS.append(t) # adding the next value to the list and so on
    else:
        TS.remove(TS[-1]) # removing the last value from the list to keep it smaller than m.
        return TS


#Problem No.2
   
def catalan_numbers(n):
    c=[1]
    if n==1:
        return [1]
    for i in range(1,n):
        s=0
        for j in range(i):
            s = s + c[j]*c[i-j-1]
        c.append(s)
    return c
    


#Problem No.3

def multiply(m,n):
    if n == 0:
        return 0 # base case
    else:
        return m+multiply(m, n-1) # recursion


#Problem No.4

def iterate(f,k,x):
    y = f(x) # intailizing 
    if k==1:
        return y #base case
    else:
        return iterate(f, k-1, y) #recursion


#Problem No.5

def cantors_set_contains(n,x):
    return
