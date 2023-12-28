# import numpy and pandas module

import numpy as np
import pandas as pd



#make dataframe from dictionary of dict
d1={1:'a',2:'b',3:'c'}
d2={1:"shubham",2:"shyam",4:"sundar"}
data={'first':d1,'second':d2}
a=pd.DataFrame(data)
print(a)





#make dataframe from 2-d array
data=np.array([[1,2,3],[4,5,6]])
a=pd.DataFrame(data)

print(a)





# make dataframe frome series
s1=pd.Series([1,2,3])
s2=pd.Series([4,5,6])
s3=pd.Series([7,8,9])
data={'s1':s1,'s2':s2,'s3':s3}
a=pd.DataFrame(data)
print(a)








#make dataframe by reading csv file
a=pd.read_csv('student.csv')
print(a)
