import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from html import escape
import re

from prediction1 import get_prediction1
from prediction2 import get_prediction2


# ============================================================
# Page Setup
# ============================================================

st.set_page_config(
    page_title="Prediction Results",
    page_icon="✦",
    layout="wide"
)


# ============================================================
# Helper Functions
# ============================================================

def readable_symptom(symptom):
    """
    Example:
    high_fever -> High Fever
    """
    return symptom.replace("_", " ").title()


def make_bullet_list(items):
    """
    Converts precautions list into HTML list items.
    """
    return "".join([f"<li>{escape(str(item))}</li>" for item in items])


def confidence_width(confidence):
    """
    Keeps confidence value between 0 and 100.
    """
    confidence = float(confidence)

    if confidence < 0:
        confidence = 0

    if confidence > 100:
        confidence = 100

    return confidence


def safe_filename_name(name):
    """
    Makes patient name safe for downloaded file name.
    Example:
    Md Tirtha -> Md_Tirtha
    """
    if not name or name.strip() == "":
        return "Not_Provided"

    clean_name = re.sub(r"[^A-Za-z0-9_-]+", "_", name.strip())
    return clean_name


def generate_report_html(patient_name, age, gender, contact_info, symptoms_text, prediction1, prediction2):
    """
    Generates the full report HTML.
    This report is shown inside the app and can also be downloaded.
    """

    report_id = "MDE-" + datetime.now().strftime("%Y%m%d%H%M%S")
    generated_time = datetime.now().strftime("%d / %m / %Y, %I:%M %p")

    patient_name_value = patient_name if patient_name and patient_name.strip() != "" else "Not Provided"
    contact_value = contact_info if contact_info and contact_info.strip() != "" else "Not Provided"

    p1_disease = escape(str(prediction1["disease"]))
    p1_conf = confidence_width(prediction1["confidence"])
    p1_precautions = make_bullet_list(prediction1["precautions"])

    p2_disease = escape(str(prediction2["disease"]))
    p2_conf = confidence_width(prediction2["confidence"])
    p2_precautions = make_bullet_list(prediction2["precautions"])

    patient_name_html = escape(patient_name_value)
    age_gender_html = escape(f"{age} / {gender}")
    contact_html = escape(contact_value)
    symptoms_html = escape(symptoms_text)

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Medical Diagnosis Expert System — Prediction Report</title>

<style>
:root {{
    --ink:#1b2430;
    --ink-soft:#4a5568;
    --line:#c9d2dc;
    --line-soft:#e4e9ee;
    --accent:#1f5f5b;
    --amber:#a66a1e;
    --amber-soft:#fbf1e2;
    --paper:#ffffff;
    --mono:'Courier New', Courier, monospace;
}}

* {{
    box-sizing:border-box;
}}

body {{
    margin:0;
    background:#dfe4e8;
    font-family: Georgia, 'Times New Roman', serif;
    color:var(--ink);
}}

.toolbar {{
    max-width:850px;
    margin:18px auto 0 auto;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:0 4px;
    font-family: Arial, Helvetica, sans-serif;
}}

.toolbar .hint {{
    font-size:12.5px;
    color:#4a5568;
}}

.toolbar button {{
    background:var(--accent);
    color:#fff;
    border:none;
    padding:9px 18px;
    font-size:13.5px;
    font-family: Arial, Helvetica, sans-serif;
    letter-spacing:.03em;
    border-radius:3px;
    cursor:pointer;
}}

.toolbar button:hover {{
    background:#174744;
}}

.sheet {{
    width:850px;
    min-height:1100px;
    margin:14px auto 40px auto;
    background:var(--paper);
    padding:56px 60px 50px 60px;
    position:relative;
    box-shadow:0 2px 18px rgba(0,0,0,.18);
}}

.head {{
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    border-bottom:3px solid var(--accent);
    padding-bottom:16px;
}}

.brand {{
    display:flex;
    align-items:center;
    gap:14px;
}}

.mark {{
    width:46px;
    height:46px;
    border:2px solid var(--accent);
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-family:Arial, Helvetica, sans-serif;
    font-weight:700;
    color:var(--accent);
    font-size:17px;
    flex:none;
}}

.brand h1 {{
    margin:0;
    font-size:21px;
    letter-spacing:.01em;
    color:var(--ink);
}}

.brand .tag {{
    font-family: Arial, Helvetica, sans-serif;
    font-size:11px;
    letter-spacing:.12em;
    text-transform:uppercase;
    color:var(--accent);
    margin-top:3px;
}}

.head-right {{
    text-align:right;
    font-family: Arial, Helvetica, sans-serif;
    font-size:11.5px;
    color:var(--ink-soft);
    line-height:1.5;
}}

.head-right .doc-id {{
    font-family:var(--mono);
    color:var(--ink);
    font-size:12px;
}}

.banner {{
    margin-top:14px;
    background:var(--amber-soft);
    border:1px solid #e3c68a;
    border-left:4px solid var(--amber);
    padding:10px 14px;
    font-family: Arial, Helvetica, sans-serif;
    font-size:11.5px;
    line-height:1.55;
    color:#6b4a12;
}}

.banner b {{
    color:#5a3c0f;
}}

.meta {{
    margin-top:22px;
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:0 30px;
    font-family:Arial, Helvetica, sans-serif;
    font-size:12.5px;
}}

.field {{
    display:flex;
    align-items:flex-end;
    gap:8px;
    padding:6px 0;
    border-bottom:1px solid var(--line-soft);
}}

.field .lbl {{
    color:var(--ink-soft);
    font-size:10.5px;
    text-transform:uppercase;
    letter-spacing:.08em;
    white-space:nowrap;
}}

.field .val {{
    flex:1;
    min-height:16px;
}}

.section-title {{
    margin:30px 0 12px 0;
    font-family:Arial, Helvetica, sans-serif;
    font-size:11.5px;
    font-weight:700;
    letter-spacing:.12em;
    text-transform:uppercase;
    color:var(--accent);
    display:flex;
    align-items:center;
    gap:10px;
}}

.section-title:after {{
    content:"";
    flex:1;
    height:1px;
    background:var(--line);
}}

.symptoms {{
    min-height:22px;
    font-size:14px;
    line-height:1.7;
    padding:2px 0;
}}

.predictions {{
    display:flex;
    gap:22px;
}}

.pred-card {{
    flex:1;
    border:1px solid var(--line);
    border-top:3px solid var(--accent);
    padding:16px 18px 18px 18px;
    position:relative;
}}

.pred-card.secondary {{
    border-top-color:#7a8a95;
}}

.pred-rank {{
    position:absolute;
    top:-13px;
    left:16px;
    background:var(--accent);
    color:#fff;
    font-family:Arial, Helvetica, sans-serif;
    font-size:10px;
    font-weight:700;
    letter-spacing:.08em;
    padding:3px 9px;
    border-radius:2px;
}}

.pred-card.secondary .pred-rank {{
    background:#7a8a95;
}}

.pred-name {{
    font-size:17px;
    font-weight:700;
    margin:8px 0 10px 0;
    min-height:20px;
}}

.confidence-row {{
    display:flex;
    align-items:center;
    gap:10px;
    font-family:Arial, Helvetica, sans-serif;
    margin-bottom:12px;
}}

.confidence-row .lbl {{
    font-size:10.5px;
    text-transform:uppercase;
    letter-spacing:.07em;
    color:var(--ink-soft);
    white-space:nowrap;
}}

.bar-track {{
    flex:1;
    height:8px;
    background:var(--line-soft);
    border-radius:5px;
    overflow:hidden;
}}

.bar-fill {{
    height:100%;
    background:var(--accent);
}}

.pred-card.secondary .bar-fill {{
    background:#7a8a95;
}}

.confidence-val {{
    font-family:var(--mono);
    font-size:12.5px;
    min-width:45px;
    text-align:right;
}}

.precautions-lbl {{
    font-family:Arial, Helvetica, sans-serif;
    font-size:10.5px;
    text-transform:uppercase;
    letter-spacing:.08em;
    color:var(--ink-soft);
    margin-bottom:6px;
}}

.precautions {{
    font-size:12.8px;
    line-height:1.85;
    min-height:60px;
}}

.notes {{
    min-height:50px;
    font-size:13px;
    line-height:1.7;
    border:1px solid var(--line-soft);
    padding:10px 12px;
    background:#fbfcfc;
}}

.disclaimer {{
    margin-top:28px;
    border:1px dashed #c2401f;
    background:#fdf2ef;
    padding:14px 16px;
    font-family:Arial, Helvetica, sans-serif;
    font-size:11px;
    line-height:1.65;
    color:#7d2a12;
}}

.disclaimer .title {{
    font-weight:700;
    letter-spacing:.08em;
    text-transform:uppercase;
    font-size:10.5px;
    margin-bottom:5px;
    color:#a3311a;
}}

.footer {{
    margin-top:34px;
    display:flex;
    justify-content:space-between;
    align-items:flex-end;
    font-family:Arial, Helvetica, sans-serif;
    font-size:11.5px;
    color:var(--ink-soft);
}}

.sig {{
    text-align:center;
}}

.sig-line {{
    width:190px;
    border-bottom:1px solid var(--ink);
    height:34px;
}}

.sig .cap {{
    margin-top:6px;
    font-size:10.5px;
    color:var(--ink-soft);
}}

.foot-left {{
    font-size:10.5px;
    line-height:1.6;
}}

.watermark {{
    position:absolute;
    top:46%;
    left:50%;
    transform:translate(-50%,-50%) rotate(-28deg);
    font-family:Arial, Helvetica, sans-serif;
    font-size:64px;
    font-weight:800;
    letter-spacing:.05em;
    color:rgba(31,95,91,0.06);
    pointer-events:none;
    white-space:nowrap;
    user-select:none;
}}

@media print {{
    body {{
        background:#fff;
    }}

    .toolbar {{
        display:none;
    }}

    .sheet {{
        box-shadow:none;
        margin:0 auto;
        width:auto;
        padding:30px 42px 34px 42px;
    }}

    @page {{
        size:A4;
        margin:12mm;
    }}
}}
</style>
</head>

<body>

<div class="toolbar">
    <div class="hint">Click Print Report and choose Save as PDF.</div>
    <button onclick="window.print()">Print Report</button>
</div>

<div class="sheet">
    <div class="watermark">NOT VERIFIED</div>

    <div class="head">
        <div class="brand">
            <div class="mark">MD</div>
            <div>
                <h1>Medical Diagnosis Expert System</h1>
                <div class="tag">AI-Based Disease Prediction Report</div>
            </div>
        </div>

        <div class="head-right">
            Report ID: <span class="doc-id">{report_id}</span><br>
            Generated: <span>{generated_time}</span><br>
            System: AI-Based Prediction
        </div>
    </div>

    <div class="banner">
        <b>This is not a medical certificate or verified diagnosis.</b>
        It is an automated prediction generated by a student/academic AI project for demonstration purposes only.
        It does not replace consultation, examination, or prescription by a licensed physician.
    </div>

    <div class="meta">
        <div class="field"><span class="lbl">Patient Name</span><span class="val">{patient_name_html}</span></div>
        <div class="field"><span class="lbl">Age / Gender</span><span class="val">{age_gender_html}</span></div>
        <div class="field"><span class="lbl">Contact</span><span class="val">{contact_html}</span></div>
        <div class="field"><span class="lbl">Reference No.</span><span class="val">{report_id}</span></div>
    </div>

    <div class="section-title">Reported Symptoms</div>
    <div class="symptoms">{symptoms_html}</div>

    <div class="section-title">Predicted Conditions</div>

    <div class="predictions">
        <div class="pred-card">
            <div class="pred-rank">Most Likely</div>
            <div class="pred-name">{p1_disease}</div>

            <div class="confidence-row">
                <span class="lbl">Confidence</span>
                <div class="bar-track"><div class="bar-fill" style="width:{p1_conf:.2f}%"></div></div>
                <span class="confidence-val">{p1_conf:.2f}%</span>
            </div>

            <div class="precautions-lbl">Suggested Precautions</div>
            <div class="precautions">
                <ol>{p1_precautions}</ol>
            </div>
        </div>

        <div class="pred-card secondary">
            <div class="pred-rank">Possible</div>
            <div class="pred-name">{p2_disease}</div>

            <div class="confidence-row">
                <span class="lbl">Confidence</span>
                <div class="bar-track"><div class="bar-fill" style="width:{p2_conf:.2f}%"></div></div>
                <span class="confidence-val">{p2_conf:.2f}%</span>
            </div>

            <div class="precautions-lbl">Suggested Precautions</div>
            <div class="precautions">
                <ol>{p2_precautions}</ol>
            </div>
        </div>
    </div>

    <div class="section-title">Additional Notes</div>
    <div class="notes">
        Prediction 1 is the main system result. Prediction 2 is shown as a second-priority comparison result.
        Confidence scores are model-generated values and should not be treated as clinical certainty.
    </div>

    <div class="disclaimer">
        <div class="title">Important</div>
        Results are generated by a machine learning model trained on a symptom–disease dataset for academic/project purposes.
        Confidence scores reflect model probability, not clinical certainty. This report carries no medical or legal authority
        and must not be used in place of professional medical advice, diagnosis, or treatment.
    </div>

    <div class="footer">
        <div class="foot-left">
            Medical Diagnosis Expert System — Academic Project<br>
            Generated automatically · No physician review
        </div>

        <div class="sig">
            <div class="sig-line"></div>
            <div class="cap">System-Generated · Not a Doctor's Signature</div>
        </div>
    </div>
</div>

</body>
</html>
"""


# ============================================================
# CSS Design for Streamlit Page
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

.patient-card {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    background: rgba(255, 255, 255, 0.96);
    padding: 28px;
    border-radius: 24px;
    box-shadow: 0px 14px 35px rgba(0,0,0,0.25);
    margin-bottom: 25px;
    border-left: 8px solid #16db93;
    animation: fadeUp 0.8s ease;
}

.patient-card h3,
.patient-card p,
.patient-card b {
    color: #061a40 !important;
}

.result-card-one {
    position: relative;
    background: linear-gradient(135deg, rgba(227,242,253,0.98), rgba(187,222,251,0.98));
    padding: 34px 30px 30px 30px;
    border-radius: 26px;
    border-left: 10px solid #1565c0;
    box-shadow: 0px 18px 45px rgba(0,0,0,0.32);
    min-height: 450px;
    color: #061a40 !important;
    transition: all 0.25s ease-in-out;
    animation: fadeUp 0.9s ease;
}

.result-card-two {
    position: relative;
    background: linear-gradient(135deg, rgba(232,245,233,0.98), rgba(200,230,201,0.98));
    padding: 34px 30px 30px 30px;
    border-radius: 26px;
    border-left: 10px solid #2e7d32;
    box-shadow: 0px 18px 45px rgba(0,0,0,0.32);
    min-height: 450px;
    color: #061a40 !important;
    transition: all 0.25s ease-in-out;
    animation: fadeUp 1s ease;
}

.result-card-one:hover,
.result-card-two:hover {
    transform: translateY(-8px);
    box-shadow: 0px 25px 55px rgba(255,255,255,0.18);
}

.result-card-one *,
.result-card-two * {
    color: #061a40 !important;
}

.priority-badge-main {
    position: absolute;
    top: 18px;
    right: 18px;
    background: linear-gradient(135deg, #1565c0, #00c6ff);
    color: white !important;
    padding: 9px 14px;
    border-radius: 999px;
    font-weight: 900;
    font-size: 14px;
}

.priority-badge-second {
    position: absolute;
    top: 18px;
    right: 18px;
    background: linear-gradient(135deg, #2e7d32, #16db93);
    color: white !important;
    padding: 9px 14px;
    border-radius: 999px;
    font-weight: 900;
    font-size: 14px;
}

.prediction-title {
    font-size: 20px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #345 !important;
    margin-bottom: 12px;
    padding-right: 140px;
}

.disease-name {
    font-size: 32px;
    font-weight: 950;
    margin-bottom: 14px;
    color: #0b2d5c !important;
}

.confidence {
    font-size: 21px;
    font-weight: 850;
    margin-bottom: 22px;
    background: rgba(255,255,255,0.8);
    padding: 12px 16px;
    border-radius: 16px;
    display: inline-block;
}

.result-card-one li,
.result-card-two li {
    margin-bottom: 10px;
    font-size: 16px;
    line-height: 1.55;
    font-weight: 600;
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
}

/* Small download button */
.stDownloadButton > button {
    background: #ffffff !important;
    color: #061a40 !important;
    border: 2px solid #16db93 !important;
    border-radius: 14px !important;
    font-size: 14px !important;
    font-weight: 850 !important;
    padding: 0.55rem 0.8rem !important;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.18) !important;
}

.stDownloadButton > button:hover {
    background: #e7fbff !important;
    color: #061a40 !important;
    border: 2px solid #00c6ff !important;
    transform: translateY(-2px);
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
}

.report-top-row {
    max-width: 1050px;
    margin: 10px auto 12px auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.report-title-text {
    color: #ffffff;
    font-size: 22px;
    font-weight: 900;
}

hr {
    border: none;
    height: 1px;
    background: rgba(255,255,255,0.25);
    margin: 28px 0;
}
</style>
""")


# ============================================================
# Check Symptoms
# ============================================================

if "selected_symptoms" not in st.session_state or len(st.session_state.selected_symptoms) == 0:
    st.error("No symptoms selected. Please go back and select symptoms first.")
    st.html('<a class="home-link" href="/diagnosis" target="_self">Go To Diagnosis Page</a>')
    st.stop()


# ============================================================
# Report Visibility Session State
# ============================================================

if "show_report_view" not in st.session_state:
    st.session_state.show_report_view = False


# ============================================================
# Get Predictions
# ============================================================

prediction1 = get_prediction1(st.session_state.selected_symptoms)
prediction2 = get_prediction2(st.session_state.selected_symptoms)

selected_symptoms_text = ", ".join(
    [readable_symptom(s) for s in st.session_state.selected_symptoms]
)

patient_name_display = st.session_state.patient_name if st.session_state.patient_name else "Not Provided"
contact_display = st.session_state.contact_info if "contact_info" in st.session_state and st.session_state.contact_info else "Not Provided"


# ============================================================
# Generate Report
# ============================================================

report_html = generate_report_html(
    patient_name=st.session_state.patient_name,
    age=st.session_state.age,
    gender=st.session_state.gender,
    contact_info=st.session_state.contact_info if "contact_info" in st.session_state else "",
    symptoms_text=selected_symptoms_text,
    prediction1=prediction1,
    prediction2=prediction2
)

download_name = safe_filename_name(st.session_state.patient_name)
download_file_name = f"medical_report_{download_name}.html"


# ============================================================
# Result Page UI
# ============================================================

st.html("""
<div class="header-card">
    <div class="section-title">Prediction Results</div>
    <div class="page-subtitle">
        The system displays two possible disease predictions in one view with separate precautions.
    </div>
    <div class="step-pill">Final Step · AI Result</div>
</div>
""")


st.html(f"""
<div class="patient-card">
    <h3>Patient Details</h3>
    <p><b>Name:</b> {escape(patient_name_display)}</p>
    <p><b>Age:</b> {st.session_state.age}</p>
    <p><b>Gender:</b> {escape(st.session_state.gender)}</p>
    <p><b>Contact:</b> {escape(contact_display)}</p>
    <p><b>Selected Symptoms:</b> {escape(selected_symptoms_text)}</p>
</div>
""")


col1, col2 = st.columns(2)

with col1:
    disease = prediction1["disease"]
    confidence = prediction1["confidence"]
    precautions = prediction1["precautions"]
    precaution_html = make_bullet_list(precautions)

    st.html(f"""
    <div class="result-card-one">
        <div class="priority-badge-main">★ Main</div>
        <div class="prediction-title">Prediction 1</div>
        <div class="disease-name">{escape(str(disease))}</div>
        <div class="confidence">Confidence Score: {confidence:.2f}%</div>
        <h4>Precautions for {escape(str(disease))}</h4>
        <ol>{precaution_html}</ol>
    </div>
    """)

with col2:
    disease = prediction2["disease"]
    confidence = prediction2["confidence"]
    precautions = prediction2["precautions"]
    precaution_html = make_bullet_list(precautions)

    st.html(f"""
    <div class="result-card-two">
        <div class="priority-badge-second">◆ Second</div>
        <div class="prediction-title">Prediction 2</div>
        <div class="disease-name">{escape(str(disease))}</div>
        <div class="confidence">Confidence Score: {confidence:.2f}%</div>
        <h4>Precautions for {escape(str(disease))}</h4>
        <ol>{precaution_html}</ol>
    </div>
    """)


st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("View Report", use_container_width=True):
        st.session_state.show_report_view = True

with col2:
    if st.button("New Diagnosis", use_container_width=True):
        st.session_state.patient_name = ""
        st.session_state.age = 18
        st.session_state.gender = "Male"
        st.session_state.contact_info = ""
        st.session_state.selected_symptoms = []
        st.session_state.show_report_view = False
        st.switch_page("pages/diagnosis.py")

with col3:
    st.html('<a class="home-link" href="/" target="_self">Back To Main Page</a>')


# ============================================================
# Show Full Report After Clicking View Report
# ============================================================

if st.session_state.show_report_view:
    st.markdown("---")

    report_col1, report_col2 = st.columns([5, 1])

    with report_col1:
        st.html('<div class="report-title-text">Report Preview</div>')

    with report_col2:
        st.download_button(
            label="Download",
            data=report_html,
            file_name=download_file_name,
            mime="text/html",
            use_container_width=True
        )

    components.html(
        report_html,
        height=1250,
        scrolling=True
    )