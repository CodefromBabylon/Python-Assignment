# File Read & Write Challenge with Error Handling

def process_file():
    """Main function to handle file reading, processing, and writing"""
    
    # Get filename from user
    filename = input("Enter the filename to read: ")
    
    try:
        # Read the original file
        with open(filename, 'r') as input_file:
            content = input_file.read()
        
        print(f"Successfully read from '{filename}'")
        
        # Process the content (modify as needed)
        # Example: Convert to uppercase and add line numbers
        modified_content = modify_content(content)
        
        # Create output filename
        output_filename = get_output_filename(filename)
        
        # Write to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Successfully wrote modified content to '{output_filename}'")
        print(f"Original file size: {len(content)} characters")
        print(f"New file size: {len(modified_content)} characters")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please check the filename and try again.")
        
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        print("You may not have read access to this file.")
        
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
        
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{filename}'.")
        print("The file may not be a text file or may have an unsupported encoding.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def modify_content(content):
    """Modify the file content - customize this function as needed"""
    # Example modification: Convert to uppercase and add line numbers
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        modified_line = f"{i:3d}. {line.upper()}"
        modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

def get_output_filename(original_filename):
    """Generate output filename by adding '_modified' before extension"""
    if '.' in original_filename:
        name, ext = original_filename.rsplit('.', 1)
        return f"{name}_modified.{ext}"
    else:
        return f"{original_filename}_modified"

def main():
    """Main program function"""
    print("=== File Processor ===")
    print("This program reads a file, modifies its content,")
    print("and writes the modified version to a new file.")
    print()
    
    while True:
        process_file()
        
        # Ask if user wants to process another file
        print()
        another = input("Process another file? (y/n): ").lower()
        if another != 'y':
            break
        print()

if __name__ == "__main__":
    main()