import streamlit as st
import PyPDF2
from sentence_transformers import SentenceTransformer
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import chromadb

# Extract text from PDFs
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Load and process PDFs (assuming PDFs are in the same directory)
alphabet_text = extract_text_from_pdf("/content/Alphabet_10-K.pdf")
tesla_text = extract_text_from_pdf("/content/Tesla_10-K.pdf")
uber_text = extract_text_from_pdf("/content/Uber_10-K.pdf")

# Generate embeddings using SentenceTransformers
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
alphabet_embeddings = model.encode(alphabet_text)
tesla_embeddings = model.encode(tesla_text)
uber_embeddings = model.encode(uber_text)

# Store embeddings in ChromaDB
client = chromadb.Client()
collection = client.create_collection("form_10k")

documents = [
    {"text": alphabet_text, "embedding": alphabet_embeddings},
    {"text": tesla_text, "embedding": tesla_embeddings},
    {"text": uber_text, "embedding": uber_embeddings}
]

for doc in documents:
    collection.insert_one(doc)

# Query vector store
def query_vector_store(query, top_k=3):
    query_embedding = model.encode(query)
    results = collection.query(query_embedding, top_k)
    return results

# Integrate LLM (GPT-2)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
llm_model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_insight(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = llm_model.generate(inputs, max_length=100, num_return_sequences=1)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Streamlit UI
def main():
    st.markdown("""
        <style>
        .main {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            color: #333;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1>Content Engine Chatbot</h1>", unsafe_allow_html=True)

    query = st.text_input("Enter your query:")

    if st.button("Get Insights"):
        if query:
            results = query_vector_store(query)
            st.write("Top Results:")
            for res in results:
                st.write(res["text"])
            
            insight = generate_insight(query)
            st.write("Generated Insight:")
            st.write(insight)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
