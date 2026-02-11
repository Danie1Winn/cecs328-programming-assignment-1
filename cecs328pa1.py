seed = 12345 # Declare a global "seed" variable for the random number generator

animals = ["bear", "chicken", "lion", "tiger", "ostrich"] # List of available animals to confine user input

def animal_palindrome(animals):
    """
    Flips the list of animals, checks if the flipped list is the same.
    returns: True if the list is palindromic, false otherwise
    """
    return animals == animals[::-1]

def random_animals(length):
    """
    Creates a list of random animals using the specified length
    """
    global seed

    random_animal_list = []
    for i in range(length):
        # LCG algorithm (Xn+1 = (a Xn + c) mod m), which generates a pseudo-random number
        seed = (seed * 1103515245 + 12345) & 0x7fffffff # Updates the seed with the LCG algorithm, so the next call (if looped) will produce another random list
        random_animal_list.append(animals[seed % len(animals)])

    return random_animal_list

if __name__ == "__main__":
    """
    Main function that provides a user menu. 
    Has options for manual list entry, random list generator, and quit.
    """
    while True:
        print("1. Generate a random list of animals")
        print("2. Manually enter a list of animals")
        print("3. Quit")
        choice = input("\nChoose an option (1 - 3): ")

        # Random list generator
        if choice == "1":
            # Loop to validate user inputs, ensuring it is a positive integer for both
            while True:
                try:
                    num_lists = int(input("\nHow many lists should be generated?: "))
                    list_length = int(input("Length of list(s)?: "))
                    if num_lists > 0 and list_length > 0:
                        break
                    print("Please enter a positive integer.")
                except ValueError:
                    print("Please enter an integer.")

            all_lists = [] # Creates an empty list to store generated lists
            print("\nGenerated Lists:")
            for i in range(num_lists): # Loops to generate the specified number of lists
                current_list = random_animals(list_length)
                all_lists.append(current_list) # Adds the generated list to all_lists
                
                # Checks all the generated lists for symmetry, placing an asterisk next to symmetric lists (for ease of grading)
                is_sym = animal_palindrome(current_list)
                status = " *" if is_sym else ""
                
                print(f"{i+1}. {current_list}{status}")
            
            # Loop to validate user input, ensuring it is within the range of lists and a valid integer
            while True:
                pick = input(f"\nChoose a list (1 - {num_lists}) to check for symmetry: ")
                try:
                    idx = int(pick) - 1
                    if 0 <= idx < num_lists:
                        selected_list = all_lists[idx]
                        print(f"\nSelected list: {selected_list}")
                        print(f"Flipped list: {selected_list[::-1]}")
                        print(f"Symmetric?: {animal_palindrome(selected_list)}\n")
                        print("------------------------------------------------------\n")
                        break
                    else:
                        print(f"Please enter a number between 1 and {num_lists}.")
                except ValueError:
                    print("Please enter a valid number.")

        # Manual list entry
        elif choice == "2":
            # Loop to validate user input, preventing an empty input or invalid animals
            while True:
                print(f"\nChoose from the following: {', '.join(animals)}")
                user_animals = input("Enter animals separated by spaces: ").lower()
                if not user_animals.strip():
                    print("Please enter at least one animal.")
                    continue
                
                animal_list = user_animals.split()
                if all(animal in animals for animal in animal_list):
                    break
                
                print("Invalid input, please only use animals from the list above.")

            # Creates a list by splitting user input, outputs the list, the flipped list, and whether it is symmetric or not
            print(f"Flipped list of animals: {animal_list[::-1]}")
            print(f"Symmetric?: {animal_palindrome(animal_list)}\n")
            print("------------------------------------------------------\n")

        # Quit
        elif choice == "3":
            break

        # Error handling for invalid menu option
        else:
            print("\nPlease enter a valid option (1, 2, or 3).")