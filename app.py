import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis Expert System",
    page_icon="✦",
    layout="wide"
)

st.html("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stHeader"] {
    background: rgba(7, 17, 31, 0.85);
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
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 80px 55px;
    border-radius: 35px;
    background:
        linear-gradient(135deg, rgba(6, 26, 64, 0.95), rgba(9, 47, 93, 0.92)),
        radial-gradient(circle at 20% 20%, rgba(0, 198, 255, 0.50), transparent 30%),
        radial-gradient(circle at 85% 75%, rgba(22, 219, 147, 0.45), transparent 32%);
    box-shadow: 0px 25px 70px rgba(0, 0, 0, 0.45);
    border: 1px solid rgba(255,255,255,0.22);
    text-align: center;
}

.hero::before {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    background: rgba(255,255,255,0.08);
    top: -90px;
    left: -70px;
    animation: floatOne 7s ease-in-out infinite;
}

.hero::after {
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    background: rgba(0,198,255,0.18);
    bottom: -80px;
    right: -60px;
    animation: floatTwo 8s ease-in-out infinite;
}

@keyframes floatOne {
    0% { transform: translate(0px, 0px); }
    50% { transform: translate(30px, 25px); }
    100% { transform: translate(0px, 0px); }
}

@keyframes floatTwo {
    0% { transform: translate(0px, 0px); }
    50% { transform: translate(-25px, -30px); }
    100% { transform: translate(0px, 0px); }
}

.pulse-icon {
    position: relative;
    z-index: 2;
    width: 105px;
    height: 105px;
    margin: 0 auto 25px auto;
    border-radius: 28px;
    background: linear-gradient(135deg, #00c6ff, #16db93);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 50px;
    color: white;
    box-shadow: 0px 18px 45px rgba(0,198,255,0.35);
    animation: pulseGlow 2.5s infinite;
}

@keyframes pulseGlow {
    0% { transform: scale(1); box-shadow: 0px 18px 45px rgba(0,198,255,0.35); }
    50% { transform: scale(1.06); box-shadow: 0px 22px 70px rgba(22,219,147,0.45); }
    100% { transform: scale(1); box-shadow: 0px 18px 45px rgba(0,198,255,0.35); }
}

.title {
    position: relative;
    z-index: 2;
    font-size: 58px;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 16px;
    text-shadow: 0px 8px 25px rgba(0,0,0,0.5);
    letter-spacing: -1px;
}

.subtitle {
    position: relative;
    z-index: 2;
    font-size: 25px;
    color: #b9f2ff;
    font-weight: 750;
    margin-bottom: 24px;
}

.description {
    position: relative;
    z-index: 2;
    font-size: 18px;
    color: #eefbff;
    max-width: 900px;
    margin: auto;
    line-height: 1.8;
}

.feature-row {
    position: relative;
    z-index: 2;
    margin-top: 34px;
    display: flex;
    gap: 18px;
    justify-content: center;
    flex-wrap: wrap;
}

.feature-pill {
    padding: 13px 22px;
    border-radius: 999px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.28);
    color: #ffffff;
    font-weight: 850;
    backdrop-filter: blur(10px);
    transition: 0.25s ease-in-out;
}

.feature-pill:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.25);
    box-shadow: 0px 12px 30px rgba(0,198,255,0.30);
}

.nav-row {
    margin-top: 30px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.nav-button {
    text-decoration: none !important;
    display: block;
    text-align: center;
    background: linear-gradient(135deg, #16db93, #00c6ff);
    color: #061a40 !important;
    border: 2px solid rgba(255,255,255,0.9);
    border-radius: 18px;
    font-size: 18px;
    font-weight: 850;
    padding: 16px 18px;
    box-shadow: 0px 12px 30px rgba(0, 198, 255, 0.25);
    transition: all 0.25s ease-in-out;
}

.nav-button:hover {
    background: linear-gradient(135deg, #ffffff, #e7fbff);
    color: #07111f !important;
    border: 2px solid #16db93;
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0px 18px 40px rgba(255,255,255,0.25);
}

.footer-note {
    text-align: center;
    color: #d9f7ff;
    margin-top: 28px;
    font-size: 15px;
    opacity: 0.9;
}
</style>

<div class="hero">
    <div class="pulse-icon">✦</div>

    <div class="title">Medical Diagnosis Expert System</div>

    <div class="subtitle">AI-Based Disease Prediction from Patient Symptoms</div>

    <p class="description">
        A modern web-based artificial intelligence system that predicts the top two possible diseases
        using symptom analysis and a trained Random Forest machine learning model. The system also
        shows confidence scores and separate precautions for each prediction.
    </p>

    <div class="feature-row">
        <div class="feature-pill">Machine Learning</div>
        <div class="feature-pill">Top 2 Predictions</div>
        <div class="feature-pill">Confidence Score</div>
        <div class="feature-pill">Precaution Support</div>
    </div>
</div>

<div class="nav-row">
    <a class="nav-button" href="/about_us" target="_self">About The System</a>
    <a class="nav-button" href="/diagnosis" target="_self">Start Diagnosis</a>
    <a class="nav-button" href="/diagnosis" target="_self">Skip Intro</a>
</div>

<div class="footer-note">
    CSE440 Artificial Intelligence Project · Medical Diagnosis Expert System
</div>
""")