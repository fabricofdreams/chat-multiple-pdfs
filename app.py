import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_text(pdf_docs):
    """
    Get the text from a PDF
    """
    text = ''
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(raw_text):
    """
    Split the text into small chunks
    """
    text_splitter = CharacterTextSplitter(
        separator='\n', chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(raw_text)
    return chunks


def main():
    load_dotenv()

    st.set_page_config(page_title='Multiple PDF Chat',
                       page_icon='🦄', layout='wide')
    st.header('Chat with multiple PDFs 🦄')
    st.text_input('Ask a question about your documents:')

    with st.sidebar:
        st.subheader('Your documents:')
        pdf_docs = st.file_uploader(
            'Upload your PDFs here and click on Process', accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing...'):
                # Get the PDFs content
                raw_text = get_pdf_text(pdf_docs)

                # Split content into small chunks
                text_chunks = get_text_chunks(raw_text)

                # Create embeddins for each chunk


if __name__ == '__main__':
    main()
