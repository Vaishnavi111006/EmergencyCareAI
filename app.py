import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="EmergencyCare AI",
    page_icon="🚑",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

/* ---------------- BACKGROUND ---------------- */

.stApp{
    background:#EAF6FF;
}

/* ---------------- TEXT ---------------- */

html, body, p, label, div, span{
    color:#1F2937 !important;
    font-family:Arial, Helvetica, sans-serif;
}

/* ---------------- HEADINGS ---------------- */

h1,h2,h3,h4,h5,h6{
    color:#0B5394 !important;
}

/* ---------------- MAIN TITLE ---------------- */

.main-title{
    font-size:72px;
    font-weight:800;
    text-align:center;
    color:#0B5394 !important;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    font-size:24px;
    color:#374151 !important;
    margin-bottom:35px;
}

/* ---------------- WHITE CARD ---------------- */

.card{
    background:white;
    border-radius:20px;
    padding:25px;
    box-shadow:0 6px 18px rgba(0,0,0,0.12);
    color:#1F2937 !important;
}

/* ---------------- RESULT ---------------- */

.result-low{
    background:#D1FAE5;
    color:#065F46 !important;
    padding:20px;
    border-radius:15px;
    font-size:28px;
    font-weight:bold;
    text-align:center;
}

.result-high{
    background:#FEE2E2;
    color:#991B1B !important;
    padding:20px;
    border-radius:15px;
    font-size:28px;
    font-weight:bold;
    text-align:center;
}

/* ---------------- SIDEBAR ---------------- */

section[data-testid="stSidebar"]{
    background:#CFEFFF;
}

section[data-testid="stSidebar"] *{
    color:#1F2937 !important;
}

/* ---------------- BUTTON ---------------- */

.stButton>button{
    width:100%;
    height:58px;
    background:#0B5394;
    color:white !important;
    font-size:18px;
    font-weight:bold;
    border:none;
    border-radius:10px;
}

.stButton>button:hover{
    background:#1565C0;
    color:white !important;
}

/* ---------------- INPUT BOXES ---------------- */

.stNumberInput input{
    background:#2B2D3A !important;
    color:white !important;
    border-radius:10px !important;
}

/* Number input + and - buttons */

.stNumberInput button{
    color:white !important;
}

/* ---------------- SELECT BOX ---------------- */

.stSelectbox div[data-baseweb="select"]{
    background:#2B2D3A !important;
    border-radius:10px;
}

/* Selected value */

.stSelectbox div[data-baseweb="select"] span{
    color:white !important;
}

/* Dropdown arrow */

.stSelectbox svg{
    color:white !important;
    fill:white !important;
}

/* ---------------- METRIC ---------------- */

[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0 5px 15px rgba(0,0,0,0.12);
}

[data-testid="metric-container"] *{
    color:#1F2937 !important;
}

/* ---------------- FOOTER ---------------- */

.footer{
    text-align:center;
    color:#374151 !important;
    margin-top:40px;
    font-size:15px;
}

/* ---------------- LINKS ---------------- */

a{
    color:#0B5394 !important;
    text-decoration:none;
}

a:hover{
    color:#1565C0 !important;
}

/* ---------------- HIDE STREAMLIT MENU ---------------- */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD MODEL
# ----------------------------

model = joblib.load("model.pkl")

# ----------------------------
# SIDEBAR
# ----------------------------

st.sidebar.image("https://img.icons8.com/color/96/heart-with-pulse.png", width=80)

st.sidebar.title("EmergencyCare AI")

st.sidebar.markdown("""
### 🚑 About

EmergencyCare AI predicts heart disease risk using Machine Learning.

### 🤖 AI Model

Random Forest Classifier

### 🎯 Theme

HealthTech & Emergency Response

### ⭐ Features

✅ Heart Disease Prediction

✅ Confidence Score

✅ Emergency Contacts

✅ Nearby Hospitals

✅ Health Recommendations
""")

st.sidebar.success("Idea2Impact 2026")

# ----------------------------
# HEADER
# ----------------------------
st.markdown("""
<h1 class='main-title'>
🚑 EmergencyCare AI
</h1>

<p class='subtitle'>
AI-Powered Heart Disease Risk Assessment & Emergency Guidance
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class='card'>

<h3>❤️ Welcome</h3>

This application uses Artificial Intelligence and Machine Learning to estimate the likelihood of heart disease based on patient health information.

Fill in all the patient details below and click the <b>Predict Heart Disease Risk</b> button.

</div>
""", unsafe_allow_html=True)

st.markdown("## 📝 Patient Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input("Age",20,100,50)

    sex = st.selectbox(
        "Gender",
        ["Female","Male"]
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [0,1,2,3]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        80,
        220,
        120
    )

    chol = st.number_input(
        "Cholesterol",
        100,
        600,
        200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar >120",
        [0,1]
    )

    restecg = st.selectbox(
        "Rest ECG",
        [0,1,2]
    )

with col2:

    thalach = st.number_input(
        "Maximum Heart Rate",
        60,
        220,
        150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0,1]
    )

    oldpeak = st.number_input(
        "Old Peak",
        0.0,
        10.0,
        1.0
    )

    slope = st.selectbox(
        "Slope",
        [0,1,2]
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0,1,2,3,4]
    )

    thal = st.selectbox(
        "Thal",
        [0,1,2,3]
    )

sex = 1 if sex=="Male" else 0

st.divider()
# ----------------------------
# PREDICTION
# ----------------------------

if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):

    input_data = pd.DataFrame([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal

    ]], columns=[
        "age","sex","cp","trestbps","chol","fbs","restecg",
        "thalach","exang","oldpeak","slope","ca","thal"
    ])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)
    confidence = probability.max() * 100

    st.markdown("---")

    st.markdown("## 📊 Prediction Report")

    col1, col2 = st.columns([2,1])

    with col1:

        if prediction == 1:

            st.markdown("""
            <div class='result-low'>
            🟢 LOW RISK
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class='result-high'>
            🔴 HIGH RISK
            </div>
            """, unsafe_allow_html=True)

    with col2:

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    st.progress(int(confidence))

    st.markdown("---")

    st.markdown("## ❤️ AI Health Recommendations")

    if prediction == 1:

        st.success("""
✅ Your predicted risk is low.

### Maintain a Healthy Lifestyle

🥗 Eat fruits and vegetables

🚶 Exercise at least 30 minutes daily

💧 Drink enough water

😴 Sleep 7–8 hours

🚭 Avoid smoking

🩺 Get regular health checkups
""")

    else:

        st.error("""
⚠️ Your predicted risk is high.

### Immediate Recommendations

👨‍⚕️ Consult a Cardiologist

🩺 Schedule a Heart Check-up

🥗 Follow a Heart-Healthy Diet

🚭 Stop Smoking

🍺 Avoid Alcohol

💊 Follow Doctor's Advice
""")

    st.markdown("---")

    st.markdown("## 🚑 Emergency Contact Numbers")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("🚑 Ambulance","108")
    c2.metric("🚓 Police","100")
    c3.metric("🔥 Fire","101")
    c4.metric("☎ National","112")

    st.markdown("---")

    st.markdown("## 🏥 Nearby Hospitals")

    st.info(
        "Click the button below to locate nearby hospitals using Google Maps."
    )

    st.link_button(
        "🏥 Find Nearby Hospitals",
        "https://www.google.com/maps/search/hospitals+near+me",
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("## 📈 Health Risk Summary")

    if confidence >= 90:
        st.success("Prediction confidence is very high.")
    elif confidence >= 75:
        st.info("Prediction confidence is good.")
    else:
        st.warning("Prediction confidence is moderate.")

st.markdown("---")

st.markdown("---")

st.caption(
    "⚠️ This prediction is generated using Machine Learning for educational purposes only and should not replace professional medical advice."
)