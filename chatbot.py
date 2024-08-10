# chatbot.py

from transformers import DistilGPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model and tokenizer
fine_tuned_model = DistilGPT2LMHeadModel.from_pretrained('./fine-tuned-distilgpt2')
fine_tuned_tokenizer = GPT2Tokenizer.from_pretrained('./fine-tuned-distilgpt2')

def chatbot_response(question):
    # Encode the user's question
    input_text = f"Question: {question} Answer:"
    input_ids = fine_tuned_tokenizer.encode(input_text, return_tensors='pt')

    # Generate a response
    output = fine_tuned_model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=fine_tuned_tokenizer.eos_token_id)

    # Decode and return the response
    response = fine_tuned_tokenizer.decode(output[0], skip_special_tokens=True)
    return response.split("Answer:")[1].strip()

# Example interaction with the chatbot
if __name__ == "__main__":
    print(chatbot_response("What is your name?"))
    print(chatbot_response("Tell me a joke."))
    print(chatbot_response("How are you?"))
