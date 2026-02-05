import re

def generate_array(a, b):
    """
    Generates an array of integers from a to b (inclusive).

    Parameters:
    a (int): The starting integer.
    b (int): The number of integers to generate.

    Returns:
    list: A list of integers from a to b.
    """
    return list(range(a, a + b))
print(generate_array(2, 6))

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return False

print(fizz_buzz(15))

def fizz_buzz(n):
    result = ''
    if n % 3 == 0:
        result += "Fizz"
        # result.append("Fizz ")
    if n % 5 == 0:
        result += "Buzz"
        # result.append("Buzz ")
    return result

print(fizz_buzz(15))

def reverse_string(s):
    """
    Reverses the given string.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return s[::-1]

print(reverse_string("hello"))

# def user_info():
#     """
#     Returns a formatted string with user information.

#     Returns:
#     str: A formatted string containing the user's name and email.
#     """

#     while True:
#         name = input("Enter your name: ").strip()
#         if name and name.replace(" ", "").isalpha():
#             break
#         print("Invalid name. Please try again.")

#     while True:
#         email = input("Enter your email: ").strip()
#         regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if re.fullmatch(regex, email):
#             break
#         print("Invalid email format. Please try again.")

#     return f"User {name} has email {email}"

# print(user_info())

def longest_alphabetical_order_substring(s):
    """
    Finds the longest substring in alphabetical order.

    Parameters:
    s (str): The input string.

    Returns:
    str: The longest substring in alphabetical order.
    """
    longest = ""
    current = ""
    for i in range(len(s)):
        if i == 0 or s[i] >= s[i - 1]:
            current += s[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = s[i]

    if len(current) > len(longest):
        longest = current

    return longest

print(longest_alphabetical_order_substring("abdulrahman"))

def numbers():
    """
    Prompts the user to enter numbers until 'stop' is entered.
    Returns the total, count and average of the entered numbers.

    Returns:
    tuple: A tuple containing the total, count and average numbers.
    """
    nums = []
    while True:
        entry = input("Enter a number (or 'done' to finish): ").strip()
        if entry.lower() == 'done':
            break
        try:
            num = float(entry)
            nums.append(num)
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if nums:
        total = sum(nums)
        count = len(nums)
        average = total / count
        return total, count, average
    else:
        return None, None, None
    
print(numbers())

import random

# Hardcoded list of words
words = ["first", "second", "third"]

# Get user name
name = input("Enter your name: ")
print(f"Welcome {name}! Let's play Hangman Game.")

# Choose random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
turns = 7

print("\nWord to guess:", " ".join(guessed_word))

while turns > 0 and "_" in guessed_word:
    guess = input("\nGuess an alphabet: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess ")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        turns -= 1
        print(f"Wrong guess . Turns left: {turns}")

    print("Word:", " ".join(guessed_word))

if "_" not in guessed_word:
    print(f"\n Congratulations {name}, you guessed the word: {word}")
else:
    print(f"\n Game Over! The word was: {word}")
