import numpy as np

ages=np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
teenagers=ages[ages<18]
adults=ages[(ages>=18) & (ages<60)]
seniors=ages[ages>=60]
print(teenagers)
print(adults)
print(seniors)
dup_adults=np.where(ages>=18,ages,0)
print(dup_adults)