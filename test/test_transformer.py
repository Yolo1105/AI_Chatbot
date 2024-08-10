from transformers import DistilGPT2LMHeadModel, DistilGPT2Tokenizer

model = DistilGPT2LMHeadModel.from_pretrained('distilgpt2')
tokenizer = DistilGPT2Tokenizer.from_pretrained('distilgpt2')

text_data = [
    "Welcome to our website. We provide the best services in the industry.",
    "Our mission is to deliver high-quality products that satisfy our customers.",
    "For more information, visit our FAQ section."
]

inputs = tokenizer(text_data, return_tensors='pt', padding=True, truncation=True)
