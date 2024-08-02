def convert(s):
    if ":)" in s:
        s = s.replace(":)", "🙂")
        return s
    elif ":(" in s:
        s = s.replace(":(", "🙁") 
        return s
    else:
        return s    

def main():
    user_input = input("")
    updated_text = convert(user_input)
    print(f"{updated_text}")

main()



        
