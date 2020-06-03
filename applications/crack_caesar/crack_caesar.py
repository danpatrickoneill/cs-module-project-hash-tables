import string
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("ciphertext.txt") as f:
  text = f.read()
# Your code here
valid_chars = set(string.ascii_uppercase)
frequencies = {}
letter_count = 0
for char in text:
  if char in valid_chars:
    # Increment letter_count for finding percentages
    letter_count += 1
    # Set char as key in freq dict; start at 1
    if char not in frequencies:
      frequencies[char] = 1
    # Else, increment count
    else:
      frequencies[char] += 1

print(letter_count)
print(frequencies)

# Probably no need to calculate percentages; lining up the rankings an equally valid option

