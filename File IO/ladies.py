ladies = []
with open("ladies.csv") as file:
    for line in file:
        name, address = line.strip().split(",")
        lady = {}
        lady["name"] = name
        lady["address"] = address
        ladies.append(lady)

for lady in ladies:
    print(f"{lady['name']} lives in {lady['address']}")        