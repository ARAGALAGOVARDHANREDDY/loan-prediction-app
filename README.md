# 🏦 Loan Approval Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn)
![LightGBM](https://img.shields.io/badge/LightGBM-Gradient%20Boosting-green)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-red)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

# 📌 Overview

The **Loan Approval Prediction System** is an end-to-end Machine Learning application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant information and financial attributes.

This project demonstrates the complete machine learning lifecycle, including:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Categorical Encoding
- Feature Scaling
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Model Comparison
- Model Deployment

A total of **9 Machine Learning algorithms** were trained and compared. After evaluating each model using multiple performance metrics, **LightGBM** achieved the best overall performance with an accuracy of **97.84%** and was selected for deployment.

---

# 🚀 Live Demo

### 🌐 Streamlit Application

**https://loan-prediction-app-apg4dln7fdto45kare37gg.streamlit.app/**

---

# 💻 GitHub Repository

**https://github.com/ARAGALAGOVARDHANREDDY/loan-prediction-app**

---

# 🎯 Problem Statement

Financial institutions receive thousands of loan applications every day. Evaluating each application manually is time-consuming and may introduce inconsistencies.

The objective of this project is to develop a machine learning model capable of predicting loan approval decisions using historical applicant data, helping streamline the loan screening process.

---

# ✨ Key Features

- End-to-End Machine Learning Pipeline
- Comprehensive Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Categorical Encoding
- Feature Scaling
- Hyperparameter Tuning
- Comparison of 9 Classification Algorithms
- High Accuracy Prediction Model
- Interactive Streamlit Web Application
- Real-Time Loan Prediction
- Cloud Deployment using Streamlit Community Cloud

---

# 📂 Dataset

**Source:** Kaggle Loan Prediction Dataset

The dataset contains applicant demographic, financial, and loan-related information.

## Input Features

- Number of Dependents
- Education
- Employment Status
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area

## Target Variable

- Loan Status
  - Approved
  - Rejected

---

# ⚙️ Machine Learning Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Missing Value Handling
   │
   ▼
EDA
   │
   ▼
Feature Engineering
   │
   ▼
Encoding
   │
   ▼
Feature Scaling
   │
   ▼
Train-Test Split
   │
   ▼
Model Training
   │
   ▼
Hyperparameter Tuning
   │
   ▼
Model Evaluation
   │
   ▼
Best Model Selection
   │
   ▼
Model Deployment
```

---

# 🛠️ Technologies Used

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Machine Learning

- Scikit-learn
- LightGBM
- XGBoost

## Model Serialization

- Pickle
- Joblib

## Web Framework

- Streamlit

## IDE

- Jupyter Notebook

## Deployment

- Streamlit Community Cloud

---

# 📊 Exploratory Data Analysis

The dataset was analyzed to understand:

- Feature distributions
- Missing values
- Class distribution
- Correlation between variables
- Loan approval trends
- Credit history impact
- Income distribution
- Property area comparison

EDA helped identify important features contributing to loan approval decisions.

---

# ⚡ Data Preprocessing

The preprocessing pipeline included:

- Missing value treatment
- Categorical encoding
- Feature engineering
- Data normalization
- Feature scaling
- Train-Test Split

Saved preprocessing objects include:

- scaler.pkl
- education_encoder.pkl
- employment_encoder.pkl
- status_encoder.pkl

---

# 🤖 Machine Learning Models

The following algorithms were trained and evaluated:

| Model |
|---------|
| LightGBM |
| XGBoost |
| Random Forest |
| Decision Tree |
| AdaBoost |
| Support Vector Machine |
| Logistic Regression |
| K-Nearest Neighbors |
| Gaussian Naive Bayes |

---

# 🏆 Model Performance

| Rank | Model | Accuracy | Precision | Recall | F1 Score |
|------|-------|---------:|----------:|-------:|---------:|
| 🥇 | **LightGBM** | **97.84%** | **98.05%** | **97.46%** | **97.15%** |
| 🥈 | XGBoost | 97.72% | 96.55% | 97.46% | 96.99% |
| 🥉 | Random Forest | 97.49% | 96.82% | 96.51% | 96.66% |
| 4 | Decision Tree | 96.41% | 95.24% | 95.24% | 95.24% |
| 5 | AdaBoost | 96.41% | 94.39% | 96.19% | 95.28% |
| 6 | SVM | 94.74% | 93.02% | 93.02% | 93.02% |
| 7 | Logistic Regression | 91.75% | 89.42% | 88.57% | 88.99% |
| 8 | KNN | 89.47% | 86.03% | 86.03% | 86.03% |
| 9 | Gaussian Naive Bayes | 77.39% | 90.38% | 44.76% | 59.87% |

---

# 🥇 Final Model

## LightGBM Classifier

The LightGBM classifier achieved the highest performance among all tested models and was selected for deployment.

| Metric | Score |
|---------|-------:|
| Accuracy | **97.84%** |
| Precision | **98.05%** |
| Recall | **97.46%** |
| F1 Score | **97.15%** |

---

# 🌐 Web Application

The trained model has been deployed as an interactive Streamlit application where users can:

- Enter applicant information
- Submit loan details
- Receive instant loan approval prediction
- View prediction in real time

---

# 📸 Application Screenshots

## 🏠 Home Page

![Home](image/home.png)

---

## 🔮 Prediction Result

![Prediction](image/prediction.png)

---

# 📁 Project Structure

```
loan-prediction-app/
│
├── app.py
├── loan_prediction_analysis.ipynb
├── loan_approval_model.pkl
├── scaler.pkl
├── education_encoder.pkl
├── employment_encoder.pkl
├── status_encoder.pkl
├── columns.json
├── requirements.txt
├── README.md
│
├── image/
│   ├── home.png
│   └── prediction.png
│
└── .streamlit/
    └── config.toml
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ARAGALAGOVARDHANREDDY/loan-prediction-app.git
```

Move into the project directory

```bash
cd loan-prediction-app
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

- Deep Learning implementation
- Explainable AI using SHAP
- Model monitoring
- REST API deployment
- Docker containerization
- CI/CD pipeline
- Database integration
- User authentication
- Cloud deployment on AWS/Azure/GCP

---

# 👨‍💻 Author

**Aragala Govardhan Reddy**

📧 Email: aragalavishnu30@gmail.com

🔗 LinkedIn: https://linkedin.com/in/aragala-govardhan-reddy

💻 GitHub: https://github.com/ARAGALAGOVARDHANREDDY

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.

---

## 📄 License

This project is licensed under the MIT License.
