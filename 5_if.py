age = input("Enter your age: ")

if age >= 100:
    print("You are now signed up!")
    
elif age >= 18:
    print("You haven't been born yet!")
    
elif age < 0:
    print("You are too old to sign up")
    
else:
    print("You must be 18+ to sign up")