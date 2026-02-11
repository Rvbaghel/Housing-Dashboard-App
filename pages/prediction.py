import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.model_utils import load_city_model
from src.data_loader import load_city_data, get_supported_cities


# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Housing Price Prediction",
    layout="wide"
)

# ------------------------------
# Page Title
# ------------------------------
st.title("🏠 Housing Price Prediction")
st.markdown(
    "Predict the **estimated housing price** based on city and property features. "
    "This tool is built for **educational and analytical purposes**."
)

st.divider()

# ------------------------------
# City Selection
# ------------------------------
st.subheader("📍 Select City")

city = st.selectbox(
    "Choose a city",
    get_supported_cities()
)

# Load dataset for selected city
df = load_city_data(city)

# ------------------------------
# Dataset Overview
# ------------------------------
st.subheader("📊 Dataset Overview")

colS1, colS2, colS3, colS4 = st.columns(4)

colS1.metric("Avg Price (₹ Lakhs)", round(df["price_lakhs"].mean(), 2))
colS2.metric("Avg Area (sq ft)", round(df["area_sqft"].mean(), 0))
colS3.metric("Max BHK", int(df["bhk"].max()))
colS4.metric("Max Area (sq ft)", int(df["area_sqft"].max()))

st.caption(
    "ℹ️ These values represent statistical distribution of the selected city's dataset."
)

st.divider()

# ------------------------------
# Feature Inputs
# ------------------------------
st.subheader("🏗️ Property Details")

col1, col2 = st.columns(2)

with col1:
    area_sqft = st.number_input(
        "Area (sq ft)",
        min_value=int(df["area_sqft"].min()),
        max_value=int(df["area_sqft"].max()),
        value=int(df["area_sqft"].mean()),
        step=50
    )

    bhk = st.slider(
        "BHK (Bedrooms)",
        min_value=int(df["bhk"].min()),
        max_value=int(df["bhk"].max()),
        value=int(df["bhk"].median())
    )

with col2:
    bath = st.slider(
        "Bathrooms",
        min_value=int(df["bath"].min()),
        max_value=int(df["bath"].max()),
        value=int(df["bath"].median())
    )

    age_years = st.slider(
        "Property Age (years)",
        min_value=int(df["age_years"].min()),
        max_value=int(df["age_years"].max()),
        value=int(df["age_years"].median())
    )

st.divider()

# ------------------------------
# Predict Button
# ------------------------------
predict_btn = st.button("🔮 Predict Price", use_container_width=True)

if predict_btn:

    model, r2 = load_city_model(city)

    input_data = np.array([[area_sqft, bhk, bath, age_years]])

    predicted_price = model.predict(input_data)[0]

    st.subheader("📊 Prediction Result")

    colA, colB = st.columns(2)

    with colA:
        st.metric(
            "Estimated Price (₹ Lakhs)",
            round(predicted_price, 2)
        )

    with colB:
        st.metric(
            "Model Accuracy (R²)",
            round(r2, 3)
        )

    # Expected price range
    low = predicted_price * 0.9
    high = predicted_price * 1.1

    st.write(
        f"Expected range: **₹ {low:.2f} – {high:.2f} Lakhs**"
    )

    st.markdown("---")

    st.subheader("📘 Model Details")

    st.markdown(
        """
        - Model Used: **Multiple Linear Regression**
        - Features Used:
            - Area (sq ft)
            - BHK
            - Bathrooms
            - Property Age
        - R² score indicates how well the model explains price variation.
        """
    )

    st.caption("⚠️ For educational purposes only.")

st.divider()

# ------------------------------
# Correlation Heatmap
# ------------------------------
# ------------------------------
# Correlation Heatmap
# ------------------------------
st.subheader("🔥 Feature Correlation Heatmap")

st.caption(
    "Correlation ranges from -1 to +1. "
    "Stronger colors indicate stronger relationships."
)

corr_features = df[[
    "area_sqft",
    "bhk",
    "bath",
    "age_years",
    "price_lakhs"
]].corr()

# Center layout
left, center, right = st.columns([1, 1.5, 1])

with center:
    fig, ax = plt.subplots(figsize=(5, 4))  # Controlled small size

    sns.heatmap(
        corr_features,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        square=True,
        linewidths=0.4,
        cbar=False,
        annot_kws={"size": 9},
        ax=ax
    )

    ax.tick_params(axis='x', rotation=30)
    ax.tick_params(axis='y', rotation=0)

    ax.set_title("Feature Correlation", fontsize=11)

    st.pyplot(fig, use_container_width=False)
