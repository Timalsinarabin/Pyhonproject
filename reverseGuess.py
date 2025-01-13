import random
def comp(low,high):
    return random.randint(low,high)

l=0
print("Think of a number")
h=int(input("Enter range of number from 0 to "))
user=''

while user!='c':
    if h<l:
        print("You are lying")
        break
    guess = comp(l,h)
    print(f'Your guess is {guess}.')
    user=input("If correct press 'c'. If computer guess is higher press 'h'. If computer guess is low press 'l': ").lower()
    if user=='h':
        h=guess-1
    elif user=='l':
        l=guess+1
    elif user=='c':
        print(f"Then {guess} is the number you've been thinking.")
    else:
        print("Invalid term used!")
print("Game Over")