#oops -> Exception handling, Threds , multiprcessing,
#LLD , DBMS , Fast API -> OOPS
#syntex erros
#logical erros


try:
    a = int(input("Enter value a:"))
    b = int(input("Enter value b:"))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("we can't divide with zero")

except ValueError:
    print("The values shoud be in base 10:")

finally:
    print("process completed")
