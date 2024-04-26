# Text Classification API with FastAPI, Docker, and Hugging Face Transformers

This repository contains code for building a RESTful API using FastAPI to perform text classification (sentiment analysis, emotion classification, etc) using a pre-trained Hugging Face Transformer model. The API is containerized using Docker for easy deployment.

---

## Table of Contents

- [Overview](#overview)
- [Dependencies](#dependencies)
- [Models Used](#models-used)
- [Code Explanation](#code-explanation)
- [File Structure](#file-structure)
- [FastAPI Integration](#fastapi-integration)
- [Dockerization](#dockerization)
- [Hugging Face Model Details](#hugging-face-model-details)
- [Hugging Face Space Link](#hugging-face-space-link)
- [Building and Running the Container](#building-and-running-the-container)
- [Interacting with the API](#interacting-with-the-api)

---

## Overview

The main objective of this project is to develop a robust and scalable API for text classification tasks using FastAPI, Docker, and Hugging Face Transformers. The API allows users to submit text data and receive sentiment or emotion analysis results in real-time.

---

## Dependencies

The project relies on the following dependencies:

- **FastAPI:** A modern web framework for building APIs with Python.
- **Transformers:** The Hugging Face library for natural language processing (NLP) tasks, including pre-trained models.
- **Pyngrok:** A Python wrapper for ngrok, which exposes local servers over public URLs.
- **Nest_asyncio:** A library for running asyncio nested in other asyncio loops.
- **NLTK:** The Natural Language Toolkit for text processing tasks.
- **Pydantic:** A data validation library for Python.

---

## Code Explanation

The main components of the code include:

- **main.py:** This file contains the FastAPI application, including the definition of endpoints, request and response models, and model integration.
- **test.py:** This file contains unit tests for the API endpoints using FastAPI's TestClient.
- **Dockerfile:** The Dockerfile defines the environment and instructions for building the Docker image for the FastAPI application.
- **requirements.txt:** This file lists all the Python dependencies required by the project.

---

## FastAPI Integration

FastAPI is used to develop the RESTful API with the following endpoints:

- **GET /:** A welcome endpoint that redirects to the Swagger UI page.
- **POST /analyze/:** The main endpoint for text classification. It accepts JSON input with a text field and returns the sentiment/emotion analysis results.

---

## Dockerization

The project is containerized using Docker for easy deployment. The Dockerfile defines the environment and instructions for building the Docker image, including installing dependencies and running the FastAPI application.

---

## Hugging Face Model Details

The API utilizes the `distilbert-base-multilingual-cased-sentiments-student` model from the Hugging Face model hub. This model is a distilled version of the DistilBERT model trained for sentiment analysis tasks across multiple languages.

---

## Hugging Face Space Link

The trained model and associated resources are hosted on the following Hugging Face Space: [FastAPI-Docker-Huggingface-Text_Sentiment_app](https://huggingface.co/spaces/HussainM899/FastAPI-Docker-Huggingface-Text_Sentiment_app).

---

## Building and Running the Container

To build and run the Docker container, follow these steps:

1. Ensure you have Docker installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run the following command to build the Docker image:

```
docker build -t fastapi-test-sentiment-api-0.1.2 .
```

5. Once the image is built successfully, run the container with the following command:

```
docker run -d -p 8000:8000 fastapi-test-sentiment-api-0.1.2:latest
```

6. The API will now be accessible at `http://localhost:8000`.

---

## Interacting with the API

You can interact with the API using tools like cURL, Postman, or by sending HTTP requests programmatically. Alternatively, you can use the Swagger UI provided by FastAPI for easy testing and exploration.

1. Open your web browser and navigate to `http://localhost:8000/`.
2. This will open the Swagger UI interface, where you can explore the API endpoints and submit requests with sample data.
3. Click on the `/analyze/` endpoint, and then click on "Try it out" to input your text data.
4. After entering the text data, click on "Execute" to send the request and view the response, which will include the sentiment/emotion analysis results.

---

Feel free to explore the code and documentation for more details on how the API works and how to interact with it.


