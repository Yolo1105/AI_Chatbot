from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Initialize the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def chatbot_response(question):
    # Encode the user's question and add special tokens
    input_ids = tokenizer.encode(question, return_tensors='pt')

    # Generate a response from the model
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # Decode the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Example interaction with the chatbot
if __name__ == "__main__":
    print("Chatbot: What is your name?")
    print("Response:", chatbot_response("What is your name?"))
    
    print("\nChatbot: Tell me a joke.")
    print("Response:", chatbot_response("Tell me a joke."))

    print("\nChatbot: How are you?")
    print("Response:", chatbot_response("How are you?"))
    
    print("\nChatbot: What can you do?")
    print("Response:", chatbot_response("What can you do?"))

    print("\nChatbot: Where do you live?")
    print("Response:", chatbot_response("Where do you live?"))
