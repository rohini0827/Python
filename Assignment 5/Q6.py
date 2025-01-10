# Write a Python program that:
# Asks the user for the name of a source file (e.g., source.txt) and
# a destination file (e.g., destination.txt).
# Copies the content of the source file to the destination file.
from Q5 import content

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file,"r") as src:
        content = src.read()

    with open(destination_file,"w") as dest:
        dest.write(content)

    print(f"Content copied from {source_file} to {destination_file} successfully.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error Occurred: {e}")