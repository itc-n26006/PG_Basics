try:
    a=input("type a number:")
    b=input("tupe another:")
    a=int(a)
    b=int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")
