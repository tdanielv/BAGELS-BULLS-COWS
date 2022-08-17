import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('BULLS and COWS is  a deductive logic game.')
    print('when i say:        it means: \n')
    print('BULL               one digit is correct and in the right position \n')
    print('COW                one digit is correct but in the wrong position\n')
    print('For example:if secret number wa 123 and your guess was 214 the clues would be BULL COW\n')

    while True:
        secretNum = getSecretNum()
        print('I have throught up a number')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))
        print('Do u wanna play again? yes/no')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing')

def getSecretNum():
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    random.shuffle(numbers)
    print(numbers)
    secretNum = []
    for i in range(NUM_DIGITS):
        secretNum.append(numbers[i])
    return ''.join(secretNum)

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(3):
        if guess[i] == secretNum[i]:
            clues.append('BULL')
        elif guess[i] in secretNum:
            clues.append('COW')
    if len(clues) == 0:
        return '^%$@!'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
