def word_counter(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
filename = input("Enter the filename: ")
word_counter(filename)
