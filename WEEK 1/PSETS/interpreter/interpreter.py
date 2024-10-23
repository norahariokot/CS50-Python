operation = input("Expression: ").split(" ")

x = int (operation[0])
y = operation[1]
z = int (operation[2])

if y == "+":
    result = float( x + z)
elif y == '-':
    result = float( x - z)  
elif y == '*':
    result = float( x * z) 
elif y == "/":
    result = float( x / z)

print(f"{result}")

