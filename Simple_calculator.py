
def Add(num1,num2):
    result = num1 + num2
    print (result)
def Subtract(num1,num2):
    result = num1 - num2
    print (result)
def Multiply(num1,num2):
    result = num1 * num2
    print (result)
def Divide(num1,num2):
    result = num1 / num2
    print (result)

print ("Welcome To Simple Calculator")
while True :
    print ("Please Select From the Following Choices: ")
    print ("""1. Add
2. Subtract
3. Multiplication
4. Division
5. Quit  """)
    choices = int(input("(1-5) Option: "))
    if choices ==1:
        int1=int(input("Enter The First Number:"))
        int2=int(input("Enter The Second Number:"))
        Add(int1, int2)
    elif choices ==2:
        int1=int(input("Enter The First Number:"))
        int2=int(input("Enter The Second Number:"))
        Subtract(int1, int2)
    elif choices ==3:
        int1=int(input("Enter The First Number:"))
        int2=int(input("Enter The Second Number:"))
        Multiply(int1, int2)
    elif choices ==4:
        int1=int(input("Enter The First Number:"))
        int2=int(input("Enter The Second Number:"))
        Divide(int1, int2)
    elif choices ==5:
        print ("Goodbye")
    
