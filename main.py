import re
import string
import nltk
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from transformers import pipeline
from pyngrok import ngrok
import nest_asyncio
from fastapi.responses import RedirectResponse

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize FastAPI app
app = FastAPI()

# Text preprocessing functions
def remove_urls(text):
    return re.sub(r'http[s]?://\S+', '', text)

def remove_punctuation(text):
    regular_punct = string.punctuation
    return re.sub(r'['+regular_punct+']', '', text)

def lower_case(text):
    return text.lower()

def lemmatize(text):
    wordnet_lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(text)
    return ' '.join([wordnet_lemmatizer.lemmatize(w) for w in tokens])

# Model loading
lyx_pipe = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")

# Input data model
class TextInput(BaseModel):
    text: str

# Welcome endpoint
@app.get('/')
async def welcome():
    # Redirect to the Swagger UI page
    return RedirectResponse(url="/docs")

# Sentiment analysis endpoint
@app.post('/analyze/')
async def Predict_Sentiment(text_input: TextInput):    
    text = text_input.text

    # Text preprocessing
    text = remove_urls(text)
    text = remove_punctuation(text)
    text = lower_case(text)
    text = lemmatize(text)

    # Perform sentiment analysis
    try:
        return lyx_pipe(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI app using Uvicorn
if __name__ == "__main__":
    # Create ngrok tunnel
    ngrok_tunnel = ngrok.connect(8000)
    print('Public URL:', ngrok_tunnel.public_url)

    # Allow nested asyncio calls
    nest_asyncio.apply()

    # Run the FastAPI app with Uvicorn
    import uvicorn
    uvicorn.run(app, port=8000)