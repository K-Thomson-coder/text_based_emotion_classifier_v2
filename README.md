\# Emotion Detection using Machine Learning



This project focuses on building an emotion classifier using different machine learning algorithms. It compares four models and uses the best-performing one to create a simple user interface (UI).



\## 📁 Folder Structure



Each folder under notebook/ contains:

\- A Jupyter notebook used for training and testing

\- The saved model file (.pkl)

\- The corresponding vectorizer file (.pkl)



\### 🔍 Models Implemented

1\. Logistic Regression  

2\. LinearSVC  

3\. Multinomial Naive Bayes  

4\. K-Nearest Neighbors (KNN)



\## 🏆 Final Model for UI

The \*LinearSVC\* model gave the best accuracy and was used to build the UI.



\## 🚀 How to Use

\- Open any notebook (e.g., Emotion\_Classifier\_1.ipynb) inside the respective model folder.

\- The model and vectorizer are loaded from .pkl files.

\- You can input any text to predict the emotion.



\## 📦 Example Folder: 1\_LogisticRegression/

1\_model\_lr.pkl             <- Trained Logistic Regression model

1\_vectorizer\_lr.pkl        <- Fitted TF-IDF Vectorizer

Emotion\_Classifier\_1.ipynb <- Notebook with code and evaluation



---



\## 📂 How to Use the Emotion Analyzer UI



The main interface is built using \*Streamlit\* and can be launched with a simple command:



```bash

streamlit run Emotion\_Analyzer.py



What it does:



Takes a user input sentence through a textbox.



Internally cleans the text and loads the trained model/vectorizer.



Displays the predicted emotion on screen in real-time.





Make sure the required model and vectorizer files are stored inside the appropriate folder before running the app.





---



🛠 Scripts



utils.py



This script includes helper functions used by the main UI app:



save\_file(file\_name, file)

Saves any given file object (like a model or vectorizer) to disk.



load\_file(file\_name)

Loads a saved file from the specified path (used to load model and vectorizer).



clean(text)

Preprocesses raw input text by removing special characters, converting to lowercase, etc., to ensure consistent input to the model.





Keeping these functions modular makes the main UI script cleaner and easier to manage.





---



🧠 Data and Model



The project uses a labeled dataset containing text entries and their corresponding emotional labels (e.g., joy, anger, fear).



All models were trained on this dataset.



Only the LinearSVC model — which gave the best accuracy — was saved and connected to the UI.





Make sure the model and vectorizer files are placed in the correct folder before launching the UI.

