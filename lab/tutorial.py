# To calculate the decimals of pi using the wallic formula
# lets try to comute till the hundreadth term
import numpy as np

x = [(4*(i**2))/(4*(i**2)-1) for i in range(1,1000)]
x = np.array(x)
y = 1
for i in range(999):
    y = y * x[i]

y = 2 * y 
print(" y = {}".format(y))
print("len(x) = {}".format(len(x)))



