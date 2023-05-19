#Jaqueline Chavez
#IveGotYourNumber Ver 1
#Date: 10/30/2022

#Prompt will ask the user to input the number by restricting it to using all CAPs to get the accurate phone number
userInput = input("Enter the phone number with the letters in all CAPS:")
#The empty string will be used to display the phone number after using the conditons
phoneNumber = ""

#This is broken down by each number on the phone key pad with the corresponding letters
for char in userInput:
    if(char == "A" or char == "B" or char == "C"):
        phoneNumber += "2"
    elif(char == "D" or char == "E" or char == "F"):
        phoneNumber += "3"
    elif(char == "G" or char == "H" or char == "I"):
        phoneNumber += "4"
    elif(char == "J" or char == "K" or char == "L"):
        phoneNumber += "5"
    elif(char == "M" or char == "N" or char == "O"):
        phoneNumber += "6"
    elif(char == "P" or char == "Q" or char == "R" or char == "S"):
        phoneNumber += "7"
    elif(char == "T" or char == "U" or char == "V"):
        phoneNumber += "8"
    elif(char == "W" or char == "X" or char == "Y" or char == "Z"):
        phoneNumber += "9"
    else:
        phoneNumber += char
#This will display the new phone number after using the user's input
print(phoneNumber)