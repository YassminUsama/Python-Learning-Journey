num1=float(input('Enter first num:'))
opr=input('choose your operator(+,-,*,/,%):')
num2=float(input('Enter second num:'))
if opr== "+":
    print(num1,"+",num2,'=',(num1+num2))
elif opr== "-":
    print(num1,"-", num2,'=',(num1-num2))
elif opr== "*":
    print(num1,"*",num2,'=',(num1*num2))
elif opr== "/":
      if(num2==0):
          print("invalid value")
      else:
          print(num1,"/",num2,'=',(num1/num2))
elif opr == "%":
    if num2 == 0: 
        print("invalid value")
    else:
        print(num1, "%", num2, "=", (num1 % num2))
else:
    print("can't find operator")
