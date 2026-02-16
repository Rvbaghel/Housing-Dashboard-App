import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# --------------------------------
# Page Title
# --------------------------------
st.title("👨‍💻 About This Project")

st.divider()

# --------------------------------
# About You
# --------------------------------
st.subheader("👋 Developer")

st.markdown("""
**Vishal Baghel**  
Computer Science Student | Data Science & ML Enthusiast  

I built this project to help students and beginners practice  
**Machine Learning, Data Visualization, and Regression Modeling**  
using standardized Indian housing datasets.
""")

st.divider()

# --------------------------------
# About the Library
# --------------------------------
st.subheader("📦 About the Library")

st.markdown("""
**india-housing-datasets** is a lightweight Python library providing:

- Standardized housing datasets for major Indian cities
- Clean and structured pandas DataFrames
- Ready-to-use data for ML practice
- Educational-focused synthetic datasets

It is designed for:
- Data Science learners
- ML practice
- Academic projects
- Portfolio building
""")

st.divider()

# --------------------------------
# Tech Stack
# --------------------------------
st.subheader("🛠 Tech Stack Used")

st.markdown("""
- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- Matplotlib & Seaborn  
- Joblib  
""")

st.divider()

# --------------------------------
# Project Links
# --------------------------------
st.subheader("🔗 Project Links")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📂 GitHub Repository  
    👉 https://github.com/Rvbaghel/india-housing-datasets
    """)

with col2:
    st.markdown("""
    ### 📦 PyPI Package  
    👉 https://pypi.org/project/india_housing_datasets/
    """)

st.divider()

# --------------------------------
# Call To Action
# --------------------------------
st.subheader("⭐ Support the Project")

st.markdown("""
If you found this useful:

- ⭐ Star the GitHub repository  
- 📢 Share with fellow learners  
- 🧠 Use it in your ML projects  
""")

st.divider()

st.caption("Built for educational purposes only.")
