import streamlit as st

st.set_page_config(page_title="Patient Symptoms", page_icon="🧾", layout="wide")

st.title("Patient Symptom Page")
st.warning("This page is a legacy symptom page. Use the Diagnosis page for the current workflow.")

st.markdown("[Go to Diagnosis](/diagnosis)")
