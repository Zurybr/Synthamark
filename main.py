import uvicorn 
from fastapi import FastAPI

#routes
from routes import userController

app = FastAPI()
app.include_router(userController.router)

@app.get('/')
def home():
    return 'hello world'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)