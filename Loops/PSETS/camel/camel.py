# programme to convert users's camelcase input to snakecase
variable_name = input("camelCase: ")

"""
words = []
indexes = []
for char in variable_name:
    if len(indexes) == 0:
        indexes.append(0)
    else:
        if char.isupper() and char!= variable_name[0]:
            index = variable_name.index(char)
            print(index)
            indexes.append(index)
        print(indexes)   
indexes2 = copy.deepcopy(indexes) # requires import copy
print(indexes2)

for index in indexes:
    print(f"indexes2 is now {indexes2}")
    if len(indexes2) >= 2:
        i = indexes2[0]
        print(f"i is {i}")
        j = indexes2[1]
        print(f"j is {j}")
        word = variable_name[i:j]  
        words.append(word)
        indexes2.pop(0) 
    elif len(indexes2) == 1:
        i = indexes2[0]
        print("Indexes 2 is now 1")
        word = variable_name[i:]    
        words.append(word)

print(words)
# This is previous odd
"""
# Find index of the first character and characters that are upper case and store in list
words = []
last_index = 0

if variable_name.islower():
    words.append(variable_name)
else:
    for i, char in enumerate(variable_name):
        if i != 0 and char.isupper():
            words.append(variable_name[last_index:i])
            last_index = i
 
    # Add the last part of the string
    words.append(variable_name[last_index:])
#print(words)        

new = ""
if words:
    new_words = []
    for i, word in enumerate(words):
        if i != (len(words) - 1):
            new_word = word.lower() + "_"  
        else:
            new_word = word.lower()
        new_words.append(new_word) 
    #print(new_words)    

    # Append list of new words to string
    """
    new = ""
    for word in new_words:
        new = new + word
    """    

    new = ''.join(new_words)    

print(f"snake_cake: {new}")  


       