import pandas as pd
import numpy as np


serd = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green','green','yellow'])

print(serd["white"])

fks = pd.Series([3,-3,np.NaN,3])

print(fks)

print(fks.isnull())

print(fks.notnull())

print(fks[fks.isnull()])


mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)
print(myseries)

student_marks = {'name' : ['sanad','klasik', 'art','geleneksel'], 'marks':[11,34,45,23]}

df = pd.DataFrame(student_marks)

print(df)


df=pd.DataFrame(np.random.rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
