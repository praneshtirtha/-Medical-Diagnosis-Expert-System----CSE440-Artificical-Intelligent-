# Medical Diagnosis Expert System

**Course:** CSE 440 — Artificial Intelligence  
**Institution:** North South University  
**Semester:** Summer 2026  

---

## 👥 Group Members

| Name | Student ID |
|---|---|
| Pranesh Majumder Tirtha | 2222899042 |
| Mahfuzur Rahman | 2221827042 |
| Nabila Nusrat | 2012394642 |
| Nahian Islam Inan | 2112259642 |

---

## 📌 Project Overview

The **Medical Diagnosis Expert System** is a web-based artificial intelligence project that predicts possible diseases from patient symptoms.

Users can enter patient information, select symptoms, and receive two possible disease predictions with confidence scores and suggested precautions. The system also provides a report view and a downloadable prediction report.

This project is developed for academic and demonstration purposes only.

---

## 🎯 Objective

The objective of this project is to develop an AI-based disease prediction system that can analyze selected symptoms and predict possible diseases using supervised machine learning models.

---

## ✨ Main Features

- Patient information input
- Optional contact number or email input
- Symptom selection from a structured list
- Manual symptom input
- Two disease prediction results
- Confidence score for each prediction
- Suggested precautions
- Report view option
- Downloadable diagnosis report
- Medical disclaimer

---

## 📁 Dataset

The project uses two main datasets:

- `DiseaseAndSymptoms.csv` — used for disease prediction
- `Disease precaution.csv` — used for precaution display

The disease-symptom dataset was preprocessed by converting symptoms into numerical **0/1 feature columns**, where:

- `1` = symptom is present
- `0` = symptom is absent

The precaution dataset is used after prediction to display suggested precautions for the predicted diseases.

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

| Model | Accuracy | Sample Confidence Score |
|---|---:|---:|
| Decision Tree | 65.57% | 100% |
| Naive Bayes | 96.72% | 99.97% |
| Random Forest | 100% | 100% |
| SVM | 100% | 17.07% |
| XGBoost | 100% | 94.03% |

Based on the current results, **Random Forest** and **SVM** achieved the highest accuracy on the test dataset.

In the final web application:

| Prediction | Model Used |
|---|---|
| Prediction 1 | Random Forest |
| Prediction 2 | SVM |

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- XGBoost
- HTML/CSS
- Git & GitHub

---

## 🔄 System Workflow

```text
Dataset Preprocessing
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Patient Information Input
        ↓
Symptom Selection
        ↓
0/1 Symptom Encoding
        ↓
Disease Prediction
        ↓
Confidence Score
        ↓
Precaution Display
        ↓
Report View and Download
```

---

## 📂 Project Structure

```text
Medical-Diagnosis-Expert-System/
├── app.py
├── prediction1.py
├── prediction2.py
├── pages/
│   ├── about_us.py
│   ├── diagnosis.py
│   ├── how_it_works.py
│   └── result.py
├── model/
│   ├── random_forest_model.pkl
│   ├── svm_model.pkl
│   ├── symptom_columns.pkl
│   ├── train_decision_tree.py
│   ├── train_naive_bayes.py
│   ├── train_random_forest.py
│   ├── train_svm.py
│   └── train_xgboost.py
├── dataset/
│   ├── train_processed.csv
│   ├── test_processed.csv
│   ├── disease_precautions_cleaned.csv
│   ├── symptom_metadata.csv
│   └── disease_metadata.csv
├── report/
├── README.md
└── requirements.txt
```

---

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
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy scikit-learn joblib streamlit xgboost
```

---

## 🧠 Train Models

To train the machine learning models, run:

```bash
python model/train_naive_bayes.py
python model/train_random_forest.py
python model/train_svm.py
python model/train_decision_tree.py
python model/train_xgboost.py
```

---

## ▶️ Run the Web App

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

Then open the local URL shown in the terminal.

---

## 🖥 App Pages

The application includes the following pages:

| Page | Description |
|---|---|
| Landing Page | Main entry page of the system |
| About The System | Short project overview |
| How It Works | Explains the system workflow |
| Diagnosis Page | Collects patient details and symptoms |
| Result Page | Shows two predictions and report option |

---

## 📄 Report Feature

After prediction, the user can click **View Report** to see a full diagnosis report. The report includes:

- Patient name
- Age and gender
- Optional contact number or email
- Selected symptoms
- Two prediction results
- Confidence scores
- Suggested precautions
- Report ID
- Generated time
- Medical disclaimer

The report can also be downloaded as an HTML file and printed or saved as PDF from the browser.

---

## 📈 Current Progress

The project is almost complete. Dataset preprocessing, model training, model evaluation, Streamlit web interface, two-model prediction system, precaution display, and report generation features have been implemented.

Random Forest and SVM are used in the final application for Prediction 1 and Prediction 2.

---

## 📚 References

- Scikit-learn Documentation
- Streamlit Documentation
- Pandas Documentation
- NumPy Documentation
- XGBoost Documentation
- Disease-Symptom Dataset

---

## ⚠️ Disclaimer

This system is not a medical certificate or verified diagnosis tool. It does not replace consultation, examination, prescription, or treatment by a licensed physician.

This project is developed only for academic purposes as part of **CSE 440 — Artificial Intelligence** at **North South University**.

---

## 📝 License

This project is developed for academic purposes only.
