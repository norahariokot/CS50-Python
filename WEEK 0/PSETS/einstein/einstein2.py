while True:
    try:
        mass = int(input("m: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

c = 300000000 ** 2
E = mass * c
print(f"E: {E}")