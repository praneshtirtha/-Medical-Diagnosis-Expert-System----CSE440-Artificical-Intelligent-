import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# Prediction 2 File
# Model: SVM
# Purpose: Second-priority prediction
# ============================================================

SVM_MODEL_PATH = "model/svm_model.pkl"
SYMPTOM_COLUMNS_PATH = "model/symptom_columns.pkl"
PRECAUTION_PATH = "dataset/disease_precautions_cleaned.csv"


@st.cache_resource
def load_prediction2_files():
    """
    Loads SVM model and symptom column names.
    """
    svm_model = joblib.load(SVM_MODEL_PATH)
    symptom_columns = joblib.load(SYMPTOM_COLUMNS_PATH)
    return svm_model, symptom_columns


@st.cache_data
def load_precaution_file_prediction2():
    """
    Loads disease precaution dataset.
    """
    return pd.read_csv(PRECAUTION_PATH)


svm_model, symptom_columns = load_prediction2_files()
precaution_data = load_precaution_file_prediction2()


def get_precautions(disease_name):
    """
    Finds precautions for predicted disease.
    """
    matched_row = precaution_data[
        precaution_data["Disease"].astype(str).str.lower().str.strip()
        == disease_name.lower().strip()
    ]

    if matched_row.empty:
        return ["No precautions found for this disease."]

    precautions = []

    for col in matched_row.columns:
        if col.lower() != "disease":
            value = matched_row.iloc[0][col]
            if pd.notna(value) and str(value).strip() != "":
                precautions.append(str(value).strip())

    if len(precautions) == 0:
        return ["No precautions found for this disease."]

    return precautions


def create_input_dataframe(selected_symptoms):
    """
    Converts selected symptoms into 0/1 input format.
    """
    input_data = np.zeros(len(symptom_columns))

    for symptom in selected_symptoms:
        if symptom in symptom_columns:
            index = symptom_columns.index(symptom)
            input_data[index] = 1

    input_df = pd.DataFrame([input_data], columns=symptom_columns)
    return input_df


def get_prediction2(selected_symptoms):
    """
    Final function for Prediction 2.
    Uses SVM model.
    """
    input_df = create_input_dataframe(selected_symptoms)

    disease = svm_model.predict(input_df)[0]

    confidence = 0.0

    # Best case: SVM was trained with probability=True
    if hasattr(svm_model, "predict_proba"):
        probabilities = svm_model.predict_proba(input_df)[0]
        confidence = np.max(probabilities) * 100

    # Backup case: if SVM does not have predict_proba()
    elif hasattr(svm_model, "decision_function"):
        scores = svm_model.decision_function(input_df)

        if scores.ndim == 1:
            score_array = np.array(scores)
        else:
            score_array = scores[0]

        exp_scores = np.exp(score_array - np.max(score_array))
        probabilities = exp_scores / exp_scores.sum()
        confidence = np.max(probabilities) * 100

    precautions = get_precautions(disease)

    return {
        "disease": disease,
        "confidence": confidence,
        "precautions": precautions
    }