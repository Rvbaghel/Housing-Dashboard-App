from india_housing_datasets import load_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Load data
df = load_housing("mumbai")

# Features
X = df[["area_sqft", "bhk","bath", "age_years"]]
y = df["price_lakhs"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

# print("MAE:", mean_absolute_error(y_test, y_pred))
# print("R2 :", r2_score(y_test, y_pred))


# importance = model.coef_

# for feature, coef in zip(X.columns, importance):
#     print(f"{feature}: {coef:.2f}")

import seaborn as sns
import matplotlib.pylab as plt
corr = df[["area_sqft", "bhk", "bath", "age_years", "price_lakhs"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.show()
