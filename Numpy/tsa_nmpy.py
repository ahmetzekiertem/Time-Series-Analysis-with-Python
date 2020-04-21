import numpy as np

mylist = [1,2,3]

np.array(mylist)

martix = [[1,2,3],[4,5,6],[7,8,9]]

matarray = np.array(martix)

#listeyle arrayin operasyonlarda cok farki var.


matarray.shape

np.zeros((4,15))


np.ones((5,55))*100


np.linspace(0,100,5)

np.eye(10)

np.random.rand(1)


np.random.rand(5,5) #uniform distribution

np.random.randn(1) # one value with 0 mean and 1 standard deviation



np.random.randn(10) # 10 value with 0 mean and 1 standard deviation

np.random.randint(1,100,10)  #between 1-100 10 value

np.random.seed(100) # initialy choose common random number 

ranarr = np.random.randint(0,50,10)

ranarr

ranarr.reshape(2,5)

ranarr.max()

ranarr.min()

ranarr.argmin()

matarray.sum(axis=0)

matarray.sum(axis=1)








