def count(word, latter):
    counting = 0
    for i in word:
        if i == latter:
            counting += 1
    print("The count: ", counting)
    




wordi = input('Enter the word: ')
latteri = input ('Enter the latter: ')

count(wordi , latteri)


