import random
num=random.randint(1,200)
print("Hello!! Welcome to Number guessing game..")
print("Enter your name here...")
name=input()
print(name+" Let's start number guessing game from(1-200)")
chances=0
print("You have 6 chances to guess right number")
while(chances<=6):
    choice=int(input("Enter a number to guess...."))
    if choice <num:
        print("Number is tooo low")
    if choice>num:
        print("Number is too high")
    if choice==num:
        print("congratsss!!!! your guess  is right")
        break
    chances+=1

