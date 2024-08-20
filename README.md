# NYU HPC Chatbot and Local Search Engine

This project showcases how to build a local search engine to index content from Markdown files and use that indexed content to fine-tune a GPT-2 model. The resulting chatbot is capable of answering questions and generating responses based on the content extracted from the indexed files.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Extracting and Indexing Content](#1-extracting-and-indexing-content)
  - [2. Performing Terminal-Based Search](#2-performing-terminal-based-search)
  - [3. Fine-Tuning GPT-2 for the Chatbot](#3-fine-tuning-gpt-2-for-the-chatbot)
  - [4. Running the Chatbot](#4-running-the-chatbot)
- [Usage Example](#usage-example)
- [Logging](#logging)

## Overview

This project consists of two main components:

1. **Local Search Engine**: A system that reads Markdown (.md) files, cleans up the text, and allows for keyword searches within the terminal.
2. **GPT-2 Based Chatbot**: A chatbot built using the GPT-2 model, fine-tuned with the content extracted from the local Markdown files. It provides intelligent responses based on the indexed content or generates new responses when needed.

## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.x
- Required Python packages: `transformers`, `torch`, `beautifulsoup4`, `requests`

## Project Structure

```plaintext
.
├── __pycache__/                  # Python cache directory
├── .git/                         # Git configuration and history
├── test/                         # Directory containing test scripts or files
├── chatbot_debug.log             # Log file for debugging chatbot
├── chatbot_responses.md          # Markdown file to store chatbot responses
├── data_management.md            # Example Markdown file with data management content
├── README.md                     # This README file
├── requirements.txt              # List of required Python packages
└── test.py                       # Python script to test the functionality
```

## Setup Instructions

### 1. Extracting and Indexing Content

The first step is to extract and clean the content from the Markdown file(s).

1. Place your Markdown files in the same directory as the script.
2. Ensure the `data_management.md` file or another `.md` file with the content you want to search is present.

### 2. Performing Terminal-Based Search

You can perform searches directly in the terminal based on the content of the Markdown files.

1. Run the script (`test.py`) in your terminal.
2. Enter your search query when prompted, and the script will return relevant sentences from the Markdown file.

### 3. Fine-Tuning GPT-2 for the Chatbot

If the search functionality does not provide a satisfactory response, the script will generate a response using a pre-trained GPT-2 model.

1. Ensure you have the necessary libraries installed:

   ```bash
   pip install transformers torch
   ```

2. The script will automatically generate responses using GPT-2 if the search term is not found in the Markdown content.

### 4. Running the Chatbot

To start the chatbot:

1. Run the `test.py` script.
2. The chatbot will prompt you for input. You can type any question or command.
3. To exit the chatbot, type `exit` or `quit`.

## Usage Example

```bash
python test.py
```

**Example Interaction:**

```plaintext
Welcome to the NYU HPC Chatbot! How can I assist you today?
Please enter your prompt here: How do I manage data?
```

## Logging

The chatbot maintains a log of all interactions in the `chatbot_debug.log` file, including errors and the responses generated. All user inputs and responses are also saved to `chatbot_responses.md` for reference and review.