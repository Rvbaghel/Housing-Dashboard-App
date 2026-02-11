from src.data_loader import load_city_data, get_supported_cities

print(get_supported_cities())
df = load_city_data("mumbai")
print(df.head())
