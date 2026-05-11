import numpy as np
array1=np.array([[1, 2, 3, 4]])
array2=np.array([[5], [6], [7], [8]])
print(array1.shape)
print(array2.shape)

#broadcasting if both the arrays have same number of dimensions and the size of each dimension is either same or one of them is 1 then we can perform broadcasting

print(array1+array2)