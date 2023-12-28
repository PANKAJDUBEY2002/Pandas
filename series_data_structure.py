# import pandas and numpy module
import numpy as np
import pandas as pd



# create series from scalar value
data=10,20,30,40
index=1,2,3,4
a=pd.Series(data)
b=pd.Series(data,index)
print(a)
print(b)




#crreate series from list
data=[10,20,30,40]
index=[1,2,3,4]
a=pd.Series(data)
b=pd.Series(data,index)
print(a)
print(b)





#create series from dictionary
data={1:10,2:20,3:30,4:40}
a=pd.Series(data)
b=pd.Series(data)
print(a)
print(b)


# create deries from hetrogeneous
data=[10,'hello',30.6,40]
index=[1,2,3,4]
a=pd.Series(data)
print(a)



#create series from nd-array
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[7,8,9],[10,11,12]])
data=a1,a2
index=0,1
a=pd.Series(data,index)
print(a)










