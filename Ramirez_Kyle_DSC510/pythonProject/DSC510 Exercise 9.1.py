# Week 9
# 9.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 15-May-2021
# Assignment is to create a program that will:
# Open the file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
# Nicely print the output, in this case from high to low frequency.
# Create a new function called process_fie. This function will perform the same operations as
# pretty_print from week 8 however it will print to a file instead of to the screen.

import os
wordList = list()
wordDic = {}


# function that processes the each line of the file and appends to the word list
def processLine(gba_file):
    for line in gba_file:
        for word in line.split():
            wordList.append(word)
    return wordList


# calculates how many of each word there is within the word list
def addWord():
    for word in wordList:
        if word in wordDic:
            wordDic[word] += 1
        else:
            wordDic[word] = 1
    return wordDic


# prints the number of words in the file, gives it a header, and prints the dictionary keys and values
def processFile(wordDic):
    filepath = 'C:/Users/Kyle/Documents/GitHub/KR/Ramirez_Kyle_DSC510/pythonProject/'
    newFile = str(input('What would you like the new file name to be?'))
    completePath = filepath+newFile+'.txt'

    if os.path.isfile(newFile):  # check if file exists
        print('File Exists')
        if os.path.isdir(newFile):  # check if file path exists
            print('Directory Exists')
            if os.path.exists(completePath):  # check if complete path exists
                print('Complete path exists')
                print('Complete Path', completePath)

    with open(completePath, 'w') as fileHandle:  # open file for writing
        fileHandle.write('Number of words in the file is: ' + str(len(wordList)))
        fileHandle.write('\nWord | count')
        for key, value in wordDic.items():
            fileHandle.write('\n' + str(key) + '   ' + str(value))
        fileHandle.close()


# main will call each function in the proper order in order to print the number of words in the file
# a header, and the keys within the dictionary along with the number of times those words repeat
def main():
    gba_file = open('gettysburg.txt', 'r')

    processLine(gba_file)
    wordDic = addWord()
    processFile(wordDic)


if __name__ == "__main__":
    main()
