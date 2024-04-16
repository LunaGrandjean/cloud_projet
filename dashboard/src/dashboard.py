import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:securepass@db:5432/sensordata')

def fetch_sensor_data():
    query = """
    SELECT timestamp, temperature, humidity
    FROM sensor_data
    ORDER BY timestamp DESC
    LIMIT 100
    """
    data = pd.read_sql(query, engine)
    return data

def main():
    st.title('Operator Dashboard')

    if st.button('Refresh Data'):
        data = fetch_sensor_data()
        st.write(data)

        fig_temp = px.line(data, x='timestamp', y='temperature', labels={'timestamp': 'Timestamp', 'temperature': 'Temperature (°C)'}, title='Temperature Over Time')
        st.plotly_chart(fig_temp)

        fig_humidity = px.line(data, x='timestamp', y='humidity', labels={'timestamp': 'Timestamp', 'humidity': 'Humidity (%)'}, title='Humidity Over Time')
        st.plotly_chart(fig_humidity)

if __name__ == "__main__":
    main()
