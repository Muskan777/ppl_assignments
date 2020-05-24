i = 0
n = input("Enter the number to be guessed\n")
while(1):
    guess = input("Enter your guessed input\n")
    if(guess == n):
        print("your answer is correct\n")
        break
    elif(guess > n):
        print("your guess is greater than the correct number\n")
        continue
    else:
        print("Your guess is smaller than the correct number\n")
        continue

