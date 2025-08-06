import random 

secret_number = random.randint(1 , 100)

attempt = 0 
print("welcome to the number guessing game ")
print ( " i have selected  a number between 1 and 100 ")
print(" can you guess it ")

while True:
    guess = input(" enter your guess number ")
    
    if not guess.isdigit():
        print("please enter the valid number")
        continue 
    
    guess = int(guess)
    attempt += 1 
    
    if guess < secret_number :
        print ( " the number is too low ")
    elif guess > secret_number :
        print("too high number try again")
    else : 
        print(f"✅ Correct! You guessed in {attempt} attempts.")
        break
    
        
    

