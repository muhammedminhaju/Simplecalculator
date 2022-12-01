def sum(a,b):
  print("Addition ",a+b)
def sub(a,b):
  print("Subtraction ",a-b)
def mul(a,b):
  print("Multiplication ",a*b)
def div(a,b):
  print("Division ",a/b)
def mod(a,b):
  print("Modulo ",a%b)           
a=input("Enter the 1st number ")
a=int(a)
op=input("Enter the Operator ")
b=int(input("Enter the 2nd numder "))
if(op=="+"):
  sum(a,b)
elif(op=="-"):
  sub(a,b)  
elif(op=="/"):
  div(a,b)
elif(op=="*"):
  mul(a,b)  
elif(op=="%"):
  mod(a,b) 


