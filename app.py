import streamlit as st
import pandas as pd
import joblib
import json

model = joblib.load("loan_approval_model.pkl")
scaler = joblib.load("scaler.pkl")

education_encoder = joblib.load("education_encoder.pkl")
employment_encoder = joblib.load("employment_encoder.pkl")
status_encoder = joblib.load("status_encoder.pkl")

with open("columns (1).json", "r") as f:
    columns = json.load(f)
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦"
)

st.title("🏦 Loan Approval Prediction System")

st.write("Enter the applicant details and click Predict.")

no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=0
)

education = st.selectbox(
    "Education",
    [" Graduate", " Not Graduate"]
)


self_employed = st.selectbox(
    "Self Employed",
    [" Yes", " No"]
)


income_annum = st.number_input(
    "Annual Income",
    min_value=0,
    value=500000
)


loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=1000000
)


loan_term = st.number_input(
    "Loan Term",
    min_value=1,
    max_value=30,
    value=10
)


cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=700
)


residential_assets_value = st.number_input(
    "Residential Assets Value",
    min_value=0,
    value=2000000
)


commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    min_value=0,
    value=0
)


luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    min_value=0,
    value=500000
)


bank_asset_value = st.number_input(
    "Bank Asset Value",
    min_value=0,
    value=300000
)


if st.button("Predict Loan Status"):

    try:

        education_encoded = education_encoder.transform(
            [education]
        )[0]


        self_employed_encoded = employment_encoder.transform(
            [self_employed]
        )[0]

        input_data = pd.DataFrame([[
            no_of_dependents,
            education_encoded,
            self_employed_encoded,
            income_annum,
            loan_amount,
            loan_term,
            cibil_score,
            residential_assets_value,
            commercial_assets_value,
            luxury_assets_value,
            bank_asset_value
        ]], columns=columns)


        input_scaled = scaler.transform(input_data)


        prediction = model.predict(input_scaled)[0]

        prediction = status_encoder.inverse_transform(
            [prediction]
        )[0]

        st.write("### Prediction Result")

        st.write("Model Prediction:", prediction)


        result = str(prediction).strip().lower()


        if result == "approved":

            st.success("✅ Loan Approved")

        elif result == "rejected":

            st.error("❌ Loan Rejected")

        else:

            st.info(
                "Prediction: " + str(prediction)
            )


    except Exception as e:

        st.error("An error occurred during prediction.")

        st.write(e)