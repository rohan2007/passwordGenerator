from random import randint

def ArrayConvert(providedArray):
    string = ""
    for i in range(len(providedArray)):
        string += providedArray[i]
    return string

while True:
    generatedString = []
    letterString = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    SymbolString = ['!','@','#','$','%','^','&','*','(',')','-','+','{','}','|','[',']',';',':','"',"'",'<','>',',','.','/','?']
    providedComplexity = int(input("How much letters : 1 -----> 15 , 2 -----> 25 , 3 -----> 50: "))

    if providedComplexity == 1:
        i = 1
        while i <= 5:
            randomNumber = randint(1,9)
            generatedString.append(f"{str(randomNumber)}")
            i = i + 1

        j = 1
        while j <= 5:
            randomCharacter = randint(1,25)
            generatedString.append(letterString[randomCharacter])
            j = j + 1

        k = 1
        while k <= 5:
            randomSymbol = randint(1,26)
            generatedString.append(SymbolString[randomSymbol])
            k = k + 1

        print(f"The generated password is -----> {ArrayConvert(generatedString)}")

        tryAgain = int(input("Do you want to have this or you want to try again: 1 -----> yes this is good, 2 -----> no try again: "))
        if tryAgain == 1:
            print("Okay, have fun using this tool again")
            break
        elif tryAgain == 2:
            continue
        else:
            print("I can not understand that i will take this as you are not satisfied with the password so we will try again creating new one")
            continue