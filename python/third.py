secret_number=10
guess_limit=3
guess_count=0
print("you can guess the number between 0 to 20 and you have only three chances")
while guess_count < guess_limit:
    guess=int(input("guess the number game begins :"))
    guess_count += 1
    if(guess==secret_number):
        print("you won the game")
        break
else:
    print("sorry! you failed")
  

        