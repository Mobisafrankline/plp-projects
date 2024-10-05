def create_and_write_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("The second line contains a number: 42.\n")
            file.write("This is the third line with a mix of text and numbers: 3.14.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating and writing to the file: {e}")

def read_and_display_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Contents of the file:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is the first appended line.\n")
            file.write("The second appended line contains another number: 100.\n")
            file.write("This is the third appended line with more text and numbers: 2.71.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
