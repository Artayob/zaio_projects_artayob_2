my_strinng = "The quick brown fox jumps over the lazy dog"

# Get the first character
print("First character: ", my_strinng[0])

# Get the last character
print("Last character: ", my_strinng[-1])

# Access the 5th to 9th character
print("5-9th character:", my_strinng[4:9])

# Access the 5th to 5th last character
print("5th to 5th last characters:", my_strinng[4:-4])

print("-------------------------------------------------------------------")

# Merging strings 
str1 = "The quick brown fox"
str2 = "jumps over the lazy "
str = str1 + " " + str2
print(str)

for c in str:
    print(c)
print("------------------------------------------------------------------")

my_strinng = "The quick brown fox jumps over the lazy dog"

print('quick' in my_strinng)
print('quick' not in my_strinng)

print("-----------------------------------------------------------------")

# Using positional Arguements
str = "The {1} brown fox {2} over the {0} dog.".format('lazy', 'quick', 'jumps')
print(str)

print("-------------------------------------------------------------------")

words = str.split()
print(words)

joined = ' '.join(words)  # ' ' --space is used as a seperator
print(joined)

print("----------------------------------------------------------------")

str = str.replace('quick', 'slow')
print(str)
str = str.upper()
print(str)
str = str.lower()
print(str)