#Author: Remel Kabir
#Math 308

import math

'''Write a function named implies(P,Q) that takes as input two boolean
values P and Q and returns the truth value of the statement "P implies Q".'''

def implies(P, Q):
    return not P or Q

''' Write a function named iff(P,Q) that takes as input two boolean values
P and Q and returns the truth value of the statement “P iff Q.” '''

def iff(P, Q):
    return (P==Q)

'''Say that a 2-input truth function is a function which takes as input
two boolean values P and Q and returns a boolean value.
(Examples include xor above, as well as implies and iff from the problems above)
Write a function named logically_equivalent(tf1, tf2) that takes as input
two 2-input truth functions tf1 and tf2 and returns the boolean value of
the statement ”The two truth functions are logically equivalent.” Your function
should return True if and only if the two functions tf1 and tf2 return the same
output whenever they are passed the same input values.
Examples of successful input/output:

  >>> def or_not(P,Q):

      return (not P) or (not Q)

  >>> def not_and(P,Q):

      return not (P and Q)

  >>> logically_equivalent(or_not, not_and)

  True

  >>> def or_function(P,Q):

      return P or Q

  >>> logically_equivalent(or_function, not_and)

  False'''

def logically_equivalent(tf1, tf2):
    if(tf1(True,True)==tf2(True,True)) and (tf1(True,False)==tf2(True,False))and (tf1(False,False)==tf2(False, False)) and (tf1(False,False)==tf2(False,False)):
        return True
    else:
        return False

'''Write a function planar_distance(p,q) which takes as input two points in the
plane and returns the distance between them. Here a point in the plane should be
interpreted as a 2-tuple whose entries are both real numbers.
Examples of successful input/output:

  >>> print(planar_distance( (0,0), (1,1) ))

  1.4142135623730951

  >>> print(planar_distance( (1,1), (4,5) ))

  5.0'''

def planar_distance(P,Q):
    return math.sqrt((Q[0]-P[0])**2+(Q[1]-P[1])**2)

'''Suppose A and B are two sets of numbers. Their sumset is the set
{a+b : a∈Aandb∈B}.
Write a function called sumset(A,B) which takes as input two sets
of numbers A and B and returns their sumset.
Examples of successful input/output:
    
  >>> sumset({1,2,3},{1,2,3})
    
  {2, 3, 4, 5, 6}
    
  >>> sumset({-1,1},{3,10})
    
  {9, 2, 11, 4}'''

def sumset(A,B):
    S = set()
    for i in A:
        for j in B:
            s = i+j #adding each elements of the two sets
            S.add(s) #adding only the elements that are none repeating
    return S #returns the set
