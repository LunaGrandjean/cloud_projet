import streamlit as st
import json
import pandas as pd
import numpy as np
import plotly.express as px
from sqlalchemy import create_engine
from pandas.io.json import json_normalize

engine = create_engine('postgresql://admin:securepass@db:5432/sensordata')



def fetch_sensor_data():
    query = """
    SELECT timestamp, measures
    FROM sensor_data
    ORDER BY timestamp DESC
    LIMIT 100
    """
    data = pd.read_sql(query, engine)
    
    # Convertir la chaîne JSON en un dictionnaire Python, supposer que les mesures sont stockées comme une chaîne JSON valide
    data['measures'] = data['measures'].apply(json.loads)

    # Normaliser les données JSON imbriquées dans une structure de dataframe plat
    measures_df = json_normalize(data['measures'])

    # Joindre les données normalisées avec le timestamp
    full_data = data.join(measures_df)
    
    return full_data


def main():
    st.title('Operator Dashboard')

    if st.button('Refresh Data'):
        full_data = fetch_sensor_data()
        
        # Affichage du DataFrame
        st.write(full_data)
        
        # Graphique de température
        fig_temp = px.line(full_data, x='timestamp', y='temperature', 
                           labels={'temperature': 'Temperature (°C)'}, 
                           title='Temperature Over Time')
        st.plotly_chart(fig_temp)
        
        # Graphique d'humidité
        fig_humidity = px.line(full_data, x='timestamp', y='humidity', 
                               labels={'humidity': 'Humidity (%)'}, 
                               title='Humidity Over Time')
        st.plotly_chart(fig_humidity)

if __name__ == "__main__":
    main()
