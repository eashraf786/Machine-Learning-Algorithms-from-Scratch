import openpyxl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
wb = openpyxl.load_workbook("example.xlsx")
ws = wb["Sheet1"]
#x = list(range(1,101))
x = [3,9,18,42,122]
y = [i*100000 for i in range(1,6)]
#y = []
#for i in range(2,102):
#    y.append(ws['C'+str(i)].value)
plt.plot(x,y,label='Data',marker='o')
def lin(x, a, b):
 return [a*x1+b for x1 in x]
def logar(x, a, b):
 return [a*np.log(x1)+b for x1 in x]
def quad(x, a, b, c):
 return [a*x1**2+b*x1+c for x1 in x]
popt, _ = curve_fit(lin, x, y)
a, b = popt
#print('y = %.5f * x + %.5f' % (a, b))
y1 = lin(x,a,b)
e = list(100*(abs(np.array(y1)-np.array(y))/y))
err = sum(e)/100
print("Linear MAPE = ",err, "%")
plt.plot(x, y1, color='red',label='Linear Fit')

popt, _ = curve_fit(logar, x, y)
a, b = popt
y1 = logar(x,a,b)
e = list(100*(abs(np.array(y1)-np.array(y))/y))
err = sum(e)/100
print("Logarithmic MAPE = ",err, "%")
plt.plot(x, y1, color='green',label='Log Fit')

popt, _ = curve_fit(quad, x, y)
a, b, c = popt
y1 = quad(x,a,b,c)
e = list(100*(abs(np.array(y1)-np.array(y))/y))
err = sum(e)/100
print("Quadratic MAPE = ",err, "%")
plt.plot(x, y1, color='orange',label='Quad Fit')
plt.legend()
plt.show()