num1,num2=list(map(int,input("enter two number").split()))
op=input("enter choice \n 1. add\n2. sub\n 3.mul.:\n")
if op=='1':
    print(num1+num2)
elif op=='2':
    print(num1-num2)
elif op=='3':
    print(num1*num2)
else:
    print("you have input wrong value")
