# Write a Python program that:
# Reads the content of a file named input.txt.
# Writes the reversed content to another file named reversed.txt.

try:
    with open("input.txt","r") as infile:
        content = infile.read()
except FileNotFoundError:
    print("Error: input.txt not found!")
    exit()

reversed_content = content[::-1]

with open("reversed.txt","w") as outfile:
    outfile.write(reversed_content)

print("Reversed content has been written to reversed.txt.")