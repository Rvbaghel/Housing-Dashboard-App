# 🏠 Indian Housing Price Dashboard & Prediction App

A professional **Streamlit web application** built using the  
[`india-housing-datasets`](https://pypi.org/project/india-housing-datasets/) Python library.

This app allows users to:

- 📊 Explore housing data through interactive dashboards
- 🔥 Analyze feature correlations
- 📈 Visualize price distributions
- 🔮 Predict housing prices using Multiple Linear Regression
- 🧠 Understand how features affect pricing

---

## 🚀 Live Features

### 📊 Dashboard Page
- Price distribution histogram
- City-wise housing comparison
- Feature correlation heatmap
- Clean interactive UI

### 🔮 Prediction Page
- Select city
- Enter property details:
  - Area (sq ft)
  - BHK
  - Bathrooms
  - Property age
- Get:
  - Predicted price (₹ Lakhs)
  - Model accuracy (R² score)
  - Expected price range

### 👨‍💻 About Page
- Project overview
- Library details
- GitHub & PyPI links
- Tech stack used

---

## 📦 Python Library Used

This project uses:


Install separately:

```bash
pip install india-housing-datasets
PyPI:
https://pypi.org/project/india-housing-datasets/

GitHub:
https://github.com/Rvbaghel/india-housing-datasets

🛠 Tech Stack

.Python
.Streamlit
.Pandas
.Scikit-learn
.Matplotlib
.Seaborn
.Joblib

📂 Project Structure
housing-dashboard-app/
│
├── models/                  # Trained ML models (.pkl)
├── src/
│   ├── data_loader.py
│   ├── model_utils.py
│   └── visualizations.py
│
├── pages/
│   ├── dashboard.py
│   ├── prediction.py
│   └── about.py
│
├── app.py
└── README.md



🧠 Machine Learning Model
Each city has its own trained model using:

Multiple Linear Regression

Features used:

.area_sqft
.bhk
.bath
.age_years

Target:
.price_lakhs

Model performance is evaluated using:
.R² Score

▶️ How to Run Locally

Clone the repository:
git clone https://github.com/Rvbaghel/housing-dashboard-app.git
cd housing-dashboard-app

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py

⚠️ Disclaimer

The housing data used in this project is synthetic and standardized
for educational and machine learning practice purposes only.

It should NOT be used for:

.Real estate investment decisions

.Financial planning

.Market research

👨‍💻 Author

Vishal Baghel
Computer Science Student
Data Science & ML Enthusiast

📧 baghelvishal264@gmail.com

⭐ Support

If you found this project useful:

⭐ Star the repository

📢 Share with learners

🧠 Use it in ML practice projects


---

If you want, next I can:

• Add badges (build, version, license)  
• Make it more portfolio-level  
• Add demo GIF section  
• Add deployment instructions  
• Create requirements.txt  

Tell me 👌


