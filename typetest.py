import time
import random

def sentence():
    paragraphs = ["The sun slowly dipped below the horizon, painting the sky in shades of orange and pink.","She carefully placed the book back on the shelf, lost in thought.","A cool breeze rustled the leaves, filling the air with a crisp autumn scent."]
    num = random.randint(0,len(paragraphs)-1)
    return paragraphs[num]

print("-"*15+"Typing Test"+"-"*15)
randomsen = sentence()
print(f"Type : {randomsen}")
start = time.time()
userinput = input("     : ")
end = time.time()

# Calculation
etime = end - start
word=len(randomsen.split())
if etime==0:
    print("Invalid.")
    exit()
mintime = etime / 60

speed = word / mintime

print(f"Speed: {speed:.2f}wpm")