#homework 8
#Problem 1
#input from user
firstName = input("Enter your first name here: ")
middleName = input("Enter your middle name here: ")
lastName = input("Enter your last name here: ")

#get the first characters for each inital
firstInital=(firstName[:1])
middleInital=(middleName[:1])
lastInitial=(lastName[:1])

print("your initals are", firstInital, middleInital, lastInitial)

#Problem 2
#user input
nums=str(input("Enter numbers with nothing separating them: "))
#create total for counting
total = 0
#get all of the digits separated
for ch in nums:
#convert to integers and add up each string to a total
    total+=int(ch)
#print the total
print(total)

#Problem 5
#Have user enter phone number
phoneNumber=input("Enter a 10 character telephone number: ")
phoneNumber2= ""
    #get each number separate and assigned a number
for ch in phoneNumber:
    if ch in ("abc"):
        ch =='2'
    if ch in ("def"):
        ch =='3'
    if ch in ("ghi"):
        ch =='4'
    if ch in ("jkl"):
        ch =='5'
    if ch in ("mno"):
        ch =='6'
    if ch in ("pqrs"):
        ch =='7'
    if ch in ("tuv"):
        ch =='8'
    if ch in ("wxyz"):
        ch =='9'
    phoneNumber2+=ch
        #add new variable to phone number
print(phoneNumber2)


#Problem 9
#Have user enter string
stringEnter = input("Enter a string: ")
totalVowels=0
totalConsonants=0
for ch in stringEnter:
    #gets rid of spaces
    if ch.isalpha():
        #calculates amount of vowels
        if ch == "a" or ch == "e" or ch=="i" or ch== "o" or ch== "u":
            totalVowels+=1
        else:
            #everything else is consonnant
            totalConsonants+=1

print(totalVowels, "vowels")
print(totalConsonants, "consonants")
#Problem 11
counter = 0
string = " "
sentence= input("Input a sentence in which all words are run together, but the first character of each word is upper case: ")
for ch in sentence:
    if ch.isupper() and counter > 0:
        #add space
        string+=" "
        string+=ch.lower()
    else:
        string+=ch
    counter+=1
print(string)
        
        