try:
    x = int(input("x: "))
except ValueError:
    print("x should be an integar") 
else:
    print(f"x is {x}")      