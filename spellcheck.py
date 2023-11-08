# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"
import math
import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")


    # text = input("dictionary or aliceWords ")
    # word = input("what word to search for ")
    # method = input("binary or linear search ")

    print("\nMAIN MENU")
    print("1: Spell Check a Word")
    print("2: Spell Check Alice In Wonderland")
    print("3: EXIT")

    # # Get Menu Selection from User

    selection = input("Enter Selection (1-3): ")


    # # Take Action Based on Menu Selection

    if selection == "1":
        spell_check_word(dictionary)
        main()
    elif selection == "2":
        spell_check_text(aliceWords,dictionary)
        main()
    elif selection == "3":
        print("\nEXIT")
   
       


def search(array,item,LorB):
    if LorB == "l":
        found = linearSearch(array,item)
        return found
    else:
        found = binarysearch(array,item)
        return found


def spell_check_text(words,dictionary):
    LorB = input("linear or binary (l/b)")
    words = [x.lower() for x in words]
    not_found = 0
    start_time = time.time()
    for word in words:
        test = search(dictionary,word,LorB)
        if test == -1:
            not_found +=1
    end_time = time.time()
    total = end_time - start_time
    print(f"Number of words NOT found in dictionary: {not_found}. ({total} seconds)")

def spell_check_word(dictionary):
    word = input("search for: ")
    LorB = input("linear or binary (l/b)")
    start_time = time.time()
    found = search(dictionary,word,LorB)
    end_time = time.time()
    total = end_time - start_time
    if found == -1:
        print(f"{word} not found in dictionary. ({total} seconds)")
    else:
        print(f"{dictionary[found]} is IN the dictionary at position {found}. ({total} seconds) ")


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


def binarysearch(anArray,item):
    i = 0
    lowerindex = 0
    upperindex = len(anArray)
    while lowerindex <= upperindex:
        index = math.floor((lowerindex + upperindex)/2)
        if anArray[index] < item:
            lowerindex = index +1
            i+=1
        elif  anArray[index] > item:
            upperindex = index -1
            i+=1
        else :
            # print ("program searched",i,"times")
            return index
    # print ("program searched",i,"times")
    return -1


def linearSearch(anArray,item):
    i = 0
    #check array
    while i < len(anArray) :
        if anArray[i] == item:
            # print ("program searched",i,"times")
            return i 
        # if not at i move to next spot
        elif anArray[i] != item:
            i+=1
            #if the next spot is out of the Array end function and return -1
            if i == len(anArray):
                # print ("program searched",i,"times")
                return -1
        
# Call main() to begin program
main()
