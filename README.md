📘 Lab 1 – Python Basics & String Manipulation

This lab focuses on basic Python programming concepts such as loops, conditionals, lists, and string operations.

✅ Tasks Implemented

Count Vowels

Counts the number of vowels (a, e, i, o, u) in a given string.

Sort User Input

Takes 5 numbers from the user.

Sorts them in:

Ascending order

Descending order

Count Occurrences of "iti"

Counts how many times the substring "iti" appears in a string.

Remove Vowels

Removes all vowels from a word.

Generates a shortened version.

Find Locations of "i"

Prints all positions of the character "i" in a string.

Multiplication Table Generator

Generates a multiplication table from 1 to n.

Mario Pyramid

Prints a pyramid pattern similar to Mario game style.

📗 Lab 2 – Functions & Validation

This lab focuses on functions, validation, loops, and problem solving.

✅ Tasks Implemented

Generate Sequence Function

generate_array(length, start)

Returns an array of given length.

Values increment by 1 starting from start.

FizzBuzz Function

Returns:

"Fizz" → divisible by 3

"Buzz" → divisible by 5

"FizzBuzz" → divisible by both

Reverse String Function

Takes user input.

Returns reversed string.

User Data Validation

Validates:

Name (not empty, not numbers)

Email format (Bonus)

Longest Alphabetical Substring

Example:

Input: abdulrahman
Output: abdu

Number Statistics Program

Reads numbers until user enters "done".

Prints:

Total

Count

Average

Handles invalid inputs.

Word Guessing Game (Hangman)

Random word selection.

User enters name.

7 attempts maximum.

Shows correct letter positions.

📙 Lab 3 – Crowdfunding Console Application
📌 Project Overview

A console-based crowdfunding system that allows users to:

Register & login

Create fundraising projects

Manage projects

Inspired by crowdfunding platforms.

🔐 1. Authentication System
Registration Includes:

First Name

Last Name

Email

Password

Confirm Password

Egyptian Mobile Number (validated format)

Login

User logs in using email and password.

Account activation required.

📁 2. Project Management

Each user can:

✅ Create a project

Title

Details

Total Target (e.g., 250000 EGP)

Start Date

End Date (validated date format)

👀 View all projects

✏ Edit their own projects

❌ Delete their own projects

🔎 Search projects by date

💾 Data Storage

Data stored using JSON files.

Modular design separating:

Menu

Business logic

Data handling

📕 Lab 4 – OOP & API Integration

This lab focuses on Object-Oriented Programming, Custom Exceptions, Class Methods, and API clients.

1️⃣ Queue Implementation
Basic Queue Class

Methods:

insert(value) → Adds value to rear

pop() → Removes value from front

Returns None and prints warning if empty

is_empty() → Returns True or False

2️⃣ Named Queue with Size Limit

Enhanced queue with:

🔹 Features

Has a name

Has a maximum size

Raises custom exception:

QueueOutOfRangeException

Tracks all created queues

Retrieve queue by name

Bonus:

save() → Save all queues to file

load() → Load queues from file

Custom Exception
class QueueOutOfRangeException(Exception):

Raised when insertion exceeds allowed size.

Concepts Used:

Error handling
