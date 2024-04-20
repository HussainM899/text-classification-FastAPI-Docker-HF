from fastapi.testclient import TestClient
from main import app
from main import TextInput
from fastapi.encoders import jsonable_encoder

client = TestClient(app)

# Test the sentiment analysis endpoint for positive sentiment
def test_positive_sentiment():
    with client:
        # Define the request payload 
        # Initialize payload as a TextInput object
        payload = TextInput(text="I love this eating and sleeping")

        # Convert TextInput object to JSON-serializable dictionary
        payload_dict = jsonable_encoder(payload)
        
        # Send a POST request to the sentiment analysis endpoint
        response = client.post("/analyze/", json=payload_dict)

        # Assert that the response status code is 200 OK
        assert response.status_code == 200
        
        # Assert that the sentiment returned is positive
        assert response.json()[0]['label'] == "positive"

# Test the sentiment analysis endpoint for negative sentiment
def test_negative_sentiment():
    with client:
        # Define the request payload 
        # Initialize payload as a TextInput object
        payload = TextInput(text="I'm really disappointed with this service. It's terrible.")

        # Convert TextInput object to JSON-serializable dictionary
        payload_dict = jsonable_encoder(payload)
        
        # Send a POST request to the sentiment analysis endpoint
        response = client.post("/analyze/", json=payload_dict)

        # Assert that the response status code is 200 OK
        assert response.status_code == 200
        
        # Assert that the sentiment returned is negative
        assert response.json()[0]['label'] == "negative"

# Test the sentiment analysis endpoint for neutral sentiment
def test_neutral_sentiment():
    with client:
        # Define the request payload 
        # Initialize payload as a TextInput object
        payload = TextInput(text="This is a neutral statement.")

        # Convert TextInput object to JSON-serializable dictionary
        payload_dict = jsonable_encoder(payload)
        
        # Send a POST request to the sentiment analysis endpoint
        response = client.post("/analyze/", json=payload_dict)

        # Assert that the response status code is 200 OK
        assert response.status_code == 200
        
        # Assert that the sentiment returned is neutral
        assert response.json()[0]['label'] == "neutral"
