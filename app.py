import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()

    st.set_page_config(page_title='Multiple PDF Chat',
                       page_icon='🦄', layout='wide')
    st.header('Chat with multiple PDFs 🦄')
    st.text_input('Ask a question about your documents:')

    with st.sidebar:
        st.subheader('Your documents:')
        st.file_uploader('Upload your PDFs here and click on Process')
        st.button('Process')


if __name__ == '__main__':
    main()