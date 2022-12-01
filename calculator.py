def design1():
    line="----------------------------------------".center(40)
    print("\n||{}||".format(line))
    print("||               Calculator               ||")
    print("||{}||".format(line)) 
    print("||{}||".format("Start a calculation then enter 'start'".center(40)))
    print("||{}||".format("Stop a calculation then enter 'stop'".center(40)))
    s=input("||{}||=>".format(" ".center(40)))  
    print("||{}||".format(line)) 
    print("||{}||".format(s.center(40)))
    print("||{}||".format(line)) 
    return s
def design2():
    line="----------------------------------------".center(40)
    print("||{}||".format(line))
    a=input("||{}||=>".format("Enter the 1st number ".center(40)))
    print("||{}||".format(line))
    a=int(a)
    print("||{}||".format("Enter the Operator".center(40)))
    print("||{}||".format(" ".center(40)))
    print("||{}||".format("* : Multiplication".center(40)))
    print("||{}||".format("+ : Addition      ".center(40)))
    print("||{}||".format("- : Subtraction   ".center(40)))
    print("||{}||".format("/ : Division      ".center(40)))
    print("||{}||".format("% : Modulo        ".center(40)))
    op=input("||{}||=>".format(" ".center(40)))
    print("||{}||".format(line))
    b=int(input("||{}||=>".format("Enter the 2nd number ".center(40))))
    print("||{}||".format(line))
    return a,b,op
def outputdesign(w,r):
    line="----------------------------------------".center(40)
    print("||{}||".format(" ".center(40)))
    print("||{}||".format(w.center(40)))
    print("||{}||".format(r.center(40)))
    print("||{}||".format(line.center(40)))
def sum(a,b):
  w="Addition"
  r="%d+%d=%d"%(a,b,a+b)
  outputdesign(w,r)
def sub(a,b):
  w="Subtraction"
  r="%d-%d=%d"%(a,b,a-b)
  outputdesign(w,r)
def mul(a,b):
  w="Multiplication"
  r="%d*%d=%d"%(a,b,a*b)
  outputdesign(w,r)
def div(a,b):
  w="Division"
  r="%d/%d=%d"%(a,b,a/b)
  outputdesign(w,r)
def mod(a,b):
  w="Modulo"
  r="{}%{}={}".format(a,b,a%b)
#   r="%d'/%'%d=%d"%(a,b,a%b)
  outputdesign(w,r)
s=design1() 
a,b,op=design2()       
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
    s=design1()
    if(s=="start"):
      a,b,op=design2()


