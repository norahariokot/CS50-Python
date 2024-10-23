def main():
    plate = input("Plate: ")
    if is_vailid(plate):
        print("Valid")
    else:
        print("Invalid")    


def is_vailid(s):
    char_count = 0
    letter_count = 0
    not_letteror_digit = 0
    digits = []
    for i in s:
        char_count += 1
        if i.isalpha():
            letter_count += 1
        if not i.isalpha() and not i.isdigit():
            not_letteror_digit += 1  
        if i.isdigit():
            digits.append(i)  
    #print(char_count)   
    #print(digits)
    """
    if digits:
        print(digits[0])
        if digits[0] == "0":
            print("0 is the first digit")
    """        
    if len(digits) > 0:
        if (char_count >= 2 and char_count <= 6) and letter_count >= 2 and not_letteror_digit == 0 and s[0:2].isalpha() and digits[0] != "0" and not s[char_count - 1].isalpha():
            return True
    elif len(digits) == 0:
        if (char_count >= 2 and char_count <= 6) and letter_count >= 2 and not_letteror_digit == 0 and s[0:2].isalpha():
            return True
     
  


main()
              

        






