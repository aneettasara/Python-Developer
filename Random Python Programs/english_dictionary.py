# Implement English dictionary
# User can do the following:
#       - input words and its meaning
#       - update word meaning
#       - delete existing words and its meanings

import os
from colorama import Fore, Back, Style
import time
from console_progressbar import ProgressBar
import ast

def is_file_empty(file_path):               # Check if the file is empty
    if os.path.getsize(file_path) == 0:
        return True
    else:
        return False

def add_word(dict_dict):
    word = str(input("Enter Word: "))
    meaning = str(input("Enter Meaning: "))
    f = open("english_dictionary.txt","w")   # Overwrite to the Existing File
    dict_dict[word] = meaning                # Add the New Word to the Dictionary
    f.write(str(dict_dict))
    print(Fore.YELLOW+Back.BLACK+"-- Word and Its Meaning is added in the Dictionary --"+Style.RESET_ALL)
    f.close()

def search_word(dict_dict):
    find_word = str(input("Enter the Word to be searched: "))
    f = open("english_dictionary.txt", "r")  # Read from File
    data = f.read()
    if find_word in ast.literal_eval(data).keys():     # Search the Word in the Dictionary
        print(Fore.YELLOW+Back.BLACK+"-- Word and Its Meaning FOUND !! --"+Style.RESET_ALL)
        print(find_word + " :- " + ast.literal_eval(data)[find_word])
    else:
        print("-- Word NOT FOUND !! --")
    f.close()

def display_dictionary(dict_dict):
    print("-- My English Dictionary --")
    f = open("english_dictionary.txt", "r")  # Read from File
    data = f.read()
    print(Fore.YELLOW+Back.BLACK+"-------------------------")
    print("Word" + " :- " + "Meaning")
    print("-------------------------")
    for key,value in ast.literal_eval(data).items():   # Evaluate data as Python expression
        print(key+" :- "+value)              # Display the contents in the Dictionary
    print("-------------------------")
    print(Style.RESET_ALL)
    f.close()

def update_meaning(dict_dict):
    update_word = str(input("Enter the Word to be updated: "))
    new_meaning = str(input("Enter the new meaning to that word: "))
    updated_item = {}
    updated_item[update_word] = new_meaning
    f = open("english_dictionary.txt", "r+")  # Read from File and Write to File
    data = f.read()
    if update_word in ast.literal_eval(data).keys():
        dict_dict.update(updated_item)
        f.truncate(0)                         # Clear File content in the Dictionary
        f.seek(0)
        f.write(str(dict_dict))               # Update the contents in the Dictionary
        print(Fore.YELLOW+Back.BLACK+"-- Word and Its New Meaning is updated in the Dictionary --"+Style.RESET_ALL)
    else:
        print("-- Word NOT FOUND !! --")
    f.close()

def display_options():
    print("\nHi User! ")
    print(Fore.RED+Back.BLACK+"---- MENU ----")
    print("[1] Add a word.")
    print("[2] Find meaning.")
    print("[3] Display all.")
    print("[4] Update meaning.")
    print("[5] Save and Close.")

def assign(option,dict_dict):
    switcher = {                # Switch Case using dictionary
        1: add_word,
        2: search_word,
        3: display_dictionary,
        4: update_meaning
    }
    return switcher[option](dict_dict)

def execute_english_dictionary():
    display_options()
    print(Style.RESET_ALL)
    op = int(input("Enter Choice <1/2/3/4/5> : "))
    if op not in range(1, 6):
        print("WRONG INPUT! \nEnter the option again")
    else:
        dict_dict = {}
        if (not os.path.exists("english_dictionary.txt")):
            print("English Dictionary is DOES NOT EXIST !!")
            f = open("english_dictionary.txt", "w").close()  # Create a File
            print("CREATED English Dictionary !!")
            if op == 1:
                assign(op, dict_dict)
        else:
            if is_file_empty("english_dictionary.txt"):
                print("English Dictionary is EMPTY !!")
                if op == 1:
                    assign(op, dict_dict)
                    print("ENTERED the first word in English Dictionary !!")
            else:
                f = open("english_dictionary.txt", "r")     # Read from File
                data = f.read()
                dict_dict = ast.literal_eval(data)          # Store into Python Dictionary for storing Word and Its Meaning
                f.close()
                if op == 5:
                    print(Fore.YELLOW+Back.BLACK+"English Dictionary Saved Successfully!"+Style.RESET_ALL)
                    return
                else:
                    assign(op,dict_dict)
    execute_english_dictionary()

def load_dictionary():          # Progress Bars using console_progressbar package
    bar = ProgressBar(total=10,prefix='Loading..',suffix='Completed',length=10)
    for item in range(11):
        bar.print_progress_bar(item)
        time.sleep(0.08)

# MAIN PROGRAM

print(Fore.WHITE+Back.BLACK+"----------------------")   # Add Colour to Text using colorama package
print("  ENGLISH DICTIONARY  ")
print("----------------------")
print(Style.RESET_ALL)

load_dictionary()
execute_english_dictionary()