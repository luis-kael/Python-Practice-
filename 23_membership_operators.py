word = "APPLE"

letter = input("Guess a letter in the serect word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found ")
    

students = {"Spongbob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student not in students:
   print(f"{student} was not found")
else:
    print(f"{student} is a student")
    
    
