# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import math
import time # needed to find the time the function used

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Main Menu
    loop = True 
    while loop: 
        selection = getMenuSelection()

        if selection == "1" or selection == "spell check a word (linear search)":
            wordlinear(dictionary)
        elif selection == "2" or selection == "spell check a word (binary search)":
            wordbinary(dictionary)
        elif selection == "3" or selection == "spell check alice in wonderland (linear search)":
            alicelinear(aliceWords, dictionary)
        elif selection == "4" or selection == "spell check alice in wonderland (binary search)":
            alicebinary(aliceWords, dictionary)
        elif selection == "5" or selection == "exit":
            exit()
        else: 
            print("Please choose an option. ")
# end main()

# MENU FUNCTIONS
def getMenuSelection():
    # Menu Options
    print(f"\n********MAIN MENU********")
    print("1. Spell Check a Word (Linear Search)")
    print("2. Spell Check a Word (Binary Search)")
    print("3. Spell Check Alice In Wonderland (Linear Search)")
    print("4. Spell Check Alice In Wonderland (Binary Search)")
    print("5. Exit")
    return input("\nChoose an option please: ").lower()

def wordlinear(dictionary):
    word = input("Please enter a word: ").lower()
    print("\nLinear Search Starting...")
    startTime = time.time()
    result = linearSearch(dictionary, word)
    endTime = time.time()
    if result == -1:
        print(f"{word} is NOT IN the dictionary. ({endTime-startTime}) seconds")
    else:
        print(f"{word} is IN the dictionary at position {result}. ({endTime-startTime}) seconds")


def wordbinary(dictionary):
    word = input("Please enter a word: ").lower()
    print("\nBinary Search Starting...")
    startTime = time.time()
    result = binarySearch(dictionary, word)
    endTime = time.time()
    if result == -1:
        print(f"{word} is NOT IN the dictionary. ({endTime-startTime}) seconds")
    else:
        print(f"{word} is IN the dictionary at position {result}. ({endTime-startTime}) seconds")

def alicelinear(aliceWords, dictionary):
    wordcount = 0
    print("Linear Searching Starting ...")
    startTime = time.time()
    for alword in aliceWords:
        results = linearSearch(dictionary, alword)
        if results != -1:
            wordcount += 1
    endTime = time.time()
    print(f"Number of words not found in dictionary: {wordcount} ({endTime-startTime}) seconds")



def alicebinary(aliceWords, dictionary):
    wordcount = 0
    print("Binary Searching Starting ...")
    startTime = time.time()
    for alword in aliceWords:
        results = binarySearch(dictionary, alword)
        if results != -1:
            wordcount += 1
    endTime = time.time()
    print(f"Number of words not found in dictionary: {wordcount} ({endTime-startTime}) seconds")

def exit():
    loop = False
    print("\nBye!")


# HELPER FUNCTIONS
# Binary and Linear Search Functions
def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

def binarySearch(anArray,item):
    li = 0
    ui = len(anArray)-1
 
    while li < ui or li == ui:
        mi = math.floor((li+ui)/2)
        if item == anArray[mi]:
            return mi
        elif item < anArray[mi]:
            ui = mi - 1
        elif item > anArray[mi]:
            li = mi + 1
    return -1

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()






# Call main() to begin program
main()