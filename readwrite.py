# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn't exist or can't be read.

try:
    
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")
    
    
    with open(input_filename, "r") as input_file:
        data = input_file.read()
        print("Original content:")
        print(data)
        
        modified_data = data.upper() + "\nModified: Python is awesome!"
        
    
    with open(output_filename, "w") as output_file:
        output_file.write(modified_data)
        print(f"\nModified content written to {output_filename}")
        print(modified_data)
        
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when accessing '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
