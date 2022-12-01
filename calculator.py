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
s=input("Start a calculation then enter start\n Stop a calculation then enter stop")          
a=input("Enter the 1st number ")
a=int(a)
op=input("Enter the Operator ")
b=int(input("Enter the 2nd numder "))
while (s=="start"):
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
    s=input("Start a calculation then enter start\nStop a calculation then enter stop") 
    if(s=="start"):
        a=input("Enter the 1st number ")
        a=int(a)
        op=input("Enter the Operator ")
        b=int(input("Enter the 2nd numder ")) 


