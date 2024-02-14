# Multiple PDF Chat 🦄

Welcome to the Multiple PDF Chat repository! This project allows users to engage in conversational interactions based on the content of multiple PDF documents uploaded by the user. The system utilizes Streamlit for the user interface and leverages various natural language processing and machine learning techniques.

## Overview

The project is designed to enable users to ask questions related to the content of their PDF documents and receive responses based on the information contained within them. The conversational system interacts with the user in real-time and provides relevant answers using a conversational retrieval chain.

## Features

- **PDF Text Extraction**: Extracts text from uploaded PDF documents.
- **Text Chunking**: Splits the extracted text into smaller, manageable chunks.
- **Embeddings Generation**: Generates embeddings for each text chunk using Hugging Face models.
- **Conversational Retrieval Chain**: Utilizes a conversational retrieval chain to provide responses to user questions based on the embeddings generated.

## Dependencies

The project relies on the following libraries and frameworks:

- **Streamlit**: For building the interactive web application.
- **dotenv**: For loading environment variables.
- **PyPDF2**: For extracting text from PDF documents.
- **langchain**: A custom library for text processing and conversation management.
- **Hugging Face Transformers**: For language modeling and conversational responses.
- **faiss**: For creating and querying vector indexes efficiently.

## Installation

To run the application locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your environment variables, including your Hugging Face API token.
4. Run the application using `streamlit run main.py`.

## Usage

1. Upload your PDF documents using the file uploader provided.
2. Click on the "Process" button to initiate the processing of the uploaded documents.
3. Enter your question in the text input field and press Enter.
4. The system will provide responses based on the content of the uploaded PDFs.

## Contributors

- FrabricOfDreams (https://github.com/fabricofdreams) - Project Lead & Developer

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
