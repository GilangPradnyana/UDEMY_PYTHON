import threading
import time

def print_number():
  for i in range(5):
    print(f'number : {i}')

def print_letter():
  for letter in "abcde":
    print(f'Letter : {letter}')