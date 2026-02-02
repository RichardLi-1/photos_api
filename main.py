from fastapi import FastAPI
app = FastAPI()

@app.post("/{240}/upload")
async def upload_photo():
    []
    return {"message": "Photo uploaded successfully"}