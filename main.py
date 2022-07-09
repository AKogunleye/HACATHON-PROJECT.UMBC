# create an empty list for the and number of fail time
Word = "Bubbles"
# setting the number of errors .
Error_time = 3
#create an emty list called {guesses}
guesses = []
# lets have a boolen .
finished = False
# after we going to create our while loop
while not finished:
  # using an if statement to found out if this letters are found in the store varriable 
  for letter in Word:
    # using an if statement to found out if this letters are found in the store varriable
    if letter.lower()in guesses: 
      # Display the letter 
        print(letter,end="")
    else: 
        print("_",end="")
  print("")
  # getting input from the user and allowed errors.
  guess = input(f"Timeof error left {Error_time},Next Guess:")
  guesses.append(guess.lower())
  # printing the letter cos we actually asking for lower case : if guess is not in lower 
  if guess.lower() not in Word.lower():
# allows errors to be equall = 1 and if allow errors = 0 we going to break out of the loop.
     Error_time -=1
     if Error_time == 0:
        break
# asume that we already found the word untill proven otherwise.
finished = True
for letter in Word:
# check to found the secretword lower 
  if letter.lower() not in guesses:
      finished = False
# At the end , either we broken out of the loop or we stop loop
if finished:
  print(f"you found the secretword{Word},")
  # To display if we brooken out of it otherwise
else:
  print(f" you won. {Word}")
