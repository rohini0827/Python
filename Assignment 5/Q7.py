# Write a Python program that reads a text file and
# counts how many times each word appears in the file.
# The program should display the word frequency in descending order.

from collections import Counter

from Q5 import content

file_name = input("Enter the file name: ")

try:
    with open(file_name,"r") as file:
        content = file.read()

    words = content.lower().split()

    words = [''.join(char for char in word if char.isalnum()) for word in words]

    word_count = Counter(words)

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print("\nWord Frequency (descending order): ")
    for word, count in sorted_word_count:
        print(f"{word}:{count}")
except FileNotFoundError:
    print(f"Error: the file '{file_name}' does not exist.")
except Exception as e:
    print(f"an error occurred: {e}")