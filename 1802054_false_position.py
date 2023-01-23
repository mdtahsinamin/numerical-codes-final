import math


def func(x):
  func = 0.95*(pow(x,3))-5.9*(pow(x,2))+10.9*x-6
  return func

def false_position():
  ea = 100 
  xl = 3   
  xu = 4  
  xold=0
  i=1
  while ea > 0.1:  
    xr = xu - (func (xu) * (xl - xu) / (func (xl) - func (xu)))  
    ea = ((xr - xold) / xr) * 100 
    sign_check=func(xr) * func(xl) 
    if sign_check < 0: 
      xu = xr
    else:
      xl = xr
    
    xold = xr 
    print("Iteration",i)
    print("Absolute Error", ea)
    print("Root",xr)
    i=i+1
    

def main():
    false_position()
main()