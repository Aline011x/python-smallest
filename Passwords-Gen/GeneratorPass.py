import random
import sys


save_stdout = sys.stdout

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()/&%$#!¡¿?';:-_+* "

upper, lower, nums, syms = True, True, True, True 

all = ""

if upper: 
    all +=uppercase_letters
if lower: 
    all +=lowercase_letters
if nums: 
    all +=digits
if syms: 
    all +=symbols
    
length = 20
amount = 20

with open('pass-out', 'w') as file: 
    sys.stdout = file 
    
    for x in range(amount): 
        password = "".join(random.sample(all, length))
        print(password)
    
    sys.stdout = save_stdout
