import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# Prediction 1 File
# Model: Random Forest
# Purpose: Main / most important prediction
# ============================================================

RF_MODEL_PATH = "model/random_forest_model.pkl"
SYMPTOM_COLUMNS_PATH = "model/symptom_columns.pkl"
PRECAUTION_PATH = "dataset/disease_precautions_cleaned.csv"


@st.cache_resource
def load_prediction1_files():
    """
    Loads Random Forest model and symptom column names.
    """
    rf_model = joblib.load(RF_MODEL_PATH)
    symptom_columns = joblib.load(SYMPTOM_COLUMNS_PATH)
    return rf_model, symptom_columns


@st.cache_data
def load_precaution_file_prediction1():
    """
    Loads disease precaution dataset.
    """
    return pd.read_csv(PRECAUTION_PATH)


rf_model, symptom_columns = load_prediction1_files()
precaution_data = load_precaution_file_prediction1()


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


def get_prediction1(selected_symptoms):
    """
    Final function for Prediction 1.
    Uses Random Forest model.
    """
    input_df = create_input_dataframe(selected_symptoms)

    disease = rf_model.predict(input_df)[0]

    confidence = 0.0
    if hasattr(rf_model, "predict_proba"):
        probabilities = rf_model.predict_proba(input_df)[0]
        confidence = np.max(probabilities) * 100

    precautions = get_precautions(disease)

    return {
        "disease": disease,
        "confidence": confidence,
        "precautions": precautions
    }