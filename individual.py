import numpy as np
array1=np.array([1, 2, 3, 4])
array2=np.array([5, 6, 7, 8])
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1//array2)

#comparision operator

scores=np.array([90, 80, 70, 50])
ans=scores>80
scores[scores<60]=0
print(scores)
for i in ans:
    print(i)