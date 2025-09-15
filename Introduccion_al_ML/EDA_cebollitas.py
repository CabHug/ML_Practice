"""
This file contain the cleaning and EDA for cebollitas matches data .csv
"""

import pandas as pd


cebollitas_df = pd.read_csv(r'./partidos_cebollitas.csv')

# Show data frame structure
print(cebollitas_df.head())

# Show general info
print(cebollitas_df.info())

# Show missing values
print(cebollitas_df.isnull().sum())

# Transform categorical columns to numerical
processed_data = pd.get_dummies(cebollitas_df, columns=['equipo_local', 'equipo_visitante'])
print(processed_data.head())

# Date fields management
processed_data['fecha_partido'] = pd.to_datetime(processed_data['fecha_partido'], errors='coerce')

# after cleaning
print(processed_data.info())

# Shape of data
print(processed_data.shape)