FROM python:3.9-slim
COPY src/ .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "anomaly_detector.py"]
