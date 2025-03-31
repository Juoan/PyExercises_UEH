x = "Hello World!"

#1. Use the len function to print the length of the string.
print(len(x))

#2. Get the characters from index 2 to index 4 (llo).
print(x[2:5])

#3. Return the string without any whitespace at the beginning or the end.
y = " Hello World! "
print(y.strip())

#4. Convert the value of txt to upper/lower case
print(x.upper())
print(x.lower())

#5. Replace the character l with a L.
print(x.replace("l", "L"))

#6. Enter a string prompt keyboard then display it reverse order
string = input("Enter a string: ")
print(string[::-1])
