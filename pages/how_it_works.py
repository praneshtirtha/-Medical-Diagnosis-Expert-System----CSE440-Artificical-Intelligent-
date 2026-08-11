import streamlit as st


# ============================================================
# Page Setup
# ============================================================

st.set_page_config(
    page_title="How It Works",
    page_icon="✦",
    layout="wide"
)


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
    padding: 38px 42px;
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
    font-size: 46px;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 10px;
    text-shadow: 0px 7px 20px rgba(0,0,0,0.45);
}

.page-subtitle {
    color: #c9f7ff;
    font-size: 18px;
    line-height: 1.7;
    max-width: 850px;
    margin-left: auto;
    margin-right: auto;
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

.workflow-grid {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    margin-bottom: 28px;
}

.info-card {
    background: rgba(255, 255, 255, 0.96);
    padding: 26px;
    border-radius: 24px;
    box-shadow: 0px 14px 35px rgba(0,0,0,0.25);
    border-left: 8px solid #16db93;
    min-height: 230px;
    transition: all 0.25s ease-in-out;
    animation: fadeUp 0.9s ease;
}

.info-card:hover {
    transform: translateY(-7px);
    box-shadow: 0px 22px 45px rgba(255,255,255,0.16);
}

.info-card h3 {
    color: #061a40 !important;
    font-size: 22px;
    font-weight: 950;
    margin-bottom: 12px;
}

.info-card p {
    color: #344054 !important;
    font-size: 15.5px;
    line-height: 1.65;
    font-weight: 600;
}

.step-number {
    width: 46px;
    height: 46px;
    border-radius: 16px;
    background: linear-gradient(135deg, #16db93, #00c6ff);
    color: #061a40;
    font-size: 22px;
    font-weight: 950;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
}

.flow-card {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    background: rgba(255, 255, 255, 0.96);
    padding: 30px;
    border-radius: 26px;
    box-shadow: 0px 18px 45px rgba(0,0,0,0.32);
    border-left: 10px solid #00c6ff;
    margin-bottom: 28px;
    animation: fadeUp 1s ease;
}

.flow-card h3 {
    color: #061a40 !important;
    font-size: 26px;
    font-weight: 950;
    margin-bottom: 18px;
}

.flow-line {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 18px;
}

.flow-item {
    background: #eefbff;
    border: 2px solid #8fd6ff;
    color: #061a40;
    padding: 13px 18px;
    border-radius: 16px;
    font-weight: 900;
    font-size: 15px;
}

.arrow {
    color: #0b2d5c;
    font-size: 24px;
    font-weight: 950;
}

.model-card {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    background:
        linear-gradient(135deg, rgba(227,242,253,0.98), rgba(232,245,233,0.98));
    padding: 30px;
    border-radius: 26px;
    box-shadow: 0px 18px 45px rgba(0,0,0,0.32);
    border-left: 10px solid #1565c0;
    margin-bottom: 28px;
    animation: fadeUp 1.05s ease;
}

.model-card h3 {
    color: #061a40 !important;
    font-size: 26px;
    font-weight: 950;
    margin-bottom: 16px;
}

.model-card p,
.model-card li {
    color: #344054 !important;
    font-size: 15.5px;
    line-height: 1.75;
    font-weight: 600;
}

.warning-card {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    background: #fff4e5;
    padding: 24px 28px;
    border-radius: 22px;
    border-left: 8px solid #a66a1e;
    box-shadow: 0px 14px 35px rgba(0,0,0,0.25);
    margin-bottom: 28px;
}

.warning-card h3 {
    color: #7a3f00 !important;
    font-size: 22px;
    font-weight: 950;
    margin-bottom: 10px;
}

.warning-card p {
    color: #6b4a12 !important;
    font-size: 15.5px;
    line-height: 1.65;
    font-weight: 650;
}

.button-row {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.nav-button {
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

.nav-button:hover {
    background: linear-gradient(135deg, #ffffff, #e7fbff);
    color: #07111f !important;
    border: 2px solid #16db93;
    transform: translateY(-4px) scale(1.02);
}

@media (max-width: 900px) {
    .block-container {
        max-width: 95% !important;
    }

    .section-title {
        font-size: 34px;
    }

    .header-card {
        padding: 28px 22px;
    }

    .workflow-grid {
        grid-template-columns: 1fr;
    }

    .button-row {
        grid-template-columns: 1fr;
    }

    .arrow {
        display: none;
    }
}
</style>
""")


# ============================================================
# Page Content
# ============================================================

st.html("""
<div class="header-card">
    <div class="section-title">How It Works</div>
    <div class="page-subtitle">
        This page explains how the Medical Diagnosis Expert System collects symptoms,
        processes them, generates two AI-based predictions, and creates a downloadable report.
    </div>
    <div class="step-pill">System Workflow</div>
</div>
""")


st.html("""
<div class="workflow-grid">
    <div class="info-card">
        <div class="step-number">1</div>
        <h3>Patient Information</h3>
        <p>
            The user enters basic patient details such as name, age, gender,
            and optional contact number or email. These details are used only
            for displaying the final report.
        </p>
    </div>

    <div class="info-card">
        <div class="step-number">2</div>
        <h3>Symptom Selection</h3>
        <p>
            The user selects symptoms from the available symptom list.
            The system also allows manual symptom input using comma-separated text.
        </p>
    </div>

    <div class="info-card">
        <div class="step-number">3</div>
        <h3>Input Conversion</h3>
        <p>
            The selected symptoms are converted into numerical 0/1 format.
            A value of 1 means the symptom is present, and 0 means it is absent.
        </p>
    </div>
</div>

<div class="workflow-grid">
    <div class="info-card">
        <div class="step-number">4</div>
        <h3>AI Prediction</h3>
        <p>
            The processed symptom input is passed into trained machine learning models.
            The system generates two possible disease predictions.
        </p>
    </div>

    <div class="info-card">
        <div class="step-number">5</div>
        <h3>Precaution Matching</h3>
        <p>
            After predicting diseases, the system searches the precaution dataset
            and shows separate suggested precautions for each predicted condition.
        </p>
    </div>

    <div class="info-card">
        <div class="step-number">6</div>
        <h3>Report Generation</h3>
        <p>
            The final result page can generate a report containing patient details,
            selected symptoms, predictions, confidence scores, precautions, and disclaimer.
        </p>
    </div>
</div>
""")


st.html("""
<div class="flow-card">
    <h3>Complete System Flow</h3>

    <div class="flow-line">
        <div class="flow-item">Patient Details</div>
        <div class="arrow">→</div>
        <div class="flow-item">Symptoms</div>
        <div class="arrow">→</div>
        <div class="flow-item">0/1 Encoding</div>
        <div class="arrow">→</div>
        <div class="flow-item">ML Models</div>
        <div class="arrow">→</div>
        <div class="flow-item">Prediction</div>
        <div class="arrow">→</div>
        <div class="flow-item">Report</div>
    </div>
</div>
""")


st.html("""
<div class="model-card">
    <h3>Prediction Method</h3>
    <p>
        The system uses two machine learning prediction outputs:
    </p>

    <ul>
        <li><b>Prediction 1:</b> Main prediction result generated by the best-performing model.</li>
        <li><b>Prediction 2:</b> Second-priority prediction result generated for comparison support.</li>
        <li><b>Confidence Score:</b> Shows how strongly the model supports the predicted result.</li>
        <li><b>Precautions:</b> Suggested precautions are shown from the precaution dataset, not generated randomly.</li>
    </ul>
</div>
""")


st.html("""
<div class="warning-card">
    <h3>Important Disclaimer</h3>
    <p>
        This system is an academic AI project. It is not a real medical diagnosis tool,
        not a medical certificate, and not a replacement for a doctor. The prediction is
        based on dataset patterns and should be used only for demonstration and educational purposes.
    </p>
</div>
""")


st.html("""
<div class="button-row">
    <a class="nav-button" href="/" target="_self">Back To Home</a>
    <a class="nav-button" href="/about_us" target="_self">About The System</a>
    <a class="nav-button" href="/diagnosis" target="_self">Start Diagnosis</a>
</div>
""")