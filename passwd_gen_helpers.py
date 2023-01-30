"""
This software is used to generate a very simple password with simple words
- Makes saying the password over the phone easier
- then spelling everything out
"""

import random as r

# Words used to randomize the passwords


#func to randomly join two words from list
def generate_words():
    words = [
              "circle", "triangle", "square", "rectangle", "star" , # Shapes
              "green", "blue", "red", "yellow", "purple", "orange", # Colors
              "dog", "cat", "fish", "bird"                          # Animals
            ]
    chosen_words = r.sample(words, 2)

    return(chosen_words)


#func to generate two digits 
def generate_num():
    chosen_number = r.randint(10, 99)
    
    return(chosen_number)

def pick_random_symbol():
    symbols=["!", "@", "#", "$", "%"]
    chosen_symbol=r.choice(symbols)

    return symbol


#func to print password
def print_password(words, numbers):
    return("print_password() End")