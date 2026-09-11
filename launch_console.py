name = input("What's your name? ")
print(f"Welcome to my Launch Console, {name}!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Exit")
    choice = input("Pick 1-3: ")
    if choice == "1":
        print("I'm a nerd")
    elif choice == "2":
        print("My goal: git gud")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, or 3.")