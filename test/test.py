import re

# Function to read the content of the MD file
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to search for the term in the text
def search_in_text(search_term, text):
    # Convert both search term and text to lowercase for case-insensitive search
    search_term = search_term.lower()
    text = text.lower()

    # Use regex to find sentences containing the search term
    sentences = re.findall(r'[^.!?]*' + re.escape(search_term) + r'[^.!?]*[.!?]', text)

    # Return the sentences found
    if sentences:
        return sentences
    else:
        return ["No results found."]

def main():
    # Path to the MD file
    file_path = 'data_management.md'
    
    # Read the content of the MD file
    text = read_md_file(file_path)

    # Get search term from user
    search_term = input("Enter search term: ")

    # Get search results
    results = search_in_text(search_term, text)

    # Print results in a labeled format
    if results[0] != "No results found.":
        print(f"Search results for '{search_term}':")
        for index, result in enumerate(results, start=1):
            print(f"Result {index}:")
            print(result.strip())
            print("-" * 50)  # Separator between results
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
