import random

n = random.randint(1,20)
a = -1
guess = 0

while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower Number please")
        guess += 1
    elif(a < n):
        print("Higher Number please")
        guess += 1
    
print(f"You guess the correct number {n} in {guess} attempts")