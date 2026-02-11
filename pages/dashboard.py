import streamlit as st
import matplotlib.pyplot as plt

from src.data_loader import load_city_data, get_supported_cities


st.title("📊 Indian Housing Dashboard")
st.markdown("Explore housing data city-wise with detailed visual analytics.")

st.markdown("---")

# -----------------------------
# City selector (top)
# -----------------------------
city = st.selectbox("Select City", get_supported_cities())
df = load_city_data(city)


# -----------------------------
# Key Metrics
# -----------------------------
st.subheader("📌 Key Metrics")

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Avg Price (₹ Lakhs)", f"{df['price_lakhs'].mean():.2f}")
m2.metric("Avg Area (sqft)", f"{df['area_sqft'].mean():.0f}")
m3.metric("Avg BHK", f"{df['bhk'].mean():.1f}")
m4.metric("Avg Baths", f"{df['bath'].mean():.1f}")
m5.metric("Listings", len(df))

st.markdown("---")


# =============================
# SECTION 1: Price Distribution
# =============================
st.header("💰 Price Distribution")
st.markdown(
    "This histogram shows how housing prices are distributed in the selected city."
)

fig1, ax1 = plt.subplots(figsize=(14, 6))
ax1.hist(df["price_lakhs"], bins=30)
ax1.set_xlabel("Price (Lakhs ₹)")
ax1.set_ylabel("Number of Listings")

st.pyplot(fig1, use_container_width=True)

st.markdown("---")


# =============================
# SECTION 2: Area vs Price
# =============================
st.header("📐 Area vs Price Relationship")
st.markdown(
    "Scatter plot showing the relationship between property size and price."
)

fig2, ax2 = plt.subplots(figsize=(14, 6))
ax2.scatter(df["area_sqft"], df["price_lakhs"], alpha=0.4)
ax2.set_xlabel("Area (sqft)")
ax2.set_ylabel("Price (Lakhs ₹)")

st.pyplot(fig2, use_container_width=True)

st.markdown("---")


# =============================
# SECTION 3: BHK Distribution
# =============================
st.header("🏘️ BHK Distribution")
st.markdown(
    "Bar chart showing the distribution of BHK types in the selected city."
)

fig3, ax3 = plt.subplots(figsize=(14, 6))
df["bhk"].value_counts().sort_index().plot(kind="bar", ax=ax3)
ax3.set_xlabel("BHK")
ax3.set_ylabel("Count")

st.pyplot(fig3, use_container_width=True)

st.markdown("---")

st.header("📈 BHK vs Price Trend")
st.markdown(
    "This line chart shows how the **average housing price** changes with the number of bedrooms (BHK)."
)

# Group by BHK and calculate average price
bhk_price_df = (
    df.groupby("bhk")["price_lakhs"]
    .mean()
    .reset_index()
    .sort_values("bhk")
)

# Plot
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(
    bhk_price_df["bhk"],
    bhk_price_df["price_lakhs"],
    marker="o",
    linewidth=3
)

ax.set_xlabel("BHK")
ax.set_ylabel("Average Price (Lakhs ₹)")
ax.set_title(f"BHK vs Average Price – {city.title()}")
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig, use_container_width=True)


# =============================
# SECTION 4: Raw Data (Optional)
# =============================
st.header("📄 Dataset Preview")

with st.expander("Click to view raw dataset"):
    st.dataframe(df, use_container_width=True)


st.info(
    "📌 Note: This dataset is synthetically generated for educational and ML practice purposes."
)
