# Create a program that reads a file 
# and writes a modified version to a new file.
# Ask the user for a filename and handle errors 
# if it doesn’t exist or can’t be read.


def read_and_write_file():
    try:
        # Ask for filename
        filename = input("Enter the name of the file: ")
        
        # Try to open the file
        with open(filename, 'r') as file:
            content = file.read()
            print(content)

        modified = content.lower()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as file:
            file.write(modified)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print(f"File not found: {filename}")

read_and_write_file()