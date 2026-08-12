import streamlit as st
import joblib

st.set_page_config(page_title="Diagnosis", page_icon="🩺", layout="wide")

SYMPTOM_COLUMNS_PATH = "model/symptom_columns.pkl"

@st.cache_resource
def load_symptom_columns():
    return joblib.load(SYMPTOM_COLUMNS_PATH)

symptom_columns = load_symptom_columns()

if "diagnosis_step" not in st.session_state:
    st.session_state.diagnosis_step = "user_input"

if "patient_name" not in st.session_state:
    st.session_state.patient_name = ""

if "age" not in st.session_state:
    st.session_state.age = 25

if "gender" not in st.session_state:
    st.session_state.gender = "Male"

if "contact_info" not in st.session_state:
    st.session_state.contact_info = ""

if "selected_symptoms" not in st.session_state:
    st.session_state.selected_symptoms = []


def readable_symptom(symptom: str) -> str:
    return symptom.replace("_", " ").title()


def original_symptom(readable: str) -> str:
    return readable.lower().replace(" ", "_")


def go_to_step(step_name: str):
    st.session_state.diagnosis_step = step_name
    st.rerun()

st.title("🩺 Symptom-Based Diagnosis")
st.write("Use the form below to enter patient information and select symptoms for prediction.")
st.markdown("---")

if st.session_state.diagnosis_step == "user_input":
    st.subheader("1. Patient Information")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.patient_name = st.text_input(
            "Patient Name",
            value=st.session_state.patient_name
        )

    with col2:
        st.session_state.age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=int(st.session_state.age)
        )

    with col3:
        st.session_state.gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"],
            index=["Male", "Female", "Other"].index(st.session_state.gender)
        )

    st.text_input(
        "Contact Info (Optional)",
        value=st.session_state.contact_info,
        key="contact_info_input"
    )

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("[Home](/)")

    with col2:
        if st.button("Continue to Symptom Selection"):
            if st.session_state.patient_name.strip() == "":
                st.warning("Please enter the patient name before continuing.")
            else:
                go_to_step("symptoms")

else:
    st.subheader("2. Symptom Selection")
    readable_symptoms = [readable_symptom(symptom) for symptom in symptom_columns]
    mapping = {readable_symptom(symptom).lower(): symptom for symptom in symptom_columns}

    selected_readable = st.multiselect(
        "Select Symptoms",
        options=sorted(readable_symptoms),
        default=[readable_symptom(symptom) for symptom in st.session_state.selected_symptoms]
    )

    manual_input = st.text_area(
        "Or enter symptoms manually (comma-separated)",
        placeholder="fever, headache, vomiting"
    )

    selected_original = [original_symptom(symptom) for symptom in selected_readable]
    if manual_input.strip() != "":
        for item in manual_input.split(","):
            value = item.strip().lower()
            if not value:
                continue
            if value in mapping:
                selected_original.append(mapping[value])
            else:
                selected_original.append(original_symptom(value))

    selected_original = [sym for sym in dict.fromkeys(selected_original) if sym in symptom_columns]
    st.session_state.selected_symptoms = selected_original

    if selected_original:
        st.success("Selected symptoms saved.")
        st.markdown("**Symptoms:** " + ", ".join([readable_symptom(sym) for sym in selected_original]))
    else:
        st.info("No symptoms selected yet.")

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back to Patient Info"):
            go_to_step("user_input")

    with col2:
        if st.button("Open Results"):
            if len(st.session_state.selected_symptoms) == 0:
                st.error("Please select at least one symptom before prediction.")
            else:
                st.switch_page("pages/result.py")

    if len(st.session_state.selected_symptoms) > 0:
        st.info("Ready to predict. Click **Open Results** above to see your prediction.")
