x=input("Enter the first number: ")
y=input("Enter the second number: ")

try:
     first=int(x)
     second=int(y)
     print(first / second)
    
except ValueError:
    print('Please  enter valid numbers')
except ZeroDivisionError:
     print('The second number can not be zero')
