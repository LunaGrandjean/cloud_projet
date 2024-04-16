CREATE TABLE raw_sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id INT,
    timestamp TIMESTAMP,
    sensor_value FLOAT
);

CREATE TABLE processed_data (
    id SERIAL PRIMARY KEY,
    sensor_id INT,
    timestamp TIMESTAMP,
    processed_value FLOAT
);
