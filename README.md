# File Read & Write Challenge

This Python program reads the content of a user-specified input file, modifies the content by converting it to uppercase and appending a custom message, and writes the modified content to a user-specified output file. It also includes error handling for common file-related issues.

## How to Run

1. Ensure you have Python installed on your system.
2. Place the `readwrite.py` script in your working directory.
3. Run the script using the command:
   ```
   python readwrite.py
   ```
4. When prompted, enter the name of the input file you want to read.
5. Enter the name of the output file where the modified content will be saved.

## What the Program Does

- Reads the content of the input file.
- Prints the original content to the console.
- Converts the content to uppercase and appends the line:
  ```
  Modified: Python is awesome!
  ```
- Writes the modified content to the output file.
- Prints the modified content to the console.

## Error Handling

The program handles the following errors gracefully:
- `FileNotFoundError`: If the input file does not exist.
- `PermissionError`: If the program does not have permission to read the input file.
- Other unexpected errors are caught and displayed with an error message.

## Example

```
Enter the input filename: example.txt
Enter the output filename: example2.txt
Original content:
Hello, world!

Modified content written to output.txt
HELLO, WORLD!
Modified: Python is awesome!
