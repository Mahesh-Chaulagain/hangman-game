import random
import string

from mywords import words   #from mywords.py file import words

def get_valid_word(words):
    word=random.choice(words)   #randomly choses something form the list of words
    while '-' in word or ' 'in word:    #filter out words containing - and " " in between
        word=random.choice(words) 

    return word.upper() #convet word to uppercase

def draw_man(lives):
    man = [
        "   O   ",  # Head
        "  /|\\  ", 
        " / | \\ ", # Arms
        "   |   ",  # Body
        "  / \\  " ,  
        " /   \\  ",# Legs
    ]

    if lives == 0:
        return "\n".join(man)
    elif lives == 5:
        return "\n".join(man[:1])
    elif lives == 4:
        return "\n".join(man[:2])
    elif lives == 3:
        return "\n".join(man[:3])
    elif lives == 2:
        return "\n".join(man[:4])
    elif lives == 1:
        return "\n".join(man[:5])
    else:
        return "      \n      \n      \n      \n       \n      \n"

def hangman():
    word = get_valid_word(words)    
    word_letters = set(word)      #set removes duplicate words
    alphabet = set(string.ascii_uppercase)  #this line creates a set alphabet containing all uppercase letters of the English alphabet
    used_letters=set()  # what the user has guessed

    lives=6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
            print(f"you have{lives} lives left and you have used these letters:{' '.join(used_letters)}")

            #what current word is (i.e w-ord)
            word_list=[letter if letter in used_letters else '-' for letter in word]
            print(f"current word: {' '.join(word_list)}")

            user_letter=input('guess a letter:').upper()    #take letter as input and convert to uppercase

            if user_letter in alphabet - used_letters:  #checks if user guess is in alphabet but not in already used letters
                used_letters.add(user_letter)   
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print(draw_man(lives))

                else:
                    lives = lives - 1
                    print(draw_man(lives))
                print("letter is not in word")
            elif(user_letter in used_letters):
                print('you have already used that character. please try again.')

            else:
                print('invalid character. try again')

    if lives==0:
            print('you died,the word was',word)
    else:
            print('you guessed corred word',word)


def main():
    while True:
        answer = input("press enter to play (q to quit):")
        if answer == 'q':
            break
        hangman()

main()
