print("\t\tGuess the number")
print("\t\tType q for exit")
import random
a = random.randint(1,9)
count = 0
while True:
    b = input("Choose a number beetween 1 and 9\n").lower()
    if b.isdigit() and int(b) > 0 and int(b) < 10:
        b = int(b)
        count += 1
        if b < a:
            print("Your number is smaller than the correct number")
        elif b > a:
            print("Your number is bigger than the correct number")
        elif b == a:
            print("You guess the correct number after",count,"tries")
            print("Have a nice day")
            break
    elif b == "q":
        print("Have a nice day")
        break
    else:
        print("You must choose a number beetween 1 and 9")
