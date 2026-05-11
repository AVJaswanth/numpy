import numpy as np
array=np.array([1, 2, 3, 4])
arr=np.array([[1,2,3],[4,5,6]])
print(arr.ndim)
print(arr.shape )  
ans=arr[0,0]+arr[1,0]
print(ans)
print(arr[0:2])
print(arr[:,0])
print(arr[:,0:3])
print(arr[0:2,0:2])
array=array*2
print(array)
print(array.ndim)
print(type(array))