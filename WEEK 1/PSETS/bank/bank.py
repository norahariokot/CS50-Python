greeting = input("Greeting: ").lower().strip().split()

if greeting[0] == "hello":
    print("$0")
elif greeting[0][0] == "h" and greeting[0] != "hello":
    print("$20")
else:
    print("$100")      