# Step 1: Write user input to file
text_to_write = input("Enter text to write to the file: ")
with open(file_name, 'w') as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append user input to the same file
text_to_append = input("Enter additional text to append: ")
with open(file_name, 'a') as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open(file_name, 'r') as file:
    print(file.read())