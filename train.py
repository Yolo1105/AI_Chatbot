from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, AutoTokenizer, AutoModelForCausalLM
from dataset import get_dataset

# Load the GPT-2 tokenizer (works with DistilGPT-2 model)
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

# Add a new pad token
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Prepare the dataset for training
dataset = get_dataset()
train_texts = [f"Question: {pair['question']} Answer: {pair['answer']}" for pair in dataset]
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=50, return_tensors='pt')

# Load the pre-trained DistilGPT-2 model
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Resize the model's embedding layer to accommodate the new pad token
model.resize_token_embeddings(len(tokenizer))

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',          # Directory to save the model outputs
    num_train_epochs=5,              # Number of training epochs
    per_device_train_batch_size=2,   # Batch size for training
    logging_dir='./logs',            # Directory to save logs
    logging_steps=10,                # Log every X updates
)

# Trainer
trainer = Trainer(
    model=model,                         # The DistilGPT-2 model
    args=training_args,                  # Training arguments
    train_dataset=train_encodings.input_ids,   # The tokenized input data
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained('./fine-tuned-distilgpt2')
tokenizer.save_pretrained('./fine-tuned-distilgpt2')
