import random
r=random.randint(1,10000)
guess = 0

while(True):
    guess += 1 
    imp=int(input("Enter your guess : "))
    if(r>imp):
        print("It's greater")
    elif(r<imp):
        print("It's Smaller")
    else:
        print("Correct guess") 
        break
    
print("You take "+ str(guess) + " chances to find number")