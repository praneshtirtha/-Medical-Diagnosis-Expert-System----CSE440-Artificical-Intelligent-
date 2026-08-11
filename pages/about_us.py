import streamlit as st


# ============================================================
# Page Setup
# ============================================================

st.set_page_config(
    page_title="About Us",
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

.logo-box {
    width: 78px;
    height: 78px;
    margin: 0 auto 18px auto;
    border-radius: 24px;
    background: linear-gradient(135deg, #00c6ff, #16db93);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    color: #ffffff;
    box-shadow: 0px 15px 38px rgba(0,198,255,0.35);
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
    max-width: 820px;
    margin-left: auto;
    margin-right: auto;
}

.card-grid {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
    margin-bottom: 28px;
}

.info-card {
    background: rgba(255, 255, 255, 0.96);
    padding: 26px;
    border-radius: 24px;
    box-shadow: 0px 14px 35px rgba(0,0,0,0.25);
    border-left: 8px solid #16db93;
    min-height: 190px;
    transition: all 0.25s ease-in-out;
    animation: fadeUp 0.9s ease;
}

.info-card:hover {
    transform: translateY(-7px);
    box-shadow: 0px 22px 45px rgba(255,255,255,0.16);
}

.info-card.blue {
    border-left-color: #00c6ff;
}

.info-card.purple {
    border-left-color: #7e57c2;
}

.info-card.orange {
    border-left-color: #f59e0b;
}

.info-card h3 {
    color: #061a40 !important;
    font-size: 23px;
    font-weight: 950;
    margin-bottom: 12px;
}

.info-card p {
    color: #344054 !important;
    font-size: 15.5px;
    line-height: 1.65;
    font-weight: 600;
}

.feature-card {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    background:
        linear-gradient(135deg, rgba(227,242,253,0.98), rgba(232,245,233,0.98));
    padding: 28px;
    border-radius: 26px;
    box-shadow: 0px 18px 45px rgba(0,0,0,0.32);
    border-left: 10px solid #1565c0;
    margin-bottom: 28px;
}

.feature-card h3 {
    color: #061a40 !important;
    font-size: 25px;
    font-weight: 950;
    margin-bottom: 16px;
}

.feature-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
}

.feature-item {
    background: #ffffff;
    color: #061a40;
    padding: 15px;
    border-radius: 16px;
    text-align: center;
    font-weight: 900;
    border: 1px solid #dbe7ef;
}

.warning-card {
    max-width: 1050px;
    margin-left: auto;
    margin-right: auto;
    background: #fff4e5;
    padding: 22px 26px;
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

    .card-grid {
        grid-template-columns: 1fr;
    }

    .feature-row {
        grid-template-columns: repeat(2, 1fr);
    }

    .button-row {
        grid-template-columns: 1fr;
    }
}
</style>
""")


# ============================================================
# Page Content
# ============================================================

st.html("""
<div class="header-card">
    <div class="logo-box">✦</div>
    <div class="section-title">About The System</div>
    <div class="page-subtitle">
        A web-based AI system that predicts possible diseases from patient symptoms
        and generates a simple prediction report.
    </div>
</div>
""")


st.html("""
<div class="card-grid">
    <div class="info-card">
        <h3>What It Does</h3>
        <p>
            The system collects symptoms from the user and predicts two possible
            diseases with confidence scores.
        </p>
    </div>

    <div class="info-card blue">
        <h3>Project Goal</h3>
        <p>
            The goal is to show how machine learning can support symptom-based
            disease prediction in an academic AI project.
        </p>
    </div>

    <div class="info-card purple">
        <h3>Prediction Result</h3>
        <p>
            Prediction 1 shows the main result. Prediction 2 shows a second-priority
            result for comparison.
        </p>
    </div>

    <div class="info-card orange">
        <h3>Report System</h3>
        <p>
            Users can view a report with patient details, symptoms, predictions,
            confidence scores, precautions, and disclaimer.
        </p>
    </div>
</div>
""")


st.html("""
<div class="feature-card">
    <h3>Main Features</h3>

    <div class="feature-row">
        <div class="feature-item">Symptom Input</div>
        <div class="feature-item">Two Predictions</div>
        <div class="feature-item">Confidence Score</div>
        <div class="feature-item">Report View</div>
    </div>
</div>
""")


st.html("""
<div class="warning-card">
    <h3>Important Note</h3>
    <p>
        This system is only for academic demonstration. It is not a medical certificate
        and cannot replace a licensed doctor.
    </p>
</div>
""")


st.html("""
<div class="button-row">
    <a class="nav-button" href="/" target="_self">Back To Home</a>
    <a class="nav-button" href="/how_it_works" target="_self">How It Works</a>
    <a class="nav-button" href="/diagnosis" target="_self">Start Diagnosis</a>
</div>
""")