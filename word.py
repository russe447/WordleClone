import random
import time
from termcolor import colored

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
    setup()
    
    
def play(word): 
    time.sleep(0.2)
    guesses_left = 5
    length = len(word)
    print(word)
    ### This causes an error marking incorrect letters as correct since 
    ### it bases the color on position of the guess
    color_arr = ['' for i in range(length)]
    w = ""
    for i in range(length):
        w = w + "_"
    solved = False
    letters = ["A","B","C","D",'E',"F","G","H","I","J","K","L",
               "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    while guesses_left and not solved:
        print(color.BOLD + str(guesses_left) + ' guesses left' + color.END)
        print(color.UNDERLINE + 'Your Letters' + color.END)
        print(*letters)
        print("Guess:", end =" ")
        for i in range(length):
            print(color_arr[i] + w[i].upper() + color.END, end=" ")
        print() 
        color_arr = ['' for i in range(length)]
        valid_input = False
        inp =''
        while not valid_input:
            inp = str(input(color.BOLD + 'Guess the word\n' + color.END))
            if length == len(inp):
                valid_input = True
            else:
                print(color.BOLD + 'Please enter ' + str(length) + ' characters')
        # Check if the guess matches the letter or if it exists in the word
        w = inp
        w = w.upper()
        time.sleep(0.1)
        if w == word.upper():
            print(color.BOLD + 'Congratulations! Your guess of ' + color.GREEN + 
                  str(w) + color.END + ' was correct!')
            print()
            time.sleep(0.8)
            solved = True
        else:
            for i in range(length):
                if w[i].upper() in word.upper():
                    if w[i].upper() == word[i].upper():
                        color_arr[i] = color.GREEN
                    else: 
                        color_arr[i] = color.YELLOW
                # if letter not in word remove from letters
                else:
                    if w[i].upper() in letters:
                        letters.remove(w[i].upper())

        
        guesses_left = guesses_left - 1
    if not solved:
        print('The word was: ' + color.PURPLE + word.upper() + color.END)
        time.sleep(0.5)
        print(color.BOLD + 'Better Luck Next Time!' + color.END)
        print()
        time.sleep(0.7)
        

def setup():
    game_active = True
    words_4 = []
    words_5 = []
    words_6 = []
    words_7 = []
    words_8 = []
    words_9 = []
    with open('wordlist.txt', 'r') as l:
        for word in l:
            new_word = word.strip()
            length = len(new_word)
            match length:
                case 4:
                    words_4.append(new_word)
                case 5:
                    words_5.append(new_word)
                case 6:
                    words_6.append(new_word)
                case 7:
                    words_7.append(new_word)
                case 8:
                    words_8.append(new_word)
                case 9:
                    words_9.append(new_word)
    
    
    while game_active:
        time.sleep(0.3)
        print(color.BOLD + 'Welcome to Wordle!' + color.END)
        time.sleep(0.3)
        print()
        print(color.UNDERLINE + color.BOLD + 'What would you like to do?' + color.END)
        #print('--------------------------')
        inp = input('|' + color.CYAN + 'PLAY' + color.END + '|' + color.PURPLE + 'EXIT' + color.END + '|\n')
        
        if inp == 'exit' or inp == 'EXIT':
            time.sleep(0.1)
            print(color.BLUE + 'Thank you for playing!' + color.END)
            time.sleep(0.3)
            game_active = False
        else:
            time.sleep(0.2)
            i = input('Choose Difficulty (4,5,6,7,8,9)\n')
         
            if i == '4':
                play(random.choice(words_4))
            elif i == '5':
                play(random.choice(words_5))
            elif i == '6':
                play(random.choice(words_6))
            elif i == '7':
                play(random.choice(words_7))
            elif i == '8':
                play(random.choice(words_8))
            elif i == '9':
                play(random.choice(words_9))
   
            
            

        

if __name__ == "__main__":
    main()