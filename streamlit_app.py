import streamlit as st
import numpy as np
import pickle

# Load the saved heart disease prediction model
model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Language setting
if "lang" not in st.session_state:
    st.session_state.lang = "en"

def toggle_language():
    st.session_state.lang = "ar" if st.session_state.lang == "en" else "en"

# Language texts without emojis (only in title and result messages)
texts = {
    "en": {
        "title": "💖 Heart Disease Prediction System",
        "age": "Age",
        "sex": "Sex",
        "male": "Male",
        "female": "Female",
        "cp": "Chest Pain Type",
        "trestbps": "Resting Blood Pressure",
        "fbs": "Fasting Blood Sugar > 120 mg/dl",
        "thalach": "Maximum Heart Rate Achieved",
        "chol": "Cholesterol Level",
        "restecg": "Resting Electrocardiographic Results",
        "exang": "Exercise Induced Angina",
        "oldpeak": "ST Depression Induced by Exercise",
        "slope": "Slope of the Peak Exercise ST Segment",
        "ca": "Number of Major Vessels",
        "thal": "Thalassemia",
        "predict": "Predict",
        "result_yes": "🚨 The model predicts the presence of heart disease.",
        "result_no": "✅ The model predicts no presence of heart disease.",
        "change_language": "Change Language",
        "yes": "Yes",
        "no": "No",
        "cp_options": ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"],
        "restecg_options": ["Normal", "Having ST-T Wave Abnormality", "Showing Probable or Definite Left Ventricular Hypertrophy"],
        "slope_options": ["Upsloping", "Flat", "Downsloping"],
        "thal_options": ["Normal", "Fixed Defect", "Reversible Defect"]
    },
    "ar": {
        "title": "💖 نظام التنبؤ بأمراض القلب",
        "age": "العمر",
        "sex": "الجنس",
        "male": "ذكر",
        "female": "أنثى",
        "cp": "نوع ألم الصدر",
        "trestbps": "ضغط الدم أثناء الراحة",
        "fbs": "سكر الدم أثناء الصيام > 120 مجم/دل",
        "thalach": "أقصى معدل ضربات قلب محقق",
        "chol": "مستوى الكوليسترول",
        "restecg": "نتائج تخطيط القلب أثناء الراحة",
        "exang": "ذبحة صدرية ناتجة عن التمرين",
        "oldpeak": "انخفاض ST الناتج عن التمرين",
        "slope": "ميل ST أثناء التمرين",
        "ca": "عدد الأوعية الرئيسية",
        "thal": "الثلاسيميا",
        "predict": "تنبؤ",
        "result_yes": "🚨 النموذج يتوقع وجود أمراض القلب.",
        "result_no": "✅ النموذج يتوقع عدم وجود أمراض القلب.",
        "change_language": "تغيير اللغة",
        "yes": "نعم",
        "no": "لا",
        "cp_options": ["ذبحة صدرية نموذجية", "ذبحة صدرية غير نموذجية", "ألم غير قلبي", "بدون أعراض"],
        "restecg_options": ["طبيعي", "وجود اضطراب موجة ST-T", "إظهار تضخم بطين أيسر محتمل أو مؤكد"],
        "slope_options": ["تصاعدي", "مسطح", "تنازلي"],
        "thal_options": ["طبيعي", "عيب ثابت", "عيب قابل للتراجع"]
    }
}

# Mapping Arabic options to English options
option_mapping = {
    "cp_options": {
        "ذبحة صدرية نموذجية": "Typical Angina",
        "ذبحة صدرية غير نموذجية": "Atypical Angina",
        "ألم غير قلبي": "Non-Anginal Pain",
        "بدون أعراض": "Asymptomatic"
    },
    "restecg_options": {
        "طبيعي": "Normal",
        "وجود اضطراب موجة ST-T": "Having ST-T Wave Abnormality",
        "إظهار تضخم بطين أيسر محتمل أو مؤكد": "Showing Probable or Definite Left Ventricular Hypertrophy"
    },
    "slope_options": {
        "تصاعدي": "Upsloping",
        "مسطح": "Flat",
        "تنازلي": "Downsloping"
    },
    "thal_options": {
        "طبيعي": "Normal",
        "عيب ثابت": "Fixed Defect",
        "عيب قابل للتراجع": "Reversible Defect"
    }
}

# Streamlit app title
st.title(texts[st.session_state.lang]["title"])

# Language change button
st.button(texts[st.session_state.lang]["change_language"], on_click=toggle_language)

# Layout with columns for inputs
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(texts[st.session_state.lang]["age"], min_value=1, max_value=120)
    sex = st.selectbox(texts[st.session_state.lang]["sex"], [texts[st.session_state.lang]["female"], texts[st.session_state.lang]["male"]])
    cp = st.selectbox(texts[st.session_state.lang]["cp"], texts[st.session_state.lang]["cp_options"])
    trestbps = st.number_input(texts[st.session_state.lang]["trestbps"], min_value=80, max_value=200)
    fbs = st.selectbox(texts[st.session_state.lang]["fbs"], [texts[st.session_state.lang]["no"], texts[st.session_state.lang]["yes"]])
    thalach = st.number_input(texts[st.session_state.lang]["thalach"], min_value=60, max_value=220)

with col2:
    chol = st.number_input(texts[st.session_state.lang]["chol"], min_value=100, max_value=400)
    restecg = st.selectbox(texts[st.session_state.lang]["restecg"], texts[st.session_state.lang]["restecg_options"])
    exang = st.selectbox(texts[st.session_state.lang]["exang"], [texts[st.session_state.lang]["no"], texts[st.session_state.lang]["yes"]])
    oldpeak = st.number_input(texts[st.session_state.lang]["oldpeak"])
    slope = st.selectbox(texts[st.session_state.lang]["slope"], texts[st.session_state.lang]["slope_options"])
    ca = st.selectbox(texts[st.session_state.lang]["ca"], [0, 1, 2, 3, 4])
    thal = st.selectbox(texts[st.session_state.lang]["thal"], texts[st.session_state.lang]["thal_options"])

# Map text inputs to numerical values for the model
sex = 1 if sex == texts[st.session_state.lang]["male"] else 0
cp = texts["en"]["cp_options"].index(option_mapping["cp_options"].get(cp, cp))  # Map Arabic to English if needed
fbs = 1 if fbs == texts[st.session_state.lang]["yes"] else 0
restecg = texts["en"]["restecg_options"].index(option_mapping["restecg_options"].get(restecg, restecg))
exang = 1 if exang == texts[st.session_state.lang]["yes"] else 0
slope = texts["en"]["slope_options"].index(option_mapping["slope_options"].get(slope, slope))
thal = texts["en"]["thal_options"].index(option_mapping["thal_options"].get(thal, thal))

# Prepare input data for prediction
input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
input_data = np.asarray(input_data).reshape(1, -1)

# Predict and display result
if st.button(texts[st.session_state.lang]["predict"]):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success(texts[st.session_state.lang]["result_yes"])
    else:
        st.success(texts[st.session_state.lang]["result_no"])
