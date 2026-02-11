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
    animals = ["bear", "chicken", "lion", "tiger", "ostrich"] # "Pool" of animals to pull from.
    dummy = object() # Creates a dummy object in the user's memory
    seed = id(dummy) # Checks the memory address of the dummy (to use as a random seed)

    random_animal_list = []
    for i in range(length):
        # LCG algorithm (Xn+1 = (a Xn + c) mod m), which generates a pseudo-random number
        seed = (seed * 1103515245 + 12345) & 0x7fffffff
        random_animal_list.append(animals[seed % len(animals)])

    return random_animal_list

if __name__ == "__main__":
    print(random_animals(5))