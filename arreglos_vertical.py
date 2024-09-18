import numpy as np 
from tabulate import tabulate

mt= np.random.randint(0,101, size=(10000,1000))
mt[321][5]=60
np.set_printoptions(threshold=np.inf,linewidth=np.inf, suppress=True)

print(mt)
print(mt[321][5])