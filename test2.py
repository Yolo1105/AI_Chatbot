import re
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Initialize GPT-2 Model and Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Function to read the content of the MD file
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to clean up text from Markdown content
def clean_text(text):
    # Remove markdown links, headings, excessive whitespace, and unwanted characters
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove links
    text = re.sub(r'#+\s', '', text)  # Remove headings
    text = re.sub(r'-{2,}', '', text)  # Remove excessive dashes
    text = re.sub(r'\s{2,}', ' ', text)  # Replace multiple spaces with one space
    text = re.sub(r'\n', ' ', text)  # Replace newlines with spaces
    return text.strip()

# Function to search for the term in the text and generate a response
def generate_response_from_md(search_term, text):
    # Convert both search term and text to lowercase for case-insensitive search
    search_term = search_term.lower()
    text = text.lower()

    # Use regex to find sentences containing the search term
    sentences = re.findall(r'[^.!?]*' + re.escape(search_term) + r'[^.!?]*[.!?]', text)

    # Generate a conversational response based on the search results
    if sentences:
        responses = []
        for sentence in sentences:
            cleaned_sentence = clean_text(sentence.strip())
            # Format response for specific terms like "data management"
            if "data management" in search_term:
                responses.append(f"Data management in HPC involves managing and organizing data to ensure efficient processing, storage, and retrieval throughout the research data lifecycle. For example, {cleaned_sentence}")
            else:
                responses.append(f"I found some information that might help you: {cleaned_sentence}")
        return responses
    else:
        return [f"I'm sorry, I couldn't find any detailed information about '{search_term}' in the provided text. Let me generate a general explanation for you."]

# Function to generate a response using GPT-2
def generate_gpt2_response(question):
    input_ids = tokenizer.encode(question, return_tensors='pt')

    output = model.generate(input_ids, max_length=50, num_return_sequences=1, 
                            pad_token_id=tokenizer.eos_token_id, attention_mask=input_ids.ne(tokenizer.pad_token_id))

    # Explicitly set clean_up_tokenization_spaces to True
    response = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return response

# Placeholder function for online search (not implemented in this environment)
def search_online(question):
    # This function would integrate with an API or web scraping tool to find relevant information online.
    # Example: Using Google's Custom Search API
    return "I couldn't find this in the local data, but here's what I found online: [online search result]"

# Function to write responses to an MD file
def write_to_md_file(file_path, user_input, responses):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"## User Input: {user_input}\n")
        for i, response in enumerate(responses, start=1):
            file.write(f"**Chatbot Response {i}:** {response}\n\n")
        file.write("\n---\n\n")

def main():
    # Path to the MD file for storing responses
    output_file_path = 'chatbot_responses.md'
    
    # Clear the file content at the start
    open(output_file_path, 'w').close()

    # Path to the MD file to read from
    input_file_path = 'data_management.md'
    
    # Read the content of the MD file
    text = read_md_file(input_file_path)

    print("Welcome to the AI Chatbot! How can I assist you today?")
    
    while True:
        # Get input from the user
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Generate a response based on the MD file content
        responses_from_md = generate_response_from_md(user_input, text)

        # If no relevant data is found in the MD file, fallback to GPT-2 model or online search
        if "I'm sorry" in responses_from_md[0]:
            # Generate a GPT-2 response
            final_response = generate_gpt2_response(user_input)
            # Example of online search fallback (commented out since not implemented)
            # final_response = search_online(user_input)
            print(f"\nChatbot: {final_response}\n")
            write_to_md_file(output_file_path, user_input, [final_response])
        else:
            # Print responses from MD file search
            for i, response in enumerate(responses_from_md, start=1):
                print(f"\nChatbot Response {i}:\n{response}\n")
            write_to_md_file(output_file_path, user_input, responses_from_md)