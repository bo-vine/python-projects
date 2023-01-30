"""
This software is used to generate a very simple password with modern criterias for a strong password
- Makes saying the password over the phone easier
- then spelling everything out
"""

import random as r

class PasswordGenerate(str):

    def __init__(self) -> None:
        super().__init__()

    #func to randomly join two words from list of available words
    @staticmethod
    def generate_words() -> str:
        words = [
                "circle", "triangle", "square", "rectangle", "star" , # Shapes
                "green", "blue", "red", "yellow", "purple", "orange", # Colors
                "dog", "cat", "fish", "bird"                          # Animals
                ]
        chosen_words = r.sample(words, 2)

        return(chosen_words)


    #func to generate two digits
    @staticmethod
    def generate_num() -> int:
        chosen_number = r.randint(10, 99)
        
        return(chosen_number)

    @staticmethod
    def pick_random_symbol() -> str:
        symbols=["!", "@", "#", "$", "%"]
        chosen_symbol=r.choice(symbols)

        return symbol


    #func to print password
    @staticmethod
    def print_password(words: str, numbers: str) -> str:
        return("print_password() End")