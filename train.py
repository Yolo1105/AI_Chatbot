from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, AutoTokenizer, AutoModelForCausalLM
from dataset import get_dataset

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

tokenizer.add_special_tokens({'pad_token': '[PAD]'})

dataset = get_dataset()
train_texts = [f"Question: {pair['question']} Answer: {pair['answer']}" for pair in dataset]
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=50, return_tensors='pt')

model = AutoModelForCausalLM.from_pretrained("distilgpt2")

model.resize_token_embeddings(len(tokenizer))

training_args = TrainingArguments(
    output_dir='./results',          
    num_train_epochs=5,              
    per_device_train_batch_size=2,   
    logging_dir='./logs',            
    logging_steps=10,                
)

trainer = Trainer(
    model=model,                        
    args=training_args,                 
    train_dataset=train_encodings.input_ids,   
)

trainer.train()

model.save_pretrained('./fine-tuned-distilgpt2')
tokenizer.save_pretrained('./fine-tuned-distilgpt2')
