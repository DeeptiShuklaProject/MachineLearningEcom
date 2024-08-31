# ML Project

## Overview

This project demonstrates a machine learning pipeline using supervised and unsupervised learning techniques. It includes data preprocessing, model training, evaluation, and deployment using Docker Compose.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd ml_project
    ```

3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

## Endpoints

- **POST /predict**
  - Request body: `{ "features": { "feature1": value, "feature2": value } }`
  - Response: `{ "prediction": "value" }`

## License

This project is licensed under the MIT License.
