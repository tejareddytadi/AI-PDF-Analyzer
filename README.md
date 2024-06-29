# Ai-pdf-analyzer

This repository contains the code for an AI-powered application that allows users to upload PDF documents, extract and analyze their contents, and generate insights based on user queries. The project leverages state-of-the-art NLP models, including Sentence Transformers for document embedding and GPT-2 for generating human-readable insights.

# Datasets
The datasets used in this project include:

Google 10-K: The annual report of Alphabet Inc, detailing the company's financial performance, risk factors, and management's discussion and analysis.
Tesla 10-K: The annual report of Tesla Inc, providing insights into the company's operations, financial condition, and risks.
Uber 10-K: The annual report of Uber Technologies Inc, highlighting the company's business model, financial metrics, and potential risk factors.

# Setup and Installation
Requirements
Python 3.6+
Streamlit
PyPDF2
Sentence Transformers
Transformers (Hugging Face)
Localtunnel (optional for sharing the app publicly)

# Interacting with the Application
Upload PDF Files:
Use the file uploader to select and upload multiple PDF documents.

Enter Query:
Input your query in the text box provided and click "Analyze".

View Insights:
The application will display extracted text snippets, relevant content, and generated insights based on your query.

# Code Overview
appnew.py: The main application file for the Streamlit app.
ai-pdfanalyzer.ipynb: The original Colab notebook that demonstrates the functionality and serves as the basis for the Streamlit app.
