##Leira Salene 1785752

words = input()
wordsList = words.split()
for i in range(len(wordsList)):
    print(wordsList[i], wordsList.count(wordsList[i]))