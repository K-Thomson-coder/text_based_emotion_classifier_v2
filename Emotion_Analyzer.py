import streamlit as st 
from scripts.utils import load_file, clean

model = load_file("notebook/2_LinearSVC/2_model_svc.pkl")
vectorizer = load_file("notebook/2_LinearSVC/2_vectorizer_svc.pkl")

labels = {0 : 'Fear', 1 : 'Anger', 2 : 'Joy'}

st.title("Text Emotion Analyzer")

user_input = st.text_area("Enter a sentence to analyze emotion.")

if st.button("ANALYZE") :
    clean_text = clean(user_input)
    vector_text = vectorizer.transform([clean_text])
    prediction = model.predict(vector_text)
    emotion = labels[prediction[0]]
    st.success(f"Predicted Emotion : {emotion}")