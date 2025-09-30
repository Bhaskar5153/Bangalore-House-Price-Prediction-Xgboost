import streamlit as st
import pandas as pd
import pickle
import os

# load the model

model_path = os.path.join("artifacts", "xgb_model.pkl")
with open(file=model_path, mode='rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("Bangalore House Price Prediction App")

st.markdown("Enter the details to see the house price prediction")


area_type = st.selectbox(
    "Area Type",
    ['Super built-up  Area', 'Plot  Area', 'Built-up  Area',
       'Carpet  Area']
)

availability = st.selectbox(
    "Availability",
    ["Ready to Move", "Not Ready to move"]
)

location = st.text_input("Location", "Electronic City Phase II")
total_sqft = st.number_input("Total square feet", min_value=200.0, max_value=10000.0, value=1050.0)
bath = st.slider("Number of bathrooms", 1, 10, 2)
balcony = st.slider("Number of balcony", 0, 5, 1)
bhk = st.slider("Number of BKH", 1, 10, 2)

if st.button("Predict Price"):
    try:
        input_data = pd.DataFrame(
            [
                {
                    "area_type": area_type,
                    "availability": availability,
                    "location": location,
                    "total_sqft": total_sqft,
                    "bath": bath,
                    "balcony": balcony,
                    "bhk": bhk
                }
            ]
        )

        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Price: {round(float(prediction), 2)} Lakhs")

    except Exception as e:
        st.error(f"Error occured during the prediction: {str(e)}")