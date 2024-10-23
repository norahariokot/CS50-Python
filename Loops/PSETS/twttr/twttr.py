# Return a string without vowels from a users input
text = input("Input: ")

vowels = ['a','e','i', 'o', 'u']

# Option 1, use a list of vowels, check for non vowels in the string and add them to list and convert the list to a string
new_word = []
for i in text:
    char = i.lower()
    if char not in vowels:
        new_word.append(i)

word = ''.join(new_word)
print(word) 

# Option 2: use a set of vowels, check for non vowels and keep appending them to the new string
vowels_set = {'a','e','i', 'o', 'u'}

new_text = ""
for a in text:
    char = a.lower()
    if char not in vowels_set:
        new_text = new_text + char

print(new_text)        
        
    

         