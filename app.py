import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Indian Housing Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🏠 Indian Housing App")

st.sidebar.markdown(
    """
    A data-driven housing analytics and price prediction app  
    built using **india-housing-datasets**.
    """
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Pages Available**
    - 📊 Dashboard  
    - 🔮 Prediction  
    - ℹ️ About  
    """
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **Author**  
    Vishal Baghel  

    🔗 [GitHub](https://github.com/Rvbaghel)  
    📦 [PyPI](https://pypi.org/project/india-housing-datasets/)
    """
)

# -----------------------------
# Main Page Content
# -----------------------------
st.title("🏠 Indian Housing Analytics & Prediction")

st.markdown(
    """
    Welcome to the **Indian Housing Dashboard** 👋  

    This application demonstrates how to use the  
    **india-housing-datasets** Python library to:

    - Explore housing data for major Indian cities  
    - Visualize key real estate trends  
    - Predict housing prices using machine learning  

    👉 Use the **sidebar** to navigate between pages.
    """
)

st.markdown("---")

st.success(
    "📊 Start by exploring the **Dashboard** page from the sidebar!"
)
