import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:securepass@db:5432/sensordata')

def process_data():
    # Exemple de traitement de données
    df = pd.read_sql("SELECT * FROM raw_sensor_data", engine)

    # Traitement des données
    df['processed_value'] = df['sensor_value'] * np.random.rand()

    # Insérer les données traitées
    df.to_sql('processed_data', engine, if_exists='append', index=False)

if __name__ == '__main__':
    process_data()
