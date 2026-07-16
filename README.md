# Medical Diagnosis Expert System

**Course:** CSE 440 — Artificial Intelligence  
**Institution:** North South University  
**Semester:** Summer 2026  

## 👥 Group Members

| Name | Student ID |
|---|---|
| Pranesh Majumder Tirtha | 2222899042 |
| Mahfuzur Rahman | 2221827042 |
| Nabila Nusrat | 2012394642 |
| Nahian Islam Inan | 2112259642 |


## 📌 Project Overview

This project is a web-based **Medical Diagnosis Expert System** that predicts possible diseases based on selected symptoms. The system uses machine learning classification models trained on a disease-symptom dataset.

Users can select symptoms through the web interface, and the system predicts the most probable disease with a confidence score.

## 🎯 Objective

To develop an AI-based disease prediction system that can analyze selected symptoms and predict possible diseases using supervised machine learning models.

## ✨ Features

- Symptom selection
- Disease prediction
- Confidence score
- Basic precautions
- Simple web-based interface
- Multiple model comparison

## 📁 Dataset

The project uses:

- `DiseaseAndSymptoms.csv` — used for disease prediction
- `Disease precaution.csv` — used for precaution display

The disease-symptom dataset was preprocessed by converting symptoms into numerical **0/1 feature columns**, where:

- `1` = symptom is present
- `0` = symptom is absent

## 🤖 Machine Learning Models

The following models were trained and evaluated:

| Model | Accuracy | Sample Confidence Score |
|---|---:|---:|
| Decision Tree | 65.57% | 100% |
| Naive Bayes | 96.72% | 99.97% |
| Random Forest | 100% | 100% |
| SVM | 100% | 17.07% |
| XGBoost | 98% | 95% |

Based on the current results, **Random Forest** and **SVM** achieved the highest accuracy on the test dataset.

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- XGBoost
- Git & GitHub

## 🔄 System Workflow

```text
Dataset Preprocessing
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Symptom Selection
        ↓
Disease Prediction
        ↓
Confidence Score
        ↓
Precaution Display
```

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/praneshtirtha/-Medical-Diagnosis-Expert-System----CSE440-Artificical-Intelligent-.git
```

### Navigate to the Project Directory

```bash
cd -Medical-Diagnosis-Expert-System----CSE440-Artificical-Intelligent-
```

### Install Required Libraries

```bash
pip install pandas numpy scikit-learn joblib streamlit xgboost
```

### Train Models

```bash
python model/train_naive_bayes.py
python model/train_random_forest.py
python model/train_svm.py
python model/train_decision_tree.py
python model/train_xgboost.py
```

### Run the Web App

```bash
streamlit run app.py
```

## 📈 Current Progress

Dataset preprocessing has been completed, and all selected machine learning models have been trained and evaluated. Random Forest and SVM achieved the highest accuracy of **100%**, while XGBoost achieved **98%**, Naive Bayes achieved **96.72%**, and Decision Tree achieved **65.57%**.

## 📚 References

- Scikit-learn Documentation
- Streamlit Documentation
- Pandas Documentation
- XGBoost Documentation
- Disease-Symptom Dataset

## 📝 License

This project is developed for academic purposes as part of **CSE 440 — Artificial Intelligence** at **North South University**.
