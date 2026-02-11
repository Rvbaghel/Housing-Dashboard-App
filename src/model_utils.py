import os
import joblib

MODEL_DIR = "models"

def load_city_model(city):
    model_path = os.path.join(MODEL_DIR, f"{city}_model.pkl")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No model found for {city}")
    
    model_info = joblib.load(model_path)
    
    return model_info["model"], model_info["r2"]
