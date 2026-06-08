#import libraries
#numpy : used to import by using the standard alias 'np'and it is used data analytics
#NUMPY-->>
import numpy as np

arr = np.array([10,20,30,40,50])
print(arr)
print("Numpy Version ", np.__version__)
print(" ")

#1d array
arr1 = np.array([10,20,30,40,50])
print(arr1)

#2d array
arr2 = np.array([
  [10,20,30],
  [40,50,60]
])
print(arr2)
print(" ")

#array if zeros
zeros_arr = np.zeros(5)
print(zeros_arr)

#2d zeros array
zeros_arr_2d = np.zeros((3,4))
print(zeros_arr_2d)
print(" ")


#array of ones
ones_arr = np.ones(5)
print(ones_arr)

#2d ones array
one_2d = np.ones((2,3))
print(one_2d)
print(" ")


#identity matriz
identity_mat = np.eye(5)
print(identity_mat)


#arrange 
arr1=np.arange(0,20,2)
print(arr1)


#linspace
arrl=np.linspace(0,100,5)
print(arrl)

print(" ")


#random numbers
ran_arr=np.random.rand(5)
print(ran_arr)


#random 2d array
ran_2d_arr=np.random.rand(3,4)
print(ran_2d_arr)

print(" ")

print("....Array Properties....")
data = np.array([
  [10,20,30],
  [40,50,60]
])
print(data)
#shape
print(data.shape)
#size
print(data.size)
#dimension
print(data.ndim)
#data type
print(data.dtype)
#item size
print(data.itemsize)
#total bytes -used to storing the value in what memory
print(data.nbytes)
print(" ")

print("reshape arrays: ")
arr=np.arange(1,13)
print(arr)
#reshaped to 3x4
reshaped = arr.reshape(3,4)
print(reshaped)

print(" ")



print("Vertical Concatenate--->")
a=np.array([
  [1,2],
  [3,4]
])
b=np.array([
  [5,6],
  [7,8]
])
vertical = np.concatenate((a,b),axis=0)
print(vertical)

print("Horizontal Concatenate--->")
horizontal = np.concatenate((a,b),axis=1)
print(horizontal)


print(" ")
print("---Indexing---")

arr=np.array([10,20,30,40,50,60])
print(arr)

print(arr[0])
print(arr[2])
print(arr[4])
print(arr[-2])

print("Slicing-->")
print(arr[0:3])
print(" ")

print("Conditional filtering-->")
arr=np.array([1,2,3,4,5,6,7,8])

print(arr[(arr>3)&(arr<7)])
print(arr[(arr==2 | (arr==8))])
print(arr[~(arr>5)])
print(" ")

print("Scaler operation-->")
arr_=np.array([10,20,30,40])
print(arr_)

print(np.add(arr_,5))
print(np.subtract(arr_,2))
print(np.multiply(arr_,2))
print(np.divide(arr_,2))
print(" ")



print("vector operation-->")
vector_arr1=np.array([10,20,30,40])
vector_arr2=np.array([50,60,70,80])

print(np.add(vector_arr1,vector_arr2))
print(np.subtract(vector_arr1, vector_arr2))
print(np.multiply(vector_arr1, vector_arr2))
print(np.divide(vector_arr1,vector_arr2))
print(np.power(vector_arr1, vector_arr2))
print(" ")


print("Numerical function-->")
arr__=np.array([1,2,3,4,5])
print(arr__)

print(np.sort(arr__))
print(np.sqrt(arr__))
print(np.abs([-10,-20,50.5]))
print(np.ceil([2.1,5.4,8.2]))
print(np.floor([2.9,5.8,8.7]))
print(np.round([2.4,5.8,9.7]))
print(" ")


print("Statistics function-->")
arr_s=np.array([10,20,30,40,50,60])
print(arr_s)

print("Mean: ", np.mean(arr_s))
print("Median: ", np.median(arr_s))
print("SD: ", np.std(arr_s))
print("Min: ", np.min(arr_s))
print("Max: ", np.max(arr_s))
print("Variance: ", np.var(arr_s))
print("Sum: ", np.sum(arr_s))
print(" ")


print("Correlation coefficient-->")
X=np.array([10,20,30,40,50])
Y=np.array([15,25,35,45,55])
print(np.corrcoef(X,Y))
print(" ")



