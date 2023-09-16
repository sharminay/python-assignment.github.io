import random

low = 1
high = 50
correct_answer = random.randint(low, high)

count = 0
for x in range(5,0,-1):
  guess = int(input("\nEnter a number between 1 to 50 \n"))
  print("(chances left : ",x-1,")")
  if (guess > 50):
    print("Enter the Input less than 51 (1-50)")
    continue

  elif (guess <= 50 and guess != 0):
      if (guess < correct_answer ):
        print("Correct answer is greater!")
      elif (guess > correct_answer ):
        print("Correct answer is smaller!")
      elif (guess == correct_answer ):
        print("\nYou Win\n")
        break
  elif (guess == 0):
    print("Please enter the Input (1-50)")
    continue

else:
  print("\nYou lose!\n")

