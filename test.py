import re
import logging
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B')
try:
    model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-j-6B')
except OSError:
    model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-j-6B', force_download=True)

logging.basicConfig(filename='chatbot_debug.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_md_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        return ""

def clean_text(text):
    text = re.sub(r'\[.*?\]\(.*?\)', '', text) 
    text = re.sub(r'#+\s', '', text)  
    text = re.sub(r'-{2,}', '', text) 
    text = re.sub(r'\s{2,}', ' ', text)  
    text = re.sub(r'\n', ' ', text)  
    return text.strip()

def generate_response_from_md(search_term, text):
    search_term = search_term.lower()
    text = text.lower()
    sentences = re.findall(r'[^.!?]*' + re.escape(search_term) + r'[^.!?]*[.!?]', text)

    if sentences:
        responses = []
        for sentence in sentences:
            cleaned_sentence = clean_text(sentence.strip())
            responses.append(f"Here's what I found from NYU HPC site: {cleaned_sentence}")
        return responses
    else:
        logging.info("Search term not found: %s", search_term)
        return [f"I'm sorry, I couldn't find any detailed information about '{search_term}'. Let me try to generate an answer for you."]

def generate_gpt_j_response(question):
    input_ids = tokenizer.encode(question, return_tensors='pt')
    output = model.generate(
        input_ids,
        max_length=100,  
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9,
        do_sample=True
    )
    response = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    response = remove_repetition(response)
    return clean_text(response)

def remove_repetition(text):
    sentences = text.split('. ')
    seen = set()
    filtered_sentences = []

    for sentence in sentences:
        if sentence not in seen:
            seen.add(sentence)
            filtered_sentences.append(sentence)
    
    return '. '.join(filtered_sentences).strip()

def remove_repeated_names(text):
    lines = text.split("\n")
    cleaned_lines = []
    previous_line = None

    for line in lines:
        if line.strip() != previous_line:
            cleaned_lines.append(line.strip())
            previous_line = line.strip()
    
    return " ".join(cleaned_lines).strip()

def write_to_md_file(file_path, user_input, responses):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"## User Input: {user_input}\n")
        for i, response in enumerate(responses, start=1):
            file.write(f"**Response {i}:** {response}\n\n")
        file.write("\n---\n\n")

def main():
    output_file_path = 'chatbot_responses.md'
    
    open(output_file_path, 'w').close()

    input_file_path = 'data_management.md'
    
    text = read_md_file(input_file_path)

    print("Welcome to the NYU HPC Chatbot! How can I assist you today?")
    
    while True:
        user_input = input("Please enter your prompt here: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Thank you for using NYU HPC Chatbot!")
            break

        responses_from_md = generate_response_from_md(user_input, text)

        if "I'm sorry" in responses_from_md[0]:
            final_response = generate_gpt_j_response(user_input)
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
        print("\nThank you for using NYU HPC Chatbot!")
