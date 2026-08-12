import streamlit as st

st.set_page_config(page_title="About System", page_icon="ℹ️", layout="wide")

st.title("About the Medical Diagnosis Expert System")
st.markdown(
    "This Streamlit app predicts possible diseases from selected symptoms using a trained Random Forest model. "
    "It is designed as a simple diagnosis assistant for demonstration purposes, not a medical substitute."
)

st.markdown("---")

st.header("How It Works")
st.markdown(
    "1. Enter patient details on the Diagnosis page.\n"
    "2. Select one or more symptoms from the symptom list.\n"
    "3. View the Random Forest prediction and recommended precautions.\n"
    "4. Download a report if needed."
)

st.header("Model")
st.markdown(
    "The app uses the trained Random Forest model saved in `model/random_forest_model.pkl`. "
    "The symptom feature columns are loaded from `model/symptom_columns.pkl`."
)

st.header("Project Team")
st.write("- Pranesh Majumder Tirtha — 2222899042")
st.write("- Mahfuzur Rahman — 2221827042")
st.write("- Nabila Nusrat — 2012394642")
st.write("- Nahian Islam Inan — 2112259642")

st.markdown("---")

st.markdown("[Go to Diagnosis](/diagnosis)")
