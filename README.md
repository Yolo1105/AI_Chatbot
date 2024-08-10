# Local Search and Chatbot Creation using GPT-2

This project demonstrates how to build a local search engine to index and search through HTML files and use that data to fine-tune a GPT-2 model to create a chatbot. The chatbot will be capable of answering questions and generating responses based on the content extracted from local files.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Extracting and Indexing Content](#1-extracting-and-indexing-content)
  - [2. Performing Terminal-Based Search](#2-performing-terminal-based-search)
  - [3. Fine-Tuning GPT-2 for the Chatbot](#3-fine-tuning-gpt-2-for-the-chatbot)
  - [4. Running the Chatbot](#4-running-the-chatbot)

## Overview

This project involves two main components:
1. **Local Search Engine**: A system to parse, index, and search through HTML files stored locally on your machine.
2. **GPT-2 Based Chatbot**: A chatbot built using the GPT-2 model, fine-tuned on the content extracted from the local files, allowing it to provide intelligent responses based on the data.

## Prerequisites

Before starting, ensure you have the following installed:
- Python 3.x
- Node.js (for optional server-based search)
- Required Python packages: `transformers`, `torch`, `beautifulsoup4`, `requests`

## Project Structure

```
.
├── html_files/                 # Directory containing your HTML files
├── extract_content.py          # Python script to extract and index content from HTML files
├── search_terminal.py          # Python script for terminal-based search
├── train_gpt2.py               # Python script for fine-tuning the GPT-2 model
├── content.json                # Generated file containing extracted content
├── index.json                  # Generated file containing keyword index
├── results/                    # Directory where fine-tuned models will be saved
├── logs/                       # Directory to save training logs
└── README.md                   # This README file
```

## Setup Instructions

### 1. Extracting and Indexing Content

The first step is to extract content from your local HTML files and create an index.

1. Place all your HTML files in the `html_files/` directory.
2. Run the following command to extract and index the content:

   ```bash
   python extract_content.py
   ```

This script will:
- Parse each HTML file in the `html_files/` directory.
- Extract the title and body content.
- Create a JSON file (`content.json`) containing the parsed content.
- Create an index (`index.json`) mapping keywords to the URLs of the documents.

### 2. Performing Terminal-Based Search

You can perform searches directly in the terminal based on the indexed content.

1. Run the following command to start the terminal-based search:

   ```bash
   python search_terminal.py
   ```

2. Enter your search query in the terminal when prompted. The script will display matching results directly in the terminal.

### 3. Fine-Tuning GPT-2 for the Chatbot

To create a chatbot that can answer questions based on your local content, you need to fine-tune a pre-trained GPT-2 model.

1. Ensure you have the `transformers` and `torch` libraries installed:

   ```bash
   pip install transformers torch
   ```

2. Prepare a dataset from the indexed content. You can customize this dataset by selecting relevant question-answer pairs or generating prompts based on your data.

3. Run the following command to fine-tune the GPT-2 model:

   ```bash
   python train_gpt2.py
   ```

This script will:
- Load the pre-trained DistilGPT-2 model.
- Tokenize the training data using the GPT-2 tokenizer.
- Fine-tune the model on your custom dataset.
- Save the fine-tuned model and tokenizer in the `results/` directory.

### 4. Running the Chatbot

After fine-tuning the GPT-2 model, you can use it to create a chatbot.

1. Load the fine-tuned model and tokenizer.
2. Use the model to generate responses to user queries.

You can extend this functionality to build a fully interactive chatbot.
