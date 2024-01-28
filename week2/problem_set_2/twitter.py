# get user input 
ans = input("Input: ")
print("Output: ", end="")


# loop through every letter
for letter in ans:
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(letter, end="")

print()

