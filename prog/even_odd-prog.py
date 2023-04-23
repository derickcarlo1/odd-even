# Open the numbers.txt file for reading
file = open("numbers.txt", "r")

# Create two empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through each line in the file
for line in file:
    # Convert the line to an integer
    number = int(line.strip())

    # Check if the number is even or odd and add it to the appropriate list
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Close the file
file.close()

# Open the even.txt file for writing and write even numbers to it
even_file = open("even.txt", "w")
for number in even_numbers:
    even_file.write(str(number) + "\n")
even_file.close()

# Open the odd.txt file for writing and write odd numbers to it
odd_file = open("odd.txt", "w")
for number in odd_numbers:
    odd_file.write(str(number) + "\n")
odd_file.close()
