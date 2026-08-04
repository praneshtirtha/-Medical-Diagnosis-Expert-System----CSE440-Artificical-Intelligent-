import streamlit as st
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Medical Diagnosis Expert System",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🩺 Medical Diagnosis Expert System")
st.markdown("### AI-Based Disease Prediction from Symptoms")

st.divider()

# =====================================================
# Patient Information Section
# =====================================================

st.header("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

st.divider()

# =====================================================
# Load Symptoms
# =====================================================

try:
    symptom_columns = joblib.load("model/symptom_columns.pkl")

except Exception as e:
    st.error(f"Unable to load symptom_columns.pkl\n\n{e}")
    st.stop()

# =====================================================
# Symptom Selection
# =====================================================

st.header("🤒 Symptom Selection")

selected_symptoms = st.multiselect(
    "Select Symptoms",
    options=sorted(symptom_columns)
)

st.divider()

# =====================================================
# Show Selected Information
# =====================================================

if st.button("Next"):

    if patient_name == "":
        st.warning("Please enter patient name.")

    elif len(selected_symptoms) == 0:
        st.warning("Please select at least one symptom.")

    else:

        st.success("Information Saved Successfully!")

        st.subheader("Patient Summary")

        st.write(f"**Patient Name:** {patient_name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")

        st.subheader("Selected Symptoms")

        for symptom in selected_symptoms:
            st.write(f"✅ {symptom}")

        # Save data for next page
        st.session_state["patient_name"] = patient_name
        st.session_state["age"] = age
        st.session_state["gender"] = gender
        st.session_state["selected_symptoms"] = selected_symptoms

        st.info("Ready for Disease Prediction.")