# 🏦 Loan Approval Prediction System

## 📌 Project Overview

This project is an end-to-end Machine Learning application that predicts whether a loan application is likely to be approved based on applicant and financial information.

The project demonstrates a complete machine learning workflow, including data preprocessing, feature engineering, exploratory data analysis (EDA), categorical encoding, feature scaling, model training, model comparison, evaluation, and deployment.

Multiple classification algorithms were trained and evaluated to identify the best-performing model. Based on the evaluation results, **LightGBM** achieved the highest accuracy of **97.84%** and was selected as the final model for the deployed application.

The trained model is integrated into an interactive **Streamlit web application** that allows users to enter applicant information and receive real-time loan approval predictions.

🚀 **Live Application:**  
https://loan-prediction-app-apg4dln7fdto45kare37gg.streamlit.app/

💻 **GitHub Repository:**  
https://github.com/ARAGALAGOVARDHANREDDY/loan-prediction-app

---

## 🎯 Objectives

- Clean and preprocess the loan application dataset.
- Handle missing values and prepare data for machine learning.
- Perform exploratory data analysis (EDA).
- Encode categorical features into numerical representations.
- Apply feature scaling where required.
- Train multiple machine learning classification models.
- Compare model performance using multiple evaluation metrics.
- Select the best-performing machine learning model.
- Save the trained model and preprocessing objects.
- Build an interactive Streamlit web application.
- Deploy the machine learning application online.

---

## 📂 Dataset

**Dataset:** Loan Prediction Dataset from Kaggle

The dataset contains information about loan applicants and their personal, financial, and loan-related details.

### Features

The project uses applicant and loan-related information such as:

- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Education
- Employment / Self-Employment Status
- Property Area
- Other applicant-related attributes

### Target Variable

- Loan Approval Status

The data was preprocessed and transformed before being used to train the machine learning models.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Data Analysis & Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- LightGBM
- XGBoost

### Model Serialization

- Joblib
- Pickle

### Web Application

- Streamlit

### Development Environment

- Jupyter Notebook

### Deployment

- Streamlit Community Cloud

---

## 📊 Project Workflow

### 1. Data Loading

- Load the Kaggle Loan Prediction Dataset.
- Explore the dataset structure.
- Analyze feature types and target variables.

### 2. Data Preprocessing

- Handle missing values.
- Clean and prepare the dataset.
- Separate input features and target variable.

### 3. Exploratory Data Analysis (EDA)

- Analyze feature distributions.
- Study relationships between applicant information and loan approval.
- Understand patterns in the dataset.

### 4. Feature Engineering

- Prepare relevant applicant and loan-related features.
- Transform features into a format suitable for machine learning.

### 5. Feature Encoding

- Encode categorical variables.
- Save encoders for use during application prediction.

### 6. Feature Scaling

- Apply feature scaling where required.
- Save the scaler for consistent preprocessing during inference.

### 7. Model Training

Multiple classification algorithms were trained and evaluated:

- LightGBM
- XGBoost
- Random Forest
- Decision Tree
- AdaBoost
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- Logistic Regression
- K-Nearest Neighbors (KNN)

### 8. Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

### 9. Best Model Selection

Based on the model comparison results, **LightGBM** achieved the highest accuracy of **97.84%**.

### 10. Model Deployment

The selected model and preprocessing objects were saved and integrated into a Streamlit application.

The application was then deployed using **Streamlit Community Cloud**.

---

## 🏆 Model Comparison

Multiple machine learning classification algorithms were compared to identify the best-performing model.

| Rank | Model | Accuracy | Precision | Recall | F1 Score |
|------|-------|---------:|----------:|-------:|---------:|
| 🥇 1 | **LightGBM** | **97.84%** | **98.05%** | **97.46%** | **97.15%** |
| 🥈 2 | XGBoost | 97.72% | 96.55% | 97.46% | 96.99% |
| 🥉 3 | Random Forest | 97.49% | 96.82% | 96.51% | 96.66% |
| 4 | Decision Tree | 96.41% | 95.24% | 95.24% | 95.24% |
| 5 | AdaBoost | 96.41% | 94.39% | 96.19% | 95.28% |
| 6 | SVM | 94.74% | 93.02% | 93.02% | 93.02% |
| 7 | Logistic Regression | 91.75% | 89.42% | 88.57% | 88.99% |
| 8 | KNN | 89.47% | 86.03% | 86.03% | 86.03% |
| 9 | Gaussian Naive Bayes | 77.39% | 90.38% | 44.76% | 59.87% |

---

## 📈 Best Model Performance

### 🥇 Selected Model: LightGBM

LightGBM achieved the best overall accuracy among the evaluated classification models.

| Metric | Score |
|--------|------:|
| Accuracy | **97.84%** |
| Precision | **98.05%** |
| Recall | **97.46%** |
| F1 Score | **97.15%** |

Based on the evaluation results, **LightGBM was selected as the final model** for the loan approval prediction application.

> **Note:** Model performance may vary depending on the dataset split, preprocessing techniques, and evaluation methodology.

---

## 📸 Application Screenshots

### 🏠 Home Page

The application provides an interactive Streamlit interface where users can enter applicant and financial information.

![Loan Prediction App Home Page](image/home.png)

### 🔮 Loan Prediction Result

After submitting the required applicant information, the application generates a loan approval prediction.

![Loan Prediction Result](image/prediction.png)

---

## 📂 Project Structure

```text
loan-prediction-app/
│
├── app.py
│
├── loan_approval_model.pkl
├── scaler.pkl
├── education_encoder.pkl
├── employment_encoder.pkl
├── status_encoder.pkl
├── columns.json
│
├── loan_prediction_analysis.ipynb
├── requirements.txt
│
├── image/
│   ├── home.png
│   └── prediction.png
│
└── README.md
