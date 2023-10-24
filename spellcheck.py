# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"
import math
import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")


    text = input("dictionary or aliceWords ")
    word = input("what word to search for ")
    method = input("binary or linear search ")

    if method == "binary":
        print (binarysearch(text,word))
    else:
         print (linearSearch(text,word))
#     # Print first 50 values of each list to verify contents
#     print(dictionary[0:50])
#     print(aliceWords[0:50])
# # end main()


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
            print ("program searched",i,"times")
            return index
    print ("program searched",i,"times")
    return -1


def linearSearch(anArray,item):
    i = 0
    #check array
    while i < len(anArray) :
        if anArray[i] == item:
            print ("program searched",i,"times")
            return i 
        # if not at i move to next spot
        elif anArray[i] != item:
            i+=1
            #if the next spot is out of the Array end function and return -1
            if i == len(anArray):
                print ("program searched",i,"times")
                return -1
        
# Call main() to begin program
main()
