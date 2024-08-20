import re
import logging
import spacy
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Initialize GPT-2 Model and Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Setup logging
logging.basicConfig(filename='chatbot_debug.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

# Function to read the content of the MD file
def read_md_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        return ""

# Function to clean up and parse text using spaCy for more advanced text analysis
def clean_and_parse_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_space])

# Function to search for the term in the text and generate a response using spaCy
def generate_response_from_md(search_term, text):
    search_term = search_term.lower()
    doc = nlp(text.lower())

    sentences = [sent.text for sent in doc.sents if search_term in sent.text.lower()]

    if sentences:
        responses = [f"Here's what I found on '{search_term}': {clean_and_parse_text(sent)}" for sent in sentences]
        return responses
    else:
        logging.info("Search term not found: %s", search_term)
        return [f"I'm sorry, I couldn't find any detailed information about '{search_term}'. Let me try to generate an answer for you."]

# Function to generate a response using GPT-2
def generate_gpt2_response(question):
    input_ids = tokenizer.encode(question, return_tensors='pt')
    output = model.generate(
        input_ids,
        max_length=250,  # Allow for longer responses
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9,
        do_sample=True
    )
    response = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return clean_and_parse_text(response)  # Use spaCy to parse the response

# Function to write responses to an MD file
def write_to_md_file(file_path, user_input, responses):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"## User Input: {user_input}\n")
        for i, response in enumerate(responses, start=1):
            file.write(f"**Response {i}:** {response}\n\n")
        file.write("\n---\n\n")

# Main function to handle user interaction
def main():
    output_file_path = 'chatbot_responses.md'
    input_file_path = 'data_management.md'
    
    open(output_file_path, 'w').close()  # Clear the file content at the start

    text = read_md_file(input_file_path)

    print("Welcome to the AI Chatbot! How can I assist you today?")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Have a great day!")
            break

        responses_from_md = generate_response_from_md(user_input, text)

        if "I'm sorry" in responses_from_md[0]:
            final_response = generate_gpt2_response(user_input)
            print(f"\n{final_response}\n")
            write_to_md_file(output_file_path, user_input, [final_response])
        else:
            for i, response in enumerate(responses_from_md, start=1):
                print(f"\n{response}\n")
            write_to_md_file(output_file_path, user_input, responses_from_md)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye! Have a great day!")
