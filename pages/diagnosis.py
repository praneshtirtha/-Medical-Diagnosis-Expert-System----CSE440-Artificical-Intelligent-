import streamlit as st
import joblib


# ============================================================
# Page Setup
# ============================================================

st.set_page_config(
    page_title="Diagnosis",
    page_icon="✦",
    layout="wide"
)


# ============================================================
# Load Symptom Columns
# ============================================================

SYMPTOM_COLUMNS_PATH = "model/symptom_columns.pkl"


@st.cache_resource
def load_symptom_columns():
    """
    Loads symptom column names used during model training.
    """
    return joblib.load(SYMPTOM_COLUMNS_PATH)


symptom_columns = load_symptom_columns()


# ============================================================
# Session State
# ============================================================

if "diagnosis_step" not in st.session_state:
    st.session_state.diagnosis_step = "user_input"

if "patient_name" not in st.session_state:
    st.session_state.patient_name = ""

if "age" not in st.session_state:
    st.session_state.age = 18

if "gender" not in st.session_state:
    st.session_state.gender = "Male"

# Optional field. User can leave this empty.
if "contact_info" not in st.session_state:
    st.session_state.contact_info = ""

if "selected_symptoms" not in st.session_state:
    st.session_state.selected_symptoms = []


# ============================================================
# Helper Functions
# ============================================================

def go_to_step(step_name):
    """
    Moves between patient information and symptom selection.
    """
    st.session_state.diagnosis_step = step_name
    st.rerun()


def readable_symptom(symptom):
    """
    Example: high_fever -> High Fever
    """
    return symptom.replace("_", " ").title()


def original_symptom(readable):
    """
    Example: High Fever -> high_fever
    """
    return readable.lower().replace(" ", "_")


# ============================================================
# CSS Design
# ============================================================

st.html("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stHeader"] {
    background: rgba(7, 17, 31, 0.85);
    height: 55px;
}

.stApp {
    background:
        radial-gradient(circle at 10% 15%, rgba(77, 208, 225, 0.35), transparent 28%),
        radial-gradient(circle at 85% 20%, rgba(129, 199, 132, 0.28), transparent 30%),
        radial-gradient(circle at 50% 90%, rgba(126, 87, 194, 0.35), transparent 35%),
        linear-gradient(135deg, #07111f 0%, #0b1f3a 42%, #12395b 100%);
    color: #ffffff;
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1120px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}

.header-card {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    background:
        linear-gradient(135deg, rgba(6, 26, 64, 0.95), rgba(9, 47, 93, 0.92)),
        radial-gradient(circle at 15% 20%, rgba(0, 198, 255, 0.35), transparent 28%),
        radial-gradient(circle at 85% 75%, rgba(22, 219, 147, 0.30), transparent 30%);
    padding: 34px 38px;
    border-radius: 30px;
    border: 1px solid rgba(255,255,255,0.22);
    box-shadow: 0px 20px 55px rgba(0,0,0,0.42);
    margin-bottom: 28px;
    text-align: center;
    animation: fadeUp 0.8s ease;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0px); }
}

.section-title {
    font-size: 44px;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 10px;
    text-shadow: 0px 7px 20px rgba(0,0,0,0.45);
}

.page-subtitle {
    color: #c9f7ff;
    font-size: 18px;
    line-height: 1.7;
}

.step-pill {
    display: inline-block;
    margin-top: 18px;
    padding: 10px 18px;
    border-radius: 999px;
    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.25);
    color: #ffffff;
    font-weight: 800;
}

.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stMultiSelect label,
.stTextArea label {
    color: white !important;
    font-weight: 800 !important;
    font-size: 16px !important;
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: rgba(255,255,255,0.96) !important;
    color: #061a40 !important;
    border: 2px solid #8fd6ff !important;
    border-radius: 14px !important;
    padding: 12px !important;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15) !important;
}

div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.96) !important;
    color: #061a40 !important;
    border: 2px solid #8fd6ff !important;
    border-radius: 14px !important;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15) !important;
}

div[data-baseweb="select"] span {
    color: #061a40 !important;
}

ul[role="listbox"] {
    background-color: white !important;
}

ul[role="listbox"] li {
    color: #061a40 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #16db93, #00c6ff) !important;
    color: #061a40 !important;
    border: 2px solid rgba(255,255,255,0.9) !important;
    border-radius: 18px !important;
    font-size: 17px !important;
    font-weight: 850 !important;
    padding: 0.85rem 1rem !important;
    box-shadow: 0px 12px 30px rgba(0, 198, 255, 0.25) !important;
    transition: all 0.25s ease-in-out !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ffffff, #e7fbff) !important;
    color: #07111f !important;
    border: 2px solid #16db93 !important;
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0px 18px 40px rgba(255,255,255,0.25) !important;
}

.home-link {
    text-decoration: none !important;
    display: block;
    text-align: center;
    background: linear-gradient(135deg, #16db93, #00c6ff);
    color: #061a40 !important;
    border: 2px solid rgba(255,255,255,0.9);
    border-radius: 18px;
    font-size: 17px;
    font-weight: 850;
    padding: 14px 18px;
    box-shadow: 0px 12px 30px rgba(0, 198, 255, 0.25);
    transition: all 0.25s ease-in-out;
}

.home-link:hover {
    background: linear-gradient(135deg, #ffffff, #e7fbff);
    color: #07111f !important;
    border: 2px solid #16db93;
    transform: translateY(-4px) scale(1.02);
}

hr {
    border: none;
    height: 1px;
    background: rgba(255,255,255,0.25);
    margin: 28px 0;
}

.stAlert {
    border-radius: 16px !important;
}
</style>
""")


# ============================================================
# Step 1: Patient Information
# ============================================================

if st.session_state.diagnosis_step == "user_input":

    st.html("""
    <div class="header-card">
        <div class="section-title">Patient Information</div>
        <div class="page-subtitle">
            Enter basic patient information before moving to symptom selection.
        </div>
        <div class="step-pill">Step 1 of 2 · Patient Details</div>
    </div>
    """)

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
            value=int(st.session_state.age),
            step=1
        )

    with col3:
        st.session_state.gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"],
            index=["Male", "Female", "Other"].index(st.session_state.gender)
        )

    # Optional contact field
    st.session_state.contact_info = st.text_input(
        "Contact Number or Email (Optional)",
        value=st.session_state.contact_info,
        placeholder="Example: 01XXXXXXXXX or example@email.com"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.html('<a class="home-link" href="/" target="_self">Back To Main Page</a>')

    with col2:
        if st.button("Continue To Symptoms", use_container_width=True):
            go_to_step("symptoms")


# ============================================================
# Step 2: Symptom Selection
# ============================================================

elif st.session_state.diagnosis_step == "symptoms":

    st.html("""
    <div class="header-card">
        <div class="section-title">Symptom Selection</div>
        <div class="page-subtitle">
            Select symptoms from the list. You can also type symptoms manually using commas.
        </div>
        <div class="step-pill">Step 2 of 2 · Symptom Analysis</div>
    </div>
    """)

    readable_symptoms = [readable_symptom(symptom) for symptom in symptom_columns]
    readable_to_original = {
        readable_symptom(symptom).lower(): symptom for symptom in symptom_columns
    }

    selected_readable = st.multiselect(
        "Select symptoms",
        readable_symptoms
    )

    typed_symptoms = st.text_area(
        "Write symptoms manually",
        placeholder="Example: fever, headache, vomiting"
    )

    selected_original = [original_symptom(symptom) for symptom in selected_readable]

    if typed_symptoms.strip() != "":
        typed_list = [item.strip().lower() for item in typed_symptoms.split(",")]

        for typed in typed_list:
            typed_clean = typed.replace(" ", "_")

            if typed_clean in symptom_columns:
                selected_original.append(typed_clean)
            elif typed in readable_to_original:
                selected_original.append(readable_to_original[typed])

    selected_original = list(set(selected_original))
    st.session_state.selected_symptoms = selected_original

    if len(selected_original) > 0:
        st.success(
            "Selected Symptoms: "
            + ", ".join([readable_symptom(s) for s in selected_original])
        )
    else:
        st.warning("No symptoms selected yet.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back To Patient Info", use_container_width=True):
            go_to_step("user_input")

    with col2:
        if st.button("Predict Disease", use_container_width=True):
            if len(st.session_state.selected_symptoms) == 0:
                st.error("Please select or type at least one valid symptom.")
            else:
                st.switch_page("pages/result.py")