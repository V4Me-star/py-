def process_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes the changes to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            # Modify the content (e.g., convert to uppercase)
            modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully processed '{input_filename}' and saved the result to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please check the file name and try again.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to read or write the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the name of the file to read: ")
    output_file = input("Enter the name of the new file to create: ")

    process_file(input_file, output_file)