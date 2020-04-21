
import numpy as np


A = np.random.random((4, 4))


A[A< 0.5]

a = np.random.random(12)
a

'''array([ 0.77841574,  0.39654203,  0.38188665,  0.26704305,  0.27519705,
        0.78115866,  0.96019214,  0.59328414,  0.52008642,  0.10862692,
        0.41894881,  0.73581471])'''
 A = a.reshape(3, 4)



  a = a.ravel()#converting one-dimension array


A = np.arange(16).reshape((4, 4))
A
'''array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])'''

[B,C] = np.hsplit(A, 2) #horizantal split

print(B)

'''array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]])'''
print(C)

'''
array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])'''


[B,C] = np.vsplit(A, 2) #vertical split
B
'''
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])'''
C
'''
array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])'''
