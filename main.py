words_ones = {
    1: "one", 2: "two", 3: "three", 
    4: "four", 5: "five", 6: "six", 
    7: "seven", 8: "eight", 9: "nine", 0: "zero"
}
main_blocks = {
    10: "ten", 2: "twen", 3: "thir", 
    4: "for", 5: "fif", 6: "six", 
    7: "seven", 8: "eigh", 9: "nine"
}

def create_ones(num: int):
    for word in words_ones:
        if word == int(num):
            return words_ones[word]
        
def create_tens(num):        
    tens, ones = [char for char in str(num)]
    print(f"tens: {tens}\nones: {ones}")
    word = {}
    for i in main_blocks:
        if i == int(tens) and i != 10:
            word["tens"] = f"{main_blocks[i]}ty"
            
    for j in words_ones:
        if int(ones) == 0:
            word["ones"] = ""
        elif j == int(ones):
            word["ones"] = f"{words_ones[j]}"
    if num in range(10, 20):
        if int(ones) == 1:
            return 'eleven'
        elif int(ones) == 0:
            return 'ten'
        elif int(ones) == 2:
            return 'twelve'
        for i in main_blocks:
            if i == int(ones) and i != 2:
                return f"{main_blocks[i]}teen"      
    
    if len(word) > 0: 
        return f"{word['tens']} {word['ones']}" 
    return 0

def create_hundreds(num):
    tens = str(num)[1:]
    hundred = str(num)[0]
    tens_word = create_tens(tens)
    hund_word = create_ones(hundred)
    return f"{hund_word} hundred and {tens_word}"

def create_thousands(num):
    thousands = str(num)[0]
    hund = str(num)[1:]
    thousand_word = create_ones(thousands)
    hund_word = create_hundreds(hund)
    return f"{thousand_word} thousand {hund_word}"

def create_tens_of_thousands(num):
    pass

def create_hundred_of_thousands(num):
    pass

def create_million(num):
    pass

def create_tens_of_millions(num):
    pass

def create_hundred_of_millions(num):
    pass

def create_billion(num):
    pass

def create_tens_of_billionss(num):
    pass

def create_hundred_of_billions(num):
    pass

def create_trillion(num):
    pass
        
def call():
    num = int(input("Enter the word: "))
    if len(str(num)) == 1:
        print(create_ones(num))
    elif len(str(num)) == 2:
        print(create_tens(num))
    elif len(str(num)) == 3:
        print(create_hundreds(num))
    elif len(str(num)) == 4:
        print(create_thousands(num))
    else:
        print("The term you entered is not supported yet")
        
call()