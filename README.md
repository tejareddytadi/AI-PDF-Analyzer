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

# Usage
Running the Application
Step 1: Run the Colab Notebook
Open the Colab notebook:
Upload the provided Colab notebook (colab_notebook.ipynb) to your Google Colab account.

Run the cells in the notebook:
Execute each cell in the notebook sequentially to set up the environment, load the models, and process the PDF documents.

Prepare the documents:
Ensure the PDF documents are properly uploaded and processed in the notebook. This will generate the necessary embeddings and allow you to test the model.

Step 2: Run the Streamlit App
Upload appnew.py to Colab:
After running the Colab notebook, upload the appnew.py file to your Google Colab environment.

Now run the lasst cell in colab file (streamlit cell), Once the Streamlit app is running, follow the link provided by Localtunnel (e.g., https://your-subdomain.loca.lt) to access the app in your browser.

# Example Interface
Here is an example of what the interface looks like:

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
