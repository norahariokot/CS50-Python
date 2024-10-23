#name = input("Name: ")

# To open and write to a file
#with open("names.txt", "a") as file:
    #file.write(f"{name}\n") 

# Reading from a file
with open("names.txt", "r") as file2:
    for line in file2:
        print(f"hello {line.rstrip()}")    
