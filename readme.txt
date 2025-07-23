# CT_Scan

A Streamlit web application that predicts chest cancer types — **adenocarcinoma**, **large cell carcinoma**, **squamous cell carcinoma**, and **normal** — from CT scan images using a trained machine learning model.

---

## Folder Structure

CT_Scan/
│
├── img(Small sample CT scan images for testing)
│
│
├── model.pt # Trained machine learning model file(this file and images 
│  are provided in google drive. scroll down for link)
│
|
|── 1_read_imgs.ipynb # Notebook to load and convert images to dataframe
│── 2_Preprocessing.ipynb # Notebook for data preprocessing
│── 3_model_train.ipynb # Notebook to train the model
│
├── app.py # Streamlit app main script
├──.ipynb_checkpoints # this is a auto generated jupyter notebook folder
└── README.md # This file



---

## Getting Started

### Prerequisites

- Python 3.7+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
Download Large Files
Due to GitHub file size limits, the full dataset and trained model are hosted externally.

CT Scan Images: Download the dataset from Google Drive - Images and extract/place them inside the data/ folder.

Trained Model: Download the trained model file from Google Drive - Model and place it inside the models/ folder.

Running the App
Run the Streamlit app with:

streamlit run app.py
Open the URL shown in your browser to upload CT scan images and get predictions on chest cancer types.

Project Overview
This project includes:

Loading and converting CT scan images into a dataframe.

Preprocessing images for model input.

Training a classification model to predict chest cancer types.

A Streamlit-based interactive web app for prediction.

License
[Add your license info here]

Contact
[Aaryan Khadka] — [rnkhadka18@gmail.com]
[https://github.com/Aaryan012]


---

https://drive.google.com/drive/folders/1dyGPOWZH7dT878GWQV1yp5atfwQH30Ro?usp=sharing

You can download images and model.pt file from above drive.