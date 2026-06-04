a=input("type a nuber:")
b=input("type another:")
a=int(a)
b=int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero.")
