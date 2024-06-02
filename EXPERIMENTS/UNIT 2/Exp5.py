x = input("Enter first no.:")
y = input("Enter second no.:")

try:
    a =int(x)
    b =int(y)
    z = a/b
    print(z)
except ZeroDivisionError:
    print("Exception is handled.")
except ValueError:
    print("Error handled.")