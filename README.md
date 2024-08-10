# NYU HPC Chatbot

## Overview

The NYU HPC Chatbot provides users with accurate and conversational responses to queries related to the NYU High Performance Computing (HPC) website. This system utilizes web crawling, SQL database management, and transformer-based language models to deliver relevant and contextually appropriate answers.

## How It Works

### 1. Web Crawling and Data Extraction
- **Crawling**: The chatbot employs a web crawler to systematically browse and extract content from the NYU HPC website. This involves retrieving web pages, parsing HTML, and extracting meaningful information such as articles, FAQs, and other relevant content.
- **Data Extraction**: Extracted data is cleaned and formatted. HTML tags are removed, and text is normalized to ensure consistency and readability.

### 2. Database Management
- **Data Storage**: Cleaned and structured information is stored in an SQL database. The database schema is designed for efficient data handling and querying.
- **Database Updates**: A mechanism is in place to detect changes on the NYU HPC website (e.g., through checksums or timestamps). The database is updated regularly to reflect these changes, ensuring that the information remains current.

### 3. Query Handling
- **User Input**: When a user asks a question, the chatbot captures and processes the query. Natural Language Processing (NLP) techniques are used to understand the intent and extract key entities from the question.
- **Information Retrieval**: The system queries the SQL database to retrieve relevant information based on the processed query. It searches for matching content and determines the most relevant pieces of information.

### 4. Response Generation
- **Contextual Understanding**: The retrieved information is fed into a transformer-based language model, specifically GPT-2. The model is fine-tuned on the extracted data to improve its ability to generate responses that are accurate and relevant to the NYU HPC context.
- **Text Generation**: The model generates a conversational response based on the retrieved information. Techniques like text generation and paraphrasing are used to ensure the response is natural and user-friendly.

### 5. Feedback and Improvement
- **User Feedback**: Users can provide feedback on the quality of the responses. This feedback is used to make iterative improvements to the system.
- **Continuous Learning**: The chatbot system can be periodically updated with new data and retrained models to enhance performance and accuracy over time.

## Principles Used

1. **Efficiency**: The system is designed to efficiently crawl and process website content, manage large volumes of data, and quickly retrieve and generate responses.
2. **Accuracy**: Emphasis is placed on accurate information retrieval and response generation. Fine-tuning the language model on specific data helps improve the relevance and correctness of responses.
3. **User Experience**: The chatbot aims to provide a conversational and engaging user experience. Responses are crafted to be natural and easy to understand.
4. **Scalability**: The architecture supports scaling to handle increased content and user queries. Regular updates ensure that the system remains relevant as the website evolves.
5. **Compliance and Ethics**: The system adheres to legal and ethical standards for web crawling and data usage, ensuring respect for website policies and user privacy.

## Installation and Usage

1. **Install Dependencies**: Ensure you have the necessary libraries installed (e.g., BeautifulSoup, Scrapy, SQL libraries, transformers).
2. **Run Web Crawler**: Execute the web crawler script to start extracting data from the NYU HPC website.
3. **Set Up Database**: Configure and initialize the SQL database to store the extracted content.
4. **Train Model**: Fine-tune the GPT-2 model on the extracted data.
5. **Start Chatbot**: Run the chatbot application to begin handling user queries and generating responses.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.