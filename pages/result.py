import streamlit as st
from datetime import datetime
from html import escape
import re

from prediction1 import get_prediction1

st.set_page_config(page_title="Prediction Results", page_icon="✅", layout="wide")

if "selected_symptoms" not in st.session_state or not st.session_state.selected_symptoms:
    st.title("Prediction Results")
    st.warning("No symptoms were selected yet. Please complete the Diagnosis page first.")
    st.markdown("[Open Diagnosis](/diagnosis)")
    st.stop()

st.title("✅ Diagnosis Results")

symptoms_text = ", ".join([sym.replace("_", " ").title() for sym in st.session_state.selected_symptoms])

prediction = get_prediction1(st.session_state.selected_symptoms)

with st.expander("Patient Summary", expanded=True):
    st.write(f"**Name:** {st.session_state.get('patient_name', 'Not Provided')}")
    st.write(f"**Age:** {st.session_state.get('age', 'Not Provided')}")
    st.write(f"**Gender:** {st.session_state.get('gender', 'Not Provided')}")
    if st.session_state.get('contact_info'):
        st.write(f"**Contact:** {st.session_state.get('contact_info')}")
    st.write(f"**Symptoms:** {symptoms_text}")

st.markdown("---")

st.subheader("Random Forest Prediction")
st.metric(label="Predicted Disease", value=prediction["disease"])
st.metric(label="Confidence", value=f"{prediction['confidence']:.2f}%")

st.subheader("Recommended Precautions")
for item in prediction["precautions"]:
    st.write(f"- {item}")

st.markdown("---")

report_html = f"""
<html>
<head><meta charset='utf-8'><title>Diagnosis Report</title></head>
<body>
<h1>Medical Diagnosis Expert System</h1>
<p><strong>Patient:</strong> {escape(str(st.session_state.get('patient_name', 'Not Provided')))}</p>
<p><strong>Age / Gender:</strong> {escape(str(st.session_state.get('age', 'Not Provided')))} / {escape(str(st.session_state.get('gender', 'Not Provided')))}</p>
<p><strong>Contact:</strong> {escape(str(st.session_state.get('contact_info', 'Not Provided')))}</p>
<p><strong>Symptoms:</strong> {escape(symptoms_text)}</p>
<h2>Prediction</h2>
<p><strong>Disease:</strong> {escape(str(prediction['disease']))}</p>
<p><strong>Confidence:</strong> {prediction['confidence']:.2f}%</p>
<h3>Precautions</h3>
<ul>{''.join([f'<li>{escape(str(item))}</li>' for item in prediction['precautions']])}</ul>
<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
</body>
</html>
"""

st.download_button(
    "Download Diagnosis Report",
    report_html,
    file_name=f"diagnosis_report_{re.sub(r'[^A-Za-z0-9_-]+', '_', st.session_state.get('patient_name', 'Not_Provided'))}.html",
    mime="text/html"
)

st.markdown("---")
st.markdown("[Run Another Diagnosis](/diagnosis)")
