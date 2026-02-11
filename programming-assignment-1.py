seed = 12345 # Declare a global "seed" variable for the random number generator

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

    animals = ["bear", "chicken", "lion", "tiger", "ostrich"] # "Pool" of animals to pull from.

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
        print("Choose an option: ")
        print("1. Enter a list of animals")
        print("2. Generate a random list of animals")
        print("3. Quit")
        choice = input()

        # Manual list entry
        if choice == "1":
            # Loop to validate user input, preventing an empty input for the list
            while True:
                user_animals = input("\nEnter animals separated by spaces: ")
                if not user_animals.strip():
                    print("Please enter at least one animal.")
                else:
                    break

            # Creates a list by splitting user input, outputs the list, the flipped list, and whether it is symmetric or not
            animal_list = user_animals.split()
            print(f"Your list of animals: {animal_list}")
            print(f"Flipped list of animals: {animal_list[::-1]}")
            print(f"Symmetric?: {animal_palindrome(animal_list)}\n")

        # Random list generator
        elif choice == "2":
            # Loop to validate user input, preventing non-integer and non-positive inputs for length
            while True:
                length_input = input("\nEnter length of random list: ")

                try:
                    length = int(length_input)
                    if length > 0:
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Generates a new random list of animals, outputs the list, the flipped list, and whether it is symmetric or not
            random_list = random_animals(length)
            print(f"Random list of animals: {random_list}")
            print(f"Flipped list of animals: {random_list[::-1]}")
            print(f"Symmetric?: {animal_palindrome(random_list)}\n")

        # Quit
        elif choice == "3":
            break

        # Error handling for invalid menu option
        else:
            print("\nPlease enter a valid option (1, 2, or 3).")