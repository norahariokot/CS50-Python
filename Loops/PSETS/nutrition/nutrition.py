#fruits = [] # to store values from the fruis csv file

fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plum": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
}
"""
# Open CSV file with fruits and calories and store them in file
with open("fruits.csv") as file:
    for line in file:
        fruit, calories = line.strip().split(",")
        fruit_dict = {}
        fruit_dict["fruit"] = fruit
        fruit_dict["calories"] = calories
        fruits.append(fruit_dict)
#print(fruits)  
"""

user_request = input("Item: ").lower()
for fruit in fruits:
    if user_request == fruit.lower():
        print(fruits[fruit])