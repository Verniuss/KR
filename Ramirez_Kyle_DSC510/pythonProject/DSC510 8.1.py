# Week 8
# 8.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 9-May-2021
# Assignment is to create a program that will:
# Open the file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
# Nicely print the output, in this case from high to low frequency.

wordList = list()
wordDic = {}
gba_file = open('gettysburg.txt', 'r')

for line in gba_file:
    # print(line.split())
    for word in line.split():
        # print(word)
        wordList.append(word)

for word in wordList:
    # print(word)
    if word in wordDic:
        wordDic[word] += 1
    else:
        wordDic[word] = 1

print("Number of words in the file is: ", len(wordList))
print("Word", "Count")
for key, value in wordDic.items():
    print(key, value)
