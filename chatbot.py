from transformers import DistilGPT2LMHeadModel, GPT2Tokenizer

fine_tuned_model = DistilGPT2LMHeadModel.from_pretrained('./fine-tuned-distilgpt2')
fine_tuned_tokenizer = GPT2Tokenizer.from_pretrained('./fine-tuned-distilgpt2')

def chatbot_response(question):
    input_text = f"Question: {question} Answer:"
    input_ids = fine_tuned_tokenizer.encode(input_text, return_tensors='pt')

    output = fine_tuned_model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=fine_tuned_tokenizer.eos_token_id)

    response = fine_tuned_tokenizer.decode(output[0], skip_special_tokens=True)
    return response.split("Answer:")[1].strip()

if __name__ == "__main__":
    print(chatbot_response("What is your name?"))
    print(chatbot_response("Tell me a joke."))
    print(chatbot_response("How are you?"))
