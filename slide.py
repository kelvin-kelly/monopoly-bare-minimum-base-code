import time

def typewriter_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def slide():
    typewriter_effect("Welcome to the Ultimate Choice Game!")
    typewriter_effect("You have two mysterious doors in front of you:")
    
    
slide()

