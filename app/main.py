from fastapi import FastAPI, Response
import uuid
import asyncio
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/uuid")
def generate_uuid():
    return {"uuid": str(uuid.uuid4())}

@app.get("/async-uuid")
async def generate_async_uuid():
    await asyncio.sleep(3)  
    return {"async-uuid": str(uuid.uuid4())}

@app.get("/cat")
def get_random_cat():
    response = requests.get("https://cataas.com/cat")  
    if response.status_code == 200:
        return Response(content=response.content, media_type="image/jpeg")  
    return {"error": "Failed to fetch cat image"} 
