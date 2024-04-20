
# Urban Farm Sensor Management System

## Overview

This project implements a cloud architecture for managing sensor data from an urban vertical farm. The system collects real-time data from sensors monitoring various environmental parameters and stores this data for analysis and operational oversight. The architecture supports both Docker Compose for local deployment and Kubernetes for scalable deployments.

## Prerequisites

Before you begin, ensure you have the following installed:
- Docker
- Docker Compose
- Kubernetes cluster (Minikube or Kind)
- Helm (for Kubernetes deployments)

## Getting Started

### Using Docker Compose

1. Clone the repository:
   ```bash
   git clone https://github.com/LunaGrandjean/cloud_projet.git
   cd <project-directory>
   ```

2. Run the following command to start all services using Docker Compose:
   ```bash
   docker-compose up --build -d
   ```

This will pull the necessary Docker images, create containers, and start the services defined in the `docker-compose.yaml` file.

### Using Kubernetes

1. Start your Kubernetes cluster with Minikube or Kind:
   ```bash
   minikube start  # For Minikube
   kind create cluster  # For Kind
   ```

2. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/
   ```

3. Deploy services using Helm:
   ```bash
   helm install my-release <chart-location>  # For example, deploying PostgreSQL with Helm
   ```

## Architecture

This project consists of multiple independent components including a relational database, a REST API for accessing historical data, and a front-end for data visualization. The architecture is designed to detect anomalies in sensor data and provide timely notifications.

## Anomaly Detection

The system uses advanced algorithms to detect anomalies in sensor data. By analyzing data from various sensors, it identifies potential issues with sensor readings or environmental conditions affecting the plants.

## Monitoring

For monitoring the health of the system, Prometheus and Grafana can be integrated:
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm install prometheus prometheus-community/kube-prometheus-stack
   helm repo add grafana https://grafana.github.io/helm-charts
   helm install grafana grafana/grafana
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your changes.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

## Contact

For any queries or technical support, please contact [maxime.viel@epita.fr].
