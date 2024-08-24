# programme to compute energy in joules
def user_mass():
    return int(input("m: "))

mass = None
while not type(mass) == int:
    try:
        mass = user_mass()
    except ValueError:
        print(f"That was not valid. Mass must be an integar ")
    
c = 300000000 ** 2
E = mass * c
print(f"E: {E}")