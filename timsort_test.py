import string
from runtime_utils import track_time
import random
CONSTANT = 10**8
letter_arr =  random.choices(string.printable, k=CONSTANT)
number_arr = list(range(CONSTANT))
random.shuffle(number_arr)

@track_time
def sort_letters(letter_arr):
    letter_arr.sort()
    return letter_arr

@track_time
def sort_numbers(number_arr):
    number_arr.sort()
    return number_arr

sort_letters(letter_arr)
sort_numbers(number_arr)
