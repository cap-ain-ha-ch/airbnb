import streamlit as st
import pandas as pd
import joblib

MODEL_PATH = "airbnb_final_model.joblib"
model = joblib.load(MODEL_PATH)

st.set_page_config(page_title="AirBnB Price Predictor", page_icon="🏠")

st.title("🏠 AirBnB Price Predictor")
st.caption("Educational demonstration using the RentHop rental-listing dataset.")


latitude = st.number_input("Latitude", value=40.75, format="%.6f")

longitude = st.number_input("Longitude", value=-73.98, format="%.6f")

minimum_nights = st.number_input("Minimum Nights", 1, 365, 1, 1)

number_of_reviews = st.number_input("Number of Reviews", 0, 1000, 10, 1)

reviews_per_month = st.number_input("Reviews per Month", 0.0, 100.0, 2.5, 0.1)

calculated_host_listings_count = st.number_input(
    "Host's Total Listings", 1, 1000, 1, 1
)

availability_365 = st.number_input(
    "Availability (Days per Year)", 0, 365, 200, 1
)

neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
)

room_type = st.selectbox(
    "Room Type",
    ["Entire home/apt", "Private room", "Shared room"]
)

if st.button("Predict Airbnb Price"):

    row = pd.DataFrame([{
        "latitude": latitude,
        "longitude": longitude,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": calculated_host_listings_count,
        "availability_365": availability_365,
        "neighbourhood_group": neighbourhood_group,
        "room_type": room_type
    }])

    prediction = model.predict(row)[0]

    st.success(f"Predicted Nightly Price: ${prediction:.2f}")

st.info(
    "Educational demonstration only. Predictions are estimates, "
    "not guaranteed Airbnb prices."
)
