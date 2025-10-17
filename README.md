# 💳 Fraudulent Transaction Classifier

A deep learning project to detect abnormal financial transactions using TensorFlow and Flask.

## 🚀 Features
- Detects fraudulent vs legitimate transactions
- Achieved **99.5% accuracy** on the Credit Card Fraud dataset
- Flask web app for real-time predictions
- REST API for programmatic access

## 🧠 Tech Stack
- Python, TensorFlow, Scikit-learn
- Flask (Backend)
- HTML/CSS (Frontend)

## ⚙️ How to Run
```bash
git clone https://github.com/<KomaliG7>/FraudulentTransactionClassifier.git
cd FraudulentTransactionClassifier
pip install -r requirements.txt
python app.py


Then open http://127.0.0.1:5000/ in your browser.

📊 Model Details

Dataset: Credit Card Fraud Detection (Kaggle)

Class Imbalance handled using SMOTE

Architecture: Fully connected deep neural network

Optimizer: Adam | Loss: Binary Crossentropy

📸 Screenshots

"Fraudulent Transaction Classifier\Output Screenshots"

## 📂 Dataset

This project uses the **Credit Card Fraud Detection** dataset from Kaggle:

**Dataset link:** [https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

**Instructions to download:**
1. Go to the Kaggle link above and download `creditcard.csv`.
2. Place `creditcard.csv` in the root folder of this project (same folder as `app.py`).

After that, the project can be run as described in the usage section.
