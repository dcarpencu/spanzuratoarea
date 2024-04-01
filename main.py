## cazurile spanzuratorii

spanzurat0 = '''
-------
|   |
| 
| 
| 
| 
-----------
'''

spanzurat1 = '''
-------
|   |
|   0
| 
|  
| 
-----------
'''

spanzurat2 = '''
-------
|   |
|   0
|   |
|  
| 
-----------
'''

spanzurat3 = '''
-------
|   |
|   0
| / | 
|  
| 
-----------
'''

spanzurat4 = '''
-------
|   |
|   0
| / | \\
|  
| 
-----------
'''

spanzurat5 = '''
-------
|   |
|   0
| / | \\
|  /
| 
-----------
'''

spanzurat6 = '''
-------
|   |
|   0
| / | \\
|  / \\
| 
-----------
'''

## alegere spanzuratoare

def which_hanger(counter):
    match counter:
        case 1:
            print(spanzurat1)
        case 2:
            print(spanzurat2)
        case 3:
            print(spanzurat3)
        case 4:
            print(spanzurat4)
        case 5:
            print(spanzurat5)
        case 6:
            print(spanzurat6)
        case _:
            print(spanzurat0)


restart = 'yes'

score = 0

while restart == 'yes':

## contor greseli
    ct = 0

    word = input('Introduceti un cuvant: ')

    wordToList = []

    for i in word:
        wordToList.append(i)

    guessWord = []
    for i in wordToList:
        guessWord.append('_')

    print(guessWord)

    usedLetters = []

    while ct < 6:
        ok = 0
        guess = input('Enter a letter [A-B]:')

        usedLetters.append(guess)

        for index, letter in enumerate(wordToList):
            if letter == guess:
                ok = 1
                guessWord[index] = letter

        if ok == 0:
            ct += 1
        which_hanger(ct)
        print(f'Used letters: {usedLetters}')
        print(guessWord)

        if guessWord == wordToList:
            score += 1
            print('CONGRATS! WE HANG U TOMORROW!')
            print(f'The score is: {score}')
            restart = input('Do you want to continue??')
            break
