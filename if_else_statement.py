try:
    
    user_input = input("Enter a number: ")
    
    
    number = int(user_input)

    
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")

except ValueError:
    
    print("Invalid input. Please enter an integer.")
